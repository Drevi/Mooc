# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        if len(player1_word) < len(player2_word):
            return 2        

        
class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def vowel_counter(self, word):
        vowels = 0
        for char in word:
            if char.lower() in "aeiou":
                vowels += 1
        return vowels

    def round_winner(self, player1_word: str, player2_word: str):
        if self.vowel_counter(player1_word) > self.vowel_counter(player2_word):
            return 1
        if self.vowel_counter(player1_word) < self.vowel_counter(player2_word):
            return 2


class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def is_valid(self, word):
        return word in ["rock","paper", "scissors"]


    def round_winner(self, player1_word: str, player2_word: str):
        if not self.is_valid(player1_word) and not self.is_valid(player2_word) or player1_word == player2_word:
            return
        if self.is_valid(player1_word) and not self.is_valid(player2_word):
            return 1
        if not self.is_valid(player1_word) and self.is_valid(player2_word):
            return 2
        if player1_word == "rock":
            if player2_word == "paper":
                return 2
            else:
                return 1
        if player1_word == "paper":
            if player2_word == "scissors":
                return 2
            else:
                return 1
        if player1_word == "scissors":
            if player2_word == "rock":
                return 2
            else:
                return 1


    
        

