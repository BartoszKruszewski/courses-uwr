#include <iostream>
#include "GameState.h"

namespace display {
    void printBoard(const gameState::GameState &gameState) {
        std::cout << "   a   b   c" << std::endl;
        std::cout << "1  " << gameState.getState(0) << " | " <<
                  gameState.getState(1) << " | " <<
                  gameState.getState(2) << std::endl;
        std::cout << "  ---+---+---" << std::endl;
        std::cout << "2  " << gameState.getState(3) << " | " <<
                  gameState.getState(4) << " | " <<
                  gameState.getState(5) << std::endl;
        std::cout << "  ---+---+---" << std::endl;
        std::cout << "3  " << gameState.getState(6) << " | " <<
                  gameState.getState(7) << " | " <<
                  gameState.getState(8) << std::endl;
    }
}

namespace input {
    int rowColToFieldID(char col, int row) {
        int fieldId = (row - 1) * 3;
        if (col == 'b') fieldId++;
        else if (col == 'c') fieldId += 2;
        return fieldId;
    }

    std::pair<char, int> inputToRowCol(const std::string &fieldChoice) {
        char col;
        int row;

        for (char field: fieldChoice) {
            if (field == '1' || field == '2' || field == '3')
                row = (int) field - 48;
            else if (tolower(field) == 'a' || tolower(field) == 'b' || tolower(field) == 'c')
                col = tolower(field);
            else
                return std::make_pair('x', 0);
        }
        return std::make_pair(col, row);
    }

    bool isCorrectFieldChoice(const std::string &fieldChoice, const gameState::GameState &gameState) {
        // sprawdzanie długości wczytanego stringa
        if (fieldChoice.length() != 2) return false;

        std::pair<char, int> choice = inputToRowCol(fieldChoice);

        if (choice.first == 'x')
            return false;

        char col = choice.first;
        int row = choice.second;


        // sprawdzanie, czy wybrane pole jest puste
        if (gameState.getState(rowColToFieldID(col, row)) != ' ') return false;

        return true;
    }
}

namespace AI {
    int computerChoice(const gameState::GameState &gameState) {

        // sprawdzanie, czy komputer lub gracz może wygrać w jednym ruchu
        const char SYMBOL[2] = {'o', 'x'};
        for (const char symbol: SYMBOL)
            for (auto combination: gameState.COMBINATIONS) {
                if (gameState.getState(combination[0]) == ' ' &&
                    gameState.getState(combination[1]) == symbol &&
                    gameState.getState(combination[2]) == symbol)
                    return combination[0];
                if (gameState.getState(combination[0]) == symbol &&
                    gameState.getState(combination[1]) == ' ' &&
                    gameState.getState(combination[2]) == symbol)
                    return combination[1];
                if (gameState.getState(combination[0]) == symbol &&
                    gameState.getState(combination[1]) == symbol &&
                    gameState.getState(combination[2]) == ' ')
                    return combination[2];
            }

        // wybór pola według jego przynależności do większej liczby rzędów
        const int PRIORITY[9] = {4, 0, 2, 6, 8, 1, 3, 5, 7};
        for (int fieldID: PRIORITY) {
            if (gameState.getState(fieldID) == ' ') return fieldID;
        }
        return 0;
    }
}

int main() {

    // utworzenie obiektu stanu gry
    gameState::GameState gameState;

    // utworzenie zmiennych przechowujących informacje o wyniku gry
    bool isPlayerWin = false;
    bool isComputerWin = false;
    std::string fieldChoice;

    // wstępne rysowanie planszy
    display::printBoard(gameState);

    // główna pętla gry
    while (!(isPlayerWin || isComputerWin || gameState.isFull())) {

        // wczytywanie numeru pola od gracza
        std::cout << "Podaj numer pola: ";
        std::cin >> fieldChoice;
        while (!input::isCorrectFieldChoice(fieldChoice, gameState)) {
            std::cout << "Bledny numer pola, podaj inny: ";
            std::cin >> fieldChoice;
        }

        std::pair<char, int> choice = input::inputToRowCol(fieldChoice);

        char col = choice.first;
        int row = choice.second;

        // zapisywanie wyboru gracza
        gameState.save(input::rowColToFieldID(col, row), true);

        // zapisywanie wyboru komputera
        gameState.save(AI::computerChoice(gameState), false);

        // rysowanie planszy
        display::printBoard(gameState);

        // sprawdzanie wyniku gry
        isPlayerWin = gameState.isWin(true);
        isComputerWin = gameState.isWin(false);
    }

    // wypisywanie wyniku
    if (isPlayerWin) std::cout << "Gracz wygral!" << std::endl;
    else if (isComputerWin) std::cout << "Komputer wygral!" << std::endl;
    else std::cout << "Remis!" << std::endl;

    return 0;
}








