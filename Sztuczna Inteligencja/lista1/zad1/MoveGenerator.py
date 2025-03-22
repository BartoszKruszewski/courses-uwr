from FigureEnum import FigureEnum
from Field import Field
from typing import List, Set
from GameState import GameState
from Move import Move
from Config import Config


class MoveGenerator:
    def moves(self, game_state: GameState) -> List[Move]:
        moves = []

        king_field = game_state.white_king if game_state.turn else game_state.black_king
        enemy_king_field = game_state.white_king if game_state.turn else game_state.black_king

        actual_surrounding = set(king_field.shift(shift) for shift in Config.SURROUNDING)
        enemy_king_surrounding = set(enemy_king_field.shift(shift) for shift in Config.SURROUNDING)
        moves.extend(
            Move(FigureEnum.KING, field)
            for field in list(actual_surrounding - enemy_king_surrounding)
            if field.in_board()
        )

        if game_state.turn:
            rook_fields = (Fieldgame_state.white_rook for x in range())
            moves.extend(game_state.white_rook)

    def _king_moves(self, actual_field: Field, enemy_king_field: Field) -> List[Move]:
        
    
    def _rook_moves(self, actual_field: Field) -> List[Move]:
        return Field