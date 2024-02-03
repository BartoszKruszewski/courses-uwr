from pygame.mouse import get_pos, get_pressed

class Mouse:
    def __init__(self, on_right_click, on_right_hold, on_left_click, on_left_hold, on_right_release, on_left_release):
        self.on_right_click = on_right_click
        self.on_right_hold = on_right_hold
        self.on_right_release = on_right_release
        self.on_left_click = on_left_click
        self.on_left_hold = on_left_hold
        self.on_left_release = on_left_release
        self.__left_switch = False
        self.__right_switch = False

    def update(self):
        pos = get_pos()
        right, _, left = get_pressed()
        if right:
            if self.__right_switch:
                self.on_right_hold(pos)
            else:
                self.on_right_click(pos)
            self.__right_switch = True
        else:
            if self.__right_switch:
                self.on_right_release(pos)
            self.__right_switch = False

        if left:
            if self.__left_switch:
                self.on_left_hold(pos)
            else:
                self.on_left_click(pos)
            self.__left_switch = True
        else:
            if self.__left_switch:
                self.on_left_release(pos)
            self.__left_switch = False