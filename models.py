from settings import lives, LIST_CHOICE, BATTLE_LIST
import random
from game_exceptions import EnemyDown, GameOver


class Enemy:
    lives: int
    level: int
    enemy_choice: list

    def __init__(self, level: int):
        """

        :param level:
        :return:
        """
        self.level = level
        self.lives = level

    # @staticmethod
    def select_attack(self):
        self.enemy_choice = random.choice(LIST_CHOICE)
        return self.enemy_choice

    def decrease_lives(self):
        self.lives -= 1
        if not self.lives:
            raise EnemyDown


class Player:
    name: str
    lives: int = lives
    score: int = 0
    battle: list
    player_choice: list

    def __init__(self, name: str):
        """

        :param name:
        """
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

    def fight(self, player_choice, enemy_choice):
        self.battle = [player_choice, enemy_choice]
        if enemy_choice == player_choice:
            return 0
        else:
            if self.battle in BATTLE_LIST:
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


