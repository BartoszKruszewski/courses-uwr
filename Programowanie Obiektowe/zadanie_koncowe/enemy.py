"""Moduł zawierający klasę węża przeciwnika "Enemy", która dziedziczy po
klasie abstrakcyjnej węża "Snake".
"""

import pygame

from snake import Snake
from food import Food
from const import AI_UPDATE_TIME, AI_SPEED_UP_DISTANCE,\
    AI_ATTACK_FOCUS_DISTANCE, AI_SAFETY_DISTANCE


class Enemy(Snake):
    """Klasa węża przeciwnika, dziedzicząca z klasy Snake.

    Ustawianie celu poruszania się węże, na podstawie położenia innych węży
    i jedzenia.

    Attributes:
        __ai_update_timer (float): Licznik czasu odświeżenia AI.
    """

    def __init__(self):
        """Resetowanie licznika czasu pozostałego do odświeżenia AI.
        """

        # wywołanie konstruktora klasy Snake
        super().__init__()

        # utworzenie zegara odliczającego czas do odświeżenia AI
        self.__ai_update_timer = AI_UPDATE_TIME

    def __get_best_food_pos(
            self, food_list: list[Food], enemies_list: list[Snake]) \
            -> pygame.Vector2:
        """Wybieranie optymalnej pozycji jedzenia, do którego będzie się
        kierował wąż.

        Args:
            food_list: Lista obiektów jedzenia.
            enemies_list: Lista obiektów pozostałych węży.
        Returns:
            Optymalna pozycja jedzenia. Jeżeli nie da się wybrać żadnej
            pozycji jedzenia, to zwracana jest aktualna pozycja celu.
        """

        # utworzenie posortowanej listy pozycji najbliższego jedzenia
        sorted_food_pos = map(
            lambda x: x.pos, sorted(
                food_list, key = lambda x: self.body[0].distance_to(x.pos)))

        for food_pos in sorted_food_pos:
            # obliczanie dystansu do jedzenia
            distance = food_pos.distance_to(self.body[0])

            # sprawdzanie, czy jakikolwiek przeciwnik jest bliżej
            # wybranego jedzenia
            for enemy in enemies_list:
                if food_pos.distance_to(enemy.body[0]) > distance:
                    return food_pos

        # jeżeli nie ma odpowiedniego jedzenia to nie zmieniaj
        # dotychczasowego celu
        return self.dest

    def __get_nearest_enemy(self, enemies_list: list[Snake]) -> Snake:
        """Wybieranie pozycji najbliższego przeciwnika.

        Args:
            enemies_list: Lista obiektów pozostałych węży.
        Returns:
            Pozycja głowy najbliższego przeciwnika.
        """

        return min(
            enemies_list, key = lambda x: self.body[0].distance_to(x.body[0]))

    def __is_possible_collision(
            self, enemy: Snake, dest: pygame.Vector2, dt: float) -> bool:
        """Sprawdzanie, czy dla podanego celu poruszania się, nastąpi kolizja
         z przeciwnikiem.

        Args:
            enemy: Obiekt przeciwnika, dla którego sprawdzana jest kolizja.
            dest: Sprawdzany cel poruszania się.
            dt: Mnożnik zmieniający wartości względem wydajności gry.
        Returns:
            Prawda, jeżeli istnieje ryzyko kolizja, fałsz w przeciwny przypadku.
        """
        # wyznaczanie przyszłej pozycji głowy
        future_head_pos = self.body[0].move_towards(dest, self.speed * dt)

        # sprawdzanie, czy nastąpi kolizja z ciałem przeciwnika (nie licząc
        # głowy)
        for body in enemy.body[1:]:
            if future_head_pos.distance_to(body) < AI_SAFETY_DISTANCE:
                return True
        return False

    def __choose_dest(
            self, food_list: list[Food], enemies_list: list[Snake], dt: float) \
            -> pygame.Vector2:
        """Wybieranie kierunku poruszania na podstawie pozycji jedzenia i
        pozycji przeciwników.

        Args:
            food_list: Lista obiektów jedzenia
            enemies_list: Lista obiektów pozostałych węży.
            dt: Mnożnik zmieniający wartości względem wydajności gry.
        Returns:
            Optymalna pozycja celu poruszania się.
        """

        # znajdowanie najbliższego przeciwnika
        nearest_enemy = self.__get_nearest_enemy(enemies_list)

        # jeżeli przeciwnik jest odpowiednio blisko oraz przemieszcza się w
        # stronę węża to zaatakuj go
        if self.body[0].distance_to(nearest_enemy.body[0]) <\
                self.body[0].distance_to(nearest_enemy.body[-1]) <\
                AI_ATTACK_FOCUS_DISTANCE:
            # wyznaczanie pozycji do ataku
            attack_pos = nearest_enemy.body[0].copy()

            # jeżeli jest możliwe ustalenie kierunku poruszania przeciwnika,
            # to przesuń pozycję do ataku przed jego głowę
            if nearest_enemy.body[0] != nearest_enemy.body[1]:
                attack_pos +=\
                    (nearest_enemy.body[0] - nearest_enemy.body[1]).normalize()\
                    * (nearest_enemy.body_size + AI_SAFETY_DISTANCE)

            # sprawdzanie, czy nie ma ryzyka kolizji z przeciwnikiem
            if not self.__is_possible_collision(nearest_enemy, attack_pos, dt):
                return attack_pos
            else:
                # jeżeli jest to zawróć w przeciwną stronę
                if self.body[0] - self.body[1] != pygame.Vector2(0, 0):
                    return self.body[0] -\
                        (self.body[0] - self.body[1]).normalize()\
                        * len(self.body) * self.body_size
                else:
                    return self.body[0].copy()
        else:
            # wyznaczanie pozycji jedzenia, do którego wąż ma mniejszy
            # dystans niż pozostałe węże
            return self.__get_best_food_pos(food_list, enemies_list)

    def update(
            self, food_list: list[Food], enemies_list: list[Snake], dt: float):
        """Odświeżanie AI i wybieranie pozycji celu poruszania się węża.

        Args:
            food_list: Lista obiektów jedzenia.
            enemies_list: Lista obiektów węży.
            dt: Mnożnik zmieniający wartości względem wydajności gry.
        """

        # aktualizowanie zegara odliczającego czas do odświeżenia AI
        self.__ai_update_timer -= dt

        if self.__ai_update_timer <= 0:
            # resetowanie zegara
            self.__ai_update_timer = AI_UPDATE_TIME

            # odświeżenie AI
            self.dest = self.__choose_dest(food_list, enemies_list, dt)
            self.is_speeding = self.body[0].distance_to(self.dest) <\
                AI_SPEED_UP_DISTANCE

        # wywołanie funkcji aktualizującej z klasy bazowej
        self.update_snake(dt)
