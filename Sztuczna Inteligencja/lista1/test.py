from collections import deque

BOARD_SIZE = 8

class Field:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def in_board(self):
        return 0 <= self.row < BOARD_SIZE and 0 <= self.col < BOARD_SIZE

    def __eq__(self, other):
        return isinstance(other, Field) and self.row == other.row and self.col == other.col

    def __hash__(self):
        return hash((self.row, self.col))

    def __repr__(self):
        # Reprezentacja w postaci (row, col)
        return f"({self.row}, {self.col})"

class GameState:
    def __init__(self, wk: Field, wr: Field, bk: Field, turn: str):
        """
        wk – pozycja białego króla,
        wr – pozycja białej wieży,
        bk – pozycja czarnego króla,
        turn – 'W' (białe) lub 'B' (czarne)
        """
        self.wk = wk
        self.wr = wr
        self.bk = bk
        self.turn = turn  # 'W' lub 'B'

    def is_legal(self):
        # Stan jest legalny, jeśli:
        # - Żadne dwie figury nie zajmują tego samego pola,
        # - Królowie nie sąsiadują (nie mogą stać obok siebie).
        if self.wk == self.wr or self.wk == self.bk or self.wr == self.bk:
            return False
        if MovesGenerator.kings_adjacent(self.wk, self.bk):
            return False
        return True

    def __eq__(self, other):
        return (isinstance(other, GameState) and
                self.wk == other.wk and
                self.wr == other.wr and
                self.bk == other.bk and
                self.turn == other.turn)

    def __hash__(self):
        return hash((self.wk, self.wr, self.bk, self.turn))

    def __repr__(self):
        return f"GameState(wk={self.wk}, wr={self.wr}, bk={self.bk}, turn={self.turn})"

class MovesGenerator:
    @staticmethod
    def kings_adjacent(f1: Field, f2: Field) -> bool:
        return abs(f1.row - f2.row) <= 1 and abs(f1.col - f2.col) <= 1

    @staticmethod
    def rook_attacks(rook: Field, target: Field, blocking: Field) -> bool:
        """
        Wieża atakuje, jeśli cel jest w tym samym wierszu lub kolumnie
        i między wieżą a celem nie ma przeszkody (tutaj: białego króla).
        """
        if rook.row == target.row:
            c1, c2 = sorted([rook.col, target.col])
            if blocking.row == rook.row and c1 < blocking.col < c2:
                return False
            return True
        elif rook.col == target.col:
            r1, r2 = sorted([rook.row, target.row])
            if blocking.col == rook.col and r1 < blocking.row < r2:
                return False
            return True
        return False

    @staticmethod
    def white_attacks_black(wk: Field, wr: Field, bk: Field) -> bool:
        """
        Biała wieża (ewentualnie wspierana przez białego króla, który nie może być zbyt daleko)
        atakuje czarnego króla, gdy:
          - czarny król znajduje się w tym samym wierszu lub kolumnie co wieża,
          - między wieżą a czarnym królem nie stoi biały król.
        """
        # W praktyce atak szachujący daje tylko wieża.
        if (wr.row == bk.row or wr.col == bk.col) and MovesGenerator.rook_attacks(wr, bk, wk):
            return True
        return False

    @staticmethod
    def generate_white_moves(state: GameState) -> list:
        moves = []
        if state.turn != 'W':
            return moves
        wk, wr, bk = state.wk, state.wr, state.bk

        # Ruchy białego króla – wszystkie sąsiednie pola
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                new_wk = Field(wk.row + dr, wk.col + dc)
                if not new_wk.in_board():
                    continue
                # Biały król nie może stanąć obok czarnego króla ani na zajętym polu
                if MovesGenerator.kings_adjacent(new_wk, bk):
                    continue
                if new_wk == wr or new_wk == bk:
                    continue
                new_state = GameState(new_wk, wr, bk, 'B')
                if new_state.is_legal():
                    moves.append(new_state)

        # Ruchy białej wieży – ruchy w poziomie i pionie
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for d in directions:
            r, c = wr.row, wr.col
            while True:
                r += d[0]
                c += d[1]
                new_field = Field(r, c)
                if not new_field.in_board():
                    break
                # Wieża nie może "przeskoczyć" ani zająć pola zajętego przez króla
                if new_field == wk or new_field == bk:
                    break
                new_state = GameState(wk, new_field, bk, 'B')
                if new_state.is_legal():
                    moves.append(new_state)
        return moves

    @staticmethod
    def generate_black_moves(state: GameState) -> list:
        moves = []
        if state.turn != 'B':
            return moves
        wk, wr, bk = state.wk, state.wr, state.bk

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                new_bk = Field(bk.row + dr, bk.col + dc)
                if not new_bk.in_board():
                    continue
                # Czarny król nie może stanąć obok białego króla ani na zajętych polach
                if MovesGenerator.kings_adjacent(new_bk, wk):
                    continue
                if new_bk == wk or new_bk == wr:
                    continue
                # Czarny król nie może przejść na pole atakowane przez białą wieżę
                if MovesGenerator.white_attacks_black(wk, wr, new_bk):
                    continue
                new_state = GameState(wk, wr, new_bk, 'W')
                if new_state.is_legal():
                    moves.append(new_state)
        return moves

class BFS:
    def __init__(self, initial_state: GameState):
        self.initial_state = initial_state

    def is_checkmate(self, state: GameState) -> bool:
        """
        Stan uznajemy za mata, gdy:
         - kolej ruchu należy do czarnych,
         - czarny król jest szachowany (przez wieżę),
         - czarny król nie ma żadnych legalnych ruchów.
        """
        if state.turn != 'B':
            return False
        wk, wr, bk = state.wk, state.wr, state.bk
        if not MovesGenerator.white_attacks_black(wk, wr, bk):
            return False
        if MovesGenerator.generate_black_moves(state):
            return False
        return True

    def search(self) -> int:
        queue = deque()
        queue.append((self.initial_state, 0))
        visited = set()

        while queue:
            state, moves = queue.popleft()
            # Jeśli kolej czarnych i pozycja jest mata, zwracamy liczbę półruchów
            if state.turn == 'B' and self.is_checkmate(state):
                return moves
            if state in visited:
                continue
            visited.add(state)

            if state.turn == 'W':
                next_states = MovesGenerator.generate_white_moves(state)
            else:
                next_states = MovesGenerator.generate_black_moves(state)

            for ns in next_states:
                if ns not in visited:
                    queue.append((ns, moves + 1))
        return -1  # teoretycznie zawsze da się zamatować

def parse_position(pos_str: str) -> Field:
    """
    Konwertuje pozycję w notacji algebraicznej (np. "g8") do obiektu Field.
    Przyjmujemy, że:
      - Kolumna: 'a' -> 0, 'b' -> 1, ... 'h' -> 7.
      - Rząd: '1' -> 0, '2' -> 1, ... '8' -> 7.
    """
    file_char = pos_str[0].lower()
    rank_char = pos_str[1]
    col = ord(file_char) - ord('a')
    row = int(rank_char) - 1
    return Field(row, col)

def parse_input(filename: str):
    """
    Oczekiwany format wejścia:
       <turn> <black_king> <white_king> <white_rook>
    Przykładowy wiersz:
       black g8 h1 c4
    """
    with open(filename, 'r') as f:
        line = f.readline().strip()
        tokens = line.split()
        if len(tokens) != 4:
            raise ValueError("Niepoprawny format wejścia. Oczekiwany format: <turn> <black_king> <white_king> <white_rook>")
        turn_token = tokens[0].lower()
        if turn_token == 'black':
            turn = 'B'
        elif turn_token == 'white':
            turn = 'W'
        else:
            raise ValueError("Niepoprawny token określający kolejność ruchu (black/white).")
        # Ustalamy kolejność: token[1] -> black king, token[2] -> white king, token[3] -> white rook
        bk_str = tokens[1]
        wk_str = tokens[2]
        wr_str = tokens[3]
        return turn, wk_str, wr_str, bk_str

def main():
    input_file = "zad1_input.txt"
    output_file = "zad1_output.txt"

    try:
        turn, wk_str, wr_str, bk_str = parse_input(input_file)
    except Exception as e:
        with open(output_file, 'w') as out:
            out.write(f"Błąd podczas parsowania wejścia: {e}\n")
        return

    wk = parse_position(wk_str)
    wr = parse_position(wr_str)
    bk = parse_position(bk_str)
    initial_state = GameState(wk, wr, bk, turn)

    bfs_solver = BFS(initial_state)
    result = bfs_solver.search()

    with open(output_file, 'w') as f:
        if result != -1:
            f.write(str(result))
        else:
            f.write("Nie znaleziono sekwencji prowadzącej do mata.\n")

if __name__ == '__main__':
    main()