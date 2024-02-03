from pygame import init, WINDOWCLOSE, quit, KEYDOWN, MOUSEWHEEL, KEYUP, Surface
from pygame.time import Clock
from pygame.display import set_mode, update as update_display
from pygame.event import get as get_event
from pygame.draw import line
from mouse import Mouse
from const import RESOLUTION, FRAMERATE, START_FONT_SIZE, SCROLL_SPEED, \
    CLICK_REPEAT_TIME, FIRST_ACTION_CLICK_MULT, MIN_FONT_SIZE, MAX_FONT_SIZE, \
    FONT_SIZE_CHANGE_SPEED, FONT_STYLES
from char_mapping import CHAR_MAPPING
from char import Char
from point import Point

class Main:
    def __init__(self):
        init()
        self.screen = set_mode(RESOLUTION)
        self.clock = Clock()
        self.mouse = Mouse(
            self.on_right_click,
            self.on_right_hold,
            self.on_left_click,
            self.on_left_hold,
            self.on_right_release,
            self.on_left_release
        )
        self.running = True
        self.scroll = Point(0, 0)
        self.font_size = START_FONT_SIZE
        self.time = 0
        self.click_time = 0
        self.clicked_key = None
        self.chars = {char:Char(*data) for char, data in CHAR_MAPPING.items()}
        self.text = ''
        self.cursor = 0
        self.end = 0
        self.style = 0

        while self.running:
            self.running = not get_event(WINDOWCLOSE)
            self.handle_events()
            self.mouse.update()
            self.update_screen()
        quit()
    
    def select_delete(self):
        a = min(self.end, self.cursor)
        b = max(self.end, self.cursor)
        self.text = self.text[:a] + self.text[b:]

    def on_keydown(self, key):
        char = None
        if 0 <= key <= 0x10ffff and chr(key) in self.chars:
            char = chr(key)
        elif key == 32: # space
            char = ' '
        elif key == 13: # enter
            char = '\n'
        elif key == 61: # =
            self.font_size += FONT_SIZE_CHANGE_SPEED
            self.font_size = min(self.font_size, MAX_FONT_SIZE)
        elif key == 45: # =
            self.font_size -= FONT_SIZE_CHANGE_SPEED
            self.font_size = max(self.font_size, MIN_FONT_SIZE)
        elif key == 1073741904: # left arrow
            self.cursor -= 1
        elif key == 1073741903: # right arrow
            self.cursor += 1
        elif key == 1073741906: # up arrow
            self.cursor -= 1
            while self.cursor >= 0 and self.text[self.cursor] != '\n':
                self.cursor -= 1
        elif key == 1073741905: # down arrow
            self.cursor += 1
            while len(self.text) > self.cursor and self.text[self.cursor] != '\n':
                self.cursor += 1
        elif key == 8: # backspace
            if self.end != self.cursor:
                self.select_delete()
            elif self.cursor > 0:
                self.text = self.text[:self.cursor - 1] + self.text[self.cursor:]
                self.cursor -= 1
        elif key == 127: # delete
            if self.end != self.cursor:
                self.select_delete()
            elif self.cursor < len(self.text):
                self.text = self.text[:self.cursor] + self.text[self.cursor + 1:]
        elif key == 1073742048: # left ctrl
            self.style += 1
            if self.style == len(FONT_STYLES):
                self.style = 0
        if char is not None:
            if self.end != self.cursor:
                self.select_delete()
            self.text = self.text[:self.cursor] + char + self.text[self.cursor:]
            self.cursor += 1
        self.cursor = max(self.cursor, 0)
        self.cursor = min(self.cursor, len(self.text))
        if self.cursor == len(self.text):
            self.scroll.y = max(
                (self.text.count('\n') + 1) * self.font_size - RESOLUTION[1],
                self.scroll.y
            )
        l = self.cursor - 1
        while l > 0 and self.text[l] != '\n':
            l -= 1
        if l == self.cursor - 1:
            self.scroll.x = 0
        else:
            l = (self.cursor - l) * self.font_size
            self.scroll.x = max(l - RESOLUTION[0], self.scroll.x)
        self.end = self.cursor

    def handle_events(self):
        for e in get_event():
            if e.type == KEYDOWN:
                self.clicked_key = e.key
                self.click_time = 0
            if e.type == KEYUP:
                if e.key == self.clicked_key:
                    self.clicked_key = None
            elif e.type == MOUSEWHEEL:
                self.scroll.x += e.x * self.dt * SCROLL_SPEED
                self.scroll.y -= e.y * self.dt * SCROLL_SPEED
                self.scroll.x = max(self.scroll.x, 0)
                self.scroll.y = max(self.scroll.y, 0)
        if self.clicked_key is not None:
            if self.click_time == 0:
                self.on_keydown(self.clicked_key)
            if self.click_time > \
                CLICK_REPEAT_TIME * FIRST_ACTION_CLICK_MULT:
                self.click_time %= CLICK_REPEAT_TIME
                self.click_time += CLICK_REPEAT_TIME * (FIRST_ACTION_CLICK_MULT - 1)
                self.on_keydown(self.clicked_key)
            self.click_time += self.dt

    def on_right_click(self, pos):
        cord = (Point(pos[0], pos[1]) + self.scroll) // self.font_size
        rows = self.text.split('\n')
        self.cursor = 0
        for i in range(min(cord.y, len(rows))):
            self.cursor += len(rows[i]) + 1
        if cord.y < len(rows):
            self.cursor += min(len(rows[cord.y]), cord.x)
        self.end = self.cursor

    def on_right_hold(self, pos):
        cord = (Point(pos[0], pos[1]) + self.scroll) // self.font_size
        rows = self.text.split('\n')
        self.end = 0
        for i in range(min(cord.y, len(rows))):
            self.end += len(rows[i]) + 1
        if cord.y < len(rows):
            self.end += min(len(rows[cord.y]), cord.x)

    def on_left_click(self, pos):
        pass

    def on_left_hold(self, pos):
        pass

    def on_right_release(self, pos):
        pass

    def on_left_release(self, pos):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))
        pos = Point(0, 0)
        selected_surf = Surface((self.font_size, self.font_size))
        selected_surf.fill((255, 0, 0))
        cursor_pos = None
        end_pos = None
        for i, char in enumerate(self.text):
            if i + 1 == self.cursor:
                cursor_pos = pos - self.scroll
            if i + 1 == self.end:
                end_pos = pos - self.scroll
            if self.cursor <= i < self.end or self.end <= i < self.cursor:
                self.screen.blit(selected_surf, tuple(pos - self.scroll))
            if char == '\n':
                pos.x = 0
                pos.y += self.font_size
            elif char == ' ':
                pos.x += self.font_size
            elif char in self.chars:
                self.chars[char].draw(
                    self.screen, self.font_size, pos - self.scroll, FONT_STYLES[self.style])
                pos.x += self.font_size
        if self.time % FRAMERATE < FRAMERATE // 2:
            if cursor_pos is not None:
                if len(self.text) > 0 and self.text[self.cursor - 1] == '\n':
                    cursor_pos = Point(-self.font_size, cursor_pos.y + self.font_size)
                line(
                    self.screen, 'white',
                    (cursor_pos.x + self.font_size, cursor_pos.y),
                    (cursor_pos.x + self.font_size, cursor_pos.y + self.font_size)
                )
            if end_pos is not None:
                if len(self.text) > 0 and self.text[self.cursor - 1] == '\n':
                    end_pos = Point(-self.font_size, end_pos.y + self.font_size)
                line(
                    self.screen, 'white',
                    (end_pos.x + self.font_size, end_pos.y),
                    (end_pos.x + self.font_size, end_pos.y + self.font_size)
                )
        
    def update_screen(self):
        self.draw()
        update_display()
        self.dt = self.clock.tick(FRAMERATE) / 1000 * FRAMERATE
        self.time += self.dt

if __name__ == '__main__':
    Main()

    