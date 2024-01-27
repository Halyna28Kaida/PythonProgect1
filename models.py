from settings import LIVES, LIST_CHOICE, BATTLE_LIST
import random
from game_exceptions import EnemyDown, GameOver, IncorrectName


class Enemy:
    lives: int
    level: int
    enemy_choice: list

    def __init__(self, level: int):
        """

        :param level:
        :return:
        """
        if not isinstance(level, int):
            raise TypeError("It is not a number.")
        if not level:
            raise ValueError("Cannot be zero.")
        if level < 0:
            raise ValueError("Cannot be negative.")
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        return random.choice(LIST_CHOICE)

    def decrease_lives(self):
        self.lives -= 1
        if not self.lives:
            raise EnemyDown


class Player:
    name: str
    lives: int = LIVES
    score: int = 0

    def __init__(self, name: str):
        """

        :param name:
        """
        if not name:
            raise IncorrectName
        else:
            self.name = name

    @staticmethod
    def get_int():
        while True:
            try:
                num = int(input("Choose: stone (1), scissors(2), paper(3): "))
                if num < 1 or num > 3:
                    print("Please, enter a number 1 - 3.")
                    continue
                else:
                    return num
            except ValueError:
                print("It isn't a number. Please, try again.")

    @staticmethod
    def fight(player_choice: str, enemy_choice: str):
        if player_choice not in LIST_CHOICE:
            raise ValueError
        if enemy_choice not in LIST_CHOICE:
            raise ValueError
        if enemy_choice == player_choice:
            return 0
        if [player_choice, enemy_choice] in BATTLE_LIST:
            return 1
        else:
            return -1

    def decrease_lives(self):
        self.lives -= 1
        if not self.lives:
            raise GameOver

    def attack(self, enemy: Enemy):
        player_choice = self.get_int()
        match player_choice:
            case 1:
                player_choice = "stone"
            case 2:
                player_choice = "scissors"
            case 3:
                player_choice = "paper"
        enemy_choice = enemy.select_attack()
        res_attack = self.fight(player_choice, enemy_choice)
        print(f"Your choice: {player_choice}\nEnemy choice: {enemy_choice}")
        match res_attack:
            case 0:
                print("It's draw")
            case 1:
                print("You attacked successfully!")
                enemy.decrease_lives()
                self.score += 1
            case -1:
                self.decrease_lives()
                print("You missed")

        print(f"Your lives: {self.lives}\nEnemy lives: {enemy.lives}")

