from unittest import TestCase
from unittest.mock import patch
from models import Enemy, Player
from game_exceptions import EnemyDown, IncorrectName, GameOver
from settings import LIVES
from game import main


class TestEnemyInit(TestCase):
    def test_init_correct(self):
        enemy = Enemy(5)
        self.assertEqual(enemy.level, 5)
        self.assertEqual(enemy.lives, 5)

    def test_init_incorrect(self):
        with self.assertRaises(TypeError):
            Enemy("hello")

    def test_init_incorrect_negative(self):
        with self.assertRaises(ValueError):
            Enemy(-1)

    def test_init_incorrect_zero(self):
        with self.assertRaises(ValueError):
            Enemy(0)


class TestEnemyDecreaseLives(TestCase):
    def test_decrease_lives_correct(self):
        enemy = Enemy(5)
        enemy.decrease_lives()
        self.assertEqual(enemy.lives, 4)

    def test_decrease_lives_dead(self):
        enemy = Enemy(2)
        enemy.decrease_lives()
        with self.assertRaises(EnemyDown):
            enemy.decrease_lives()


class TestPlayerInit(TestCase):
    @patch("builtins.input")
    def test_input_name_correct(self, mock_input):
        mock_input.return_value = "Jan"
        player = Player(mock_input.return_value)
        self.assertEqual(player.name, "Jan")

    @patch("builtins.input")
    def test_input_name_incorrect(self, mock_input):
        mock_input.return_value = ""
        with self.assertRaises(IncorrectName):
            Player(mock_input.return_value)


class TestPlayerGetInt(TestCase):
    def setUp(self):
        self.player = Player("Jan")

    @patch("builtins.input")
    def test_get_int_correct(self, mock_input):
        mock_input.return_value = 1
        self.assertEqual(self.player.get_int(), 1)

    @patch("builtins.input")
    def test_get_int_incorrect(self, mock_input):
        mock_input.side_effect = ["4"]
        with self.assertRaises(StopIteration):
            self.player.get_int()

    @patch("builtins.input")
    def test_get_int_not_num(self, mock_input):
        mock_input.side_effect = "a"
        with self.assertRaises(StopIteration):
            self.player.get_int()


class TestPlayerFight(TestCase):

    def setUp(self):
        self.player = Player("Jan")

    def test_fight_draw_stone(self):
        self.assertEqual(self.player.fight("stone", "stone"), 0)

    def test_fight_player_winner_stone_scissors(self):
        self.assertEqual(self.player.fight("stone", "scissors"), 1)

    def test_fight_player_missed_scissors_stone(self):
        self.assertEqual(self.player.fight("scissors", "stone"), -1)

    def test_fight_draw_scissors(self):
        res = self.player.fight("scissors", "scissors")
        self.assertEqual(res, 0)

    def test_fight_player_winner_scissors_paper(self):
        self.assertEqual(self.player.fight("scissors", "paper"), 1)

    def test_fight_player_missed_paper_scissors(self):
        self.assertEqual(self.player.fight("paper", "scissors"), -1)

    def test_fight_draw_paper(self):
        res = self.player.fight("paper", "paper")
        self.assertEqual(res, 0)

    def test_fight_player_winner_paper_stone(self):
        self.assertEqual(self.player.fight("paper", "stone"), 1)

    def test_fight_player_missed_stone_paper(self):
        self.assertEqual(self.player.fight("stone", "paper"), -1)

    def test_fight_player_choice_incorrect(self):
        with self.assertRaises(ValueError):
            self.player.fight("gdsdf", "stone")

    def test_fight_enemy_choice_incorrect(self):
        with self.assertRaises(ValueError):
            self.player.fight("stone", "gdsdf")

    def test_fight_both_choice_incorrect(self):
        with self.assertRaises(ValueError):
            self.player.fight("asdf", "gdsdf")


class TestPlayerDecreaseLives(TestCase):

    def setUp(self):
        self.player = Player("Jan")
        self.player.lives = 3

    def test_decrease_lives_correct(self):
        self.player.decrease_lives()
        self.assertEqual(self.player.lives, 2)

    def test_decrease_lives_dead(self):
        self.player.decrease_lives()
        self.player.decrease_lives()
        with self.assertRaises(GameOver):
            self.player.decrease_lives()


class TestPlayerAttack(TestCase):

    def setUp(self):
        self.player = Player("Jan")
        self.enemy = Enemy(3)

    @patch('models.Player.get_int')
    @patch('models.Enemy.select_attack')
    def test_attack_correct_draw(self, mock_select_attack, mock_get_int):
        mock_select_attack.return_value = "stone"
        mock_get_int.return_value = 1
        self.player.attack(self.enemy)
        self.assertEqual(self.enemy.lives, 3)
        self.assertEqual(self.player.lives, LIVES)

    @patch("models.Player.get_int")
    @patch("models.Enemy.select_attack")
    def test_attack_correct_success(self, mock_select_attack, mock_get_int):
        mock_select_attack.return_value = "scissors"
        mock_get_int.return_value = 1
        self.player.attack(self.enemy)
        self.assertEqual(self.enemy.lives, 2)
        self.assertEqual(self.player.lives, LIVES)
        self.assertEqual(self.player.score, 1)

    @patch("models.Player.get_int")
    @patch("models.Enemy.select_attack")
    def test_attack_correct_missed(self, mock_select_attack, mock_get_int):
        mock_select_attack.return_value = "stone"
        mock_get_int.return_value = 2
        self.player.attack(self.enemy)
        self.assertEqual(self.enemy.lives, 3)
        self.assertEqual(self.player.lives, LIVES - 1)


class TestMain(TestCase):

    def setUp(self):

        self.enemy = Enemy(1)

    @patch("builtins.input")
    @patch("models.Player.get_int")
    @patch("models.Enemy.select_attack")
    def test_main_enemy_down(self, mock_input, mock_get_int, mock_select_attack):
        mock_input.return_value = "Jan"
        self.player = Player(mock_input.return_value)
        mock_get_int.return_value = 1
        mock_select_attack.return_value = "scissors"
        main()
        self.assertEqual(self.enemy.level, 1)
        self.assertEqual(self.player.score, 0)


