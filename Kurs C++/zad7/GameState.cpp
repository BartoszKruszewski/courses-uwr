#include "GameState.h"

void gameState::GameState::save(int fieldID, bool isPlayer) {
    if (isPlayer) board[fieldID] = 'x';
    else board[fieldID] = 'o';
}

char gameState::GameState::getState(int fieldID) const {
    return board[fieldID];
}

bool gameState::GameState::isWin(bool isPlayer) const {
    char symbol;
    if (isPlayer) symbol = 'x';
    else symbol = 'o';
    for (auto combination: COMBINATIONS)
        if (board[combination[0]] == symbol && board[combination[1]] == symbol && board[combination[2]] == symbol)
            return true;
    return false;
}

bool gameState::GameState::isFull() const {
    for (char i : board) if (i == ' ') return false;
    return true;
}
