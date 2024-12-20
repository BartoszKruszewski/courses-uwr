#pragma once


namespace gameState {
    class GameState {
    public:
        void save(int fieldID, bool isPlayer);
        char getState(int fieldID) const;
        bool isWin(bool isPlayer) const;
        bool isFull() const;
        const int COMBINATIONS[8][3] = {
                {0,1,2},
                {3,4,5},
                {6,7,8},
                {0,3,6},
                {1,4,7},
                {2,5,8},
                {0,4,8},
                {2,4,6},
        };
    private:
        char board[9] = {' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '};
    };
}

