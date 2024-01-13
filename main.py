# import random
#
# player = input("Please enter your name: ")
# game_status = input(f"Hello {player}. Please enter 'START' to start the game: ").lower().strip(" ")
# print(f"Hello {player}.The game is starting. Good luck!!!")
#
#
# class Choice:
#     def __init__(self, name: str):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#     def __repr__(self):
#
#         return self.name
#
#
# sorcerer = Choice("sorcerer")
# robber = Choice("robber")
# warrior = Choice("warrior")
# LIST_CHOICE = [sorcerer, robber, warrior]
# BATTLE_LIST = [[sorcerer, robber], [robber, warrior], [warrior, sorcerer]]
#
#
# def gamer_attack():
#     gamer_choice = get_int()
#     enemy_choice = random.choice(LIST_CHOICE)
#     # enemy = Enemy(5)
#     # enemy_choice = enemy.select_attack()
#
#     match gamer_choice:
#         case 1:
#             gamer_choice = sorcerer
#         case 2:
#             gamer_choice = robber
#         case 3:
#             gamer_choice = warrior
#     print(f"Your choice is {gamer_choice}.")
#     print(f"My choice is {enemy_choice}.")
#     attack = [gamer_choice, enemy_choice]
#     if enemy_choice == gamer_choice:
#         res = "It's draw."
#     else:
#         if attack in BATTLE_LIST:
#             res = "Success"
#         else:
#             res = "Failed"
#     print(res)
#     return res
#
#
# def gamer_protection():
#     enemy_choice = random.choice(LIST_CHOICE)
#     print("I've done my choice. Your turn.")
#     gamer_choice = get_int()
#     match gamer_choice:
#         case 1:
#             gamer_choice = sorcerer
#         case 2:
#             gamer_choice = robber
#         case 3:
#             gamer_choice = warrior
#     print(f"Your choice is {gamer_choice}.")
#     print(f"My choice is {enemy_choice}.")
#     protection = [gamer_choice, enemy_choice]
#     if enemy_choice == gamer_choice:
#         res = "It's draw."
#     else:
#         if protection in BATTLE_LIST:
#             res = "Success"
#         else:
#             res = "Failed"
#     print(res)
#     return res
#
#
# def get_int():
#     while True:
#         try:
#             num = int(input("Choose: sorcerer (1), robber(2), warrior(3): "))
#             if num < 1 or num > 3:
#                 print("Please, enter a number 1 - 3.")
#                 continue
#             else:
#                 return num
#         except ValueError:
#             print("It isn't a number. Please, try again.")
#
#
# if game_status == "start":
#     gamer_lives = 5
#
#     score = 0
#     while gamer_lives > 0:
#         enemy_lives = 5
#         while enemy_lives > 0 and gamer_lives > 0:
#             res_attack = gamer_attack()
#             res_protection = gamer_protection()
#             if res_attack == "Success":
#                 enemy_lives -= 1
#                 score += 1
#             if res_protection == "Failed":
#                 gamer_lives -= 1
#             print(f"Enemy lives = {enemy_lives}.")
#             print(f"Your lives = {gamer_lives}.")
#             print(f"Your score is {score}.")
#         if not enemy_lives:
#             print(f"You won. Your score is {score}.")
#             print("You have a new enemy. Good luck.")
#         if not gamer_lives:
#             break
#         score += 5
#         enemy_lives = 5
# print("You've lost.\nGame over.")
from models import Player, Enemy


def get_int():
    while True:
        try:
            num = int(input("Choose: sorcerer (1), robber(2), warrior(3): "))
            if num < 1 or num > 3:
                print("Please, enter a number 1 - 3.")
                continue
            else:
                return num
        except ValueError:
            print("It isn't a number. Please, try again.")


if __name__ == "__main__":
    player = input("Please enter your name: ")
    game_status = input(f"Hello {player}. Please enter 'START' to start the game: ")

    if game_status == "start".lower().strip(" "):
        player = Player(player)
        enemy_level = 1
        while True:
            player_choice = get_int()
            enemy = Enemy(enemy_level)
            player.attack(player_choice, enemy)
