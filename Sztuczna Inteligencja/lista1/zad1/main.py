import argparse


class Main:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--debug", action="store_true")
        args = parser.parse_args()
        self.debug = args.debug

        try:
            with open("zad1_input.txt", "r") as f:
                self.lines = f.readlines()
        except FileNotFoundError:
            print("'zad1_input.txt' not exists!")
            return

        results = []

    def run()
    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) != 4:
            print(f"Niepoprawny format linii: {line}")
            continue
        turn_str, pos_wk, pos_wr, pos_bk = parts
        # Konwersja pozycji
        wk = pos_to_coord(pos_wk)
        wr = pos_to_coord(pos_wr)
        bk = pos_to_coord(pos_bk)
        # Sprawdzenie legalności pozycji – figury nie mogą zajmować tego samego pola,
        # a król biały i czarny nie mogą być sąsiadami.
        if wk == wr or wk == bk or wr == bk:
            results.append("INF")
            continue
        if kings_adjacent(wk, bk):
            results.append("INF")
            continue
        
        initial_state = (wk, wr, bk, turn_str.lower())
        moves, path = find_min_moves(initial_state)
        if moves == "INF":
            results.append("INF")
        else:
            results.append(str(moves))
        if DEBUG and moves != "INF":
            print("Sekwencja ruchów prowadząca do mata:")
            for s in path:
                print_state(s)
    
    # Zapis wyników do pliku "zad1_output.txt"
    with open("zad1_output.txt", "w") as f_out:
        for res in results:
            f_out.write(res + "\n")

if __name__ == "__main__":
    main()