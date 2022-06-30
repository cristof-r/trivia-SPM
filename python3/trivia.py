#!/usr/bin/env python3
from random import randrange
import enum

class Game:
    """

    Attributes:
        categories: List of available categories.
        place_category_mapping: Mapping from place to category.

    """
    
    categories = ["Pop", "Science", "Sports", "Rock"]

    place_category_mapping = {
        0: "Pop", 
        4: "Pop",
        8: "Pop",
        1: "Science",
        5: "Science",
        9: "Science",
        2: "Sports",
        6: "Sports",
        10: "Sports"
    }

    def __init__(self):
        self.players = []
        self.places = []
        self.purses = []
        self.in_penalty_box = []

        self.current_player = 0
        self.is_getting_out_of_penalty_box = False

        self.question_set = {category: [] for category in categories}
        for i in range(50):
            for key, value in self.question_set.items():
                value.append(self.create_question(key, i))

    def create_question(self, category: str, index: int) -> str:
        return f"{category} Question {index}"

    def is_playable(self) -> bool:
        return self.players_counter >= 2

    def add_player(self, player_name: str) -> None:
        self.players.append(player_name)
        self.places.append(0)
        self.purses.append(0)
        self.in_penalty_box.append(False)

        print(f"{player_name} was added")
        print(f"They are player number {self.players_counter}")

    @property
    def players_counter(self) -> int:
        return len(self.players)

    def roll(self, roll):
        print(f"{self.players[self.current_player]} is the current player")
        print(f"They have rolled a {roll}")

        if self.in_penalty_box[self.current_player]:
            if roll % 2 != 0:
                print(f"{self.players[self.current_player]} is getting out of the penalty box")
                self.is_getting_out_of_penalty_box = True
            else:
                print(f"{self.players[self.current_player]} is not getting out of the penalty box")
                self.is_getting_out_of_penalty_box = False

        self.places[self.current_player] += roll

        if self.places[self.current_player] > 11:
            self.places[self.current_player] -=  12

        print(f"{self.players[self.current_player]}'s new location is {str(self.places[self.current_player])}")
        print(f"The category is {self._current_category}")

        self._ask_question()

    def _ask_question(self):
        print(self.question_set[self._current_category].pop(0))

    @property
    def _current_category(self) -> str:
        current_place_player = self.places[self.current_player]

        if current_place_player in self.place_category_mapping:
            return self.place_category_mapping[current_place_player]
        else: 
            return "Rock"
            
    def was_correctly_answered(self):
        if self.in_penalty_box[self.current_player]:
            if not self.is_getting_out_of_penalty_box:
                self.current_player = (self.current_player + 1) % self.players_counter
                return True

        print("Answer was correct!!!!")
        self.purses[self.current_player] += 1
        print(f"{self.players[self.current_player]} now has {str(self.purses[self.current_player])} Gold coins")

        winner = self._did_player_win()
        self.current_player = (self.current_player + 1) % self.players_counter

        return winner

    def wrong_answer(self):
        print("Question was incorrectly answered")
        print(f"{self.players[self.current_player]} was sent to the penalty box")

        self.in_penalty_box[self.current_player] = True
        self.current_player = (self.current_player + 1) % self.players_counter

    def _did_player_win(self) -> bool:
        return self.purses[self.current_player] != 6


def main():
    game = Game()

    players = ["Chet", "Pat", "Sue"]
    for player in players:
        game.add_player(player)

    while True:
        game.roll(randrange(5) + 1)

        if randrange(9) == 7:
            game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()

            if not not_a_winner:
                break


if __name__ == "__main__":
    main()
