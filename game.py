# from models import Player, Enemy
#
# #
# # def get_int():
# #     while True:
# #         try:
# #             num = int(input("Choose: sorcerer (1), robber(2), warrior(3): "))
# #             if num < 1 or num > 3:
# #                 print("Please, enter a number 1 - 3.")
# #                 continue
# #             else:
# #                 return num
# #         except ValueError:
# #             print("It isn't a number. Please, try again.")
#
#
# if __name__ == "__main__":
#     player = input("Please enter your name: ")
#     game_status = input(f"Hello {player}. Please enter 'START' to start the game: ")
#
#     if game_status == "start".lower().strip(" "):
#         player = Player(player)
#         enemy_level = 1
#         while True:
#             player_choice = get_int()
#             enemy = Enemy(enemy_level)
#             player.attack(player_choice, enemy)


from models import Player, Enemy
from game_exceptions import EnemyDown, GameOver

if __name__ == '__main__':
    player_name = input("Please enter your name: ")
    player = Player(player_name)
    enemy_level = 1
    enemy = Enemy(enemy_level)
    while True:
        try:
            player.attack(enemy)
        except EnemyDown:
            enemy_level += 1
            player.score += 5
            print(f"Your lives: {player.lives}\nYour score: {player.score}")
            print("You have a new enemy. Good luck!")
            enemy = Enemy(enemy_level)
        except GameOver:
            print("You've lost.\nGame over!")
            player_score_str = f"{player_name}: {player.score}"
            with open("scores.txt", "a") as file_score:
                file_score.write(f"{player_name}: {player.score}\n")
                break
    top_10_request = input("\nDo you want to print TOP 10 players? (yes/no): ")
    if top_10_request == "yes".strip(""):
        with open("scores.txt", "r") as top:
            players_list = []
            lines = top.readlines()
            player_list = []
            for line in lines:
                player_list = line.strip("\n").split(": ")
                player_list[1] = int(player_list[1])
                players_list.append(player_list)
            top_list = sorted(players_list, key=lambda x: x[1], reverse=True)
            for player in top_list[:10]:
                player[1] = str(player[1])
                print(": ".join(player))
    else:
        print("Goodbye.")













