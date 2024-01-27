from models import Player, Enemy
from game_exceptions import EnemyDown, GameOver, IncorrectName


def main():
    while True:
        try:
            player_name = input("Please enter your name: ")
            player = Player(player_name)
            break
        except IncorrectName:
            print("Incorrect name.")
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
            print(f"Your score: {player.score}")
            with open("scores.txt", "a") as file_score:
                file_score.write(f"{player_name}: {player.score}\n")
                break


def top_10():
    while True:
        top_10_request = input("\nDo you want to print TOP 10 players? (yes/no): ").strip("").lower()
        if top_10_request == "yes" or top_10_request == "no":
            break
        else:
            print("Incorrect value.")
            continue
    if top_10_request == "yes":
        with open("scores.txt", "r") as top:
            players_list = []
            lines = top.readlines()
            for line in lines:
                player_list = list(line.strip("\n").split(": "))
                player_list[1] = int(player_list[1])
                players_list.append(player_list)
            top_list = sorted(players_list, key=lambda x: x[1], reverse=True)
            for player in top_list[:10]:
                player[1] = str(player[1])
                print(": ".join(player))
    else:
        print("Goodbye.")


if __name__ == '__main__':
    main()
    top_10()

