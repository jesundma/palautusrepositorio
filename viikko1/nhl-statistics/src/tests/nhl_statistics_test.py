import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_player_reader_stub_returns_five_players_in_expected_order(self):
        players = PlayerReaderStub().get_players()

        self.assertEqual(len(players), 5)
        self.assertEqual(
            [player.name for player in players],
            ["Semenko", "Lemieux", "Kurri", "Yzerman", "Gretzky"]
        )

    def test_statistics_service_returns_a_correct_player_and_statitistics_with_search(self):
        player = self.stats.search("Kurri")

        self.assertIsNotNone(player)
        self.assertEqual(
            (player.name, player.team, player.goals, player.assists),
            ("Kurri", "EDM", 37, 53)
        )

    def test_statistics_service_returns_none_for_nonexistent_player(self):
        player = self.stats.search("NotAPlayer")

        self.assertIsNone(player)

    def test_statistics_service_returns_correct_players_for_team(self):
        players = self.stats.team("EDM")

        self.assertEqual(
            [player.name for player in players],
            ["Semenko", "Kurri", "Gretzky"]
        )

    def test_statistics_service_returns_correct_order_of_players_by_points_for_3_players_without_2_param(self):
        from statistics_service import SortBy
        players = self.stats.top(3)

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Yzerman"]
        )

    def test_statistics_service_returns_correct_order_of_players_by_points_for_3_players_with_2_param(self):
            from statistics_service import SortBy
            players = self.stats.top(3, sort_order=SortBy.POINTS)
    
            self.assertEqual(
                [player.name for player in players],
                ["Gretzky", "Lemieux", "Yzerman"]
            )

    def test_statistics_service_returns_correct_order_of_players_by_assists_for_3_players(self):
        from statistics_service import SortBy
        players = self.stats.top(3, sort_order=SortBy.ASSISTS)

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Yzerman", "Lemieux"]

        )
    def test_statistics_service_returns_correct_order_of_players_by_goals_for_3_players(self):
        from statistics_service import SortBy
        players = self.stats.top(3, sort_order=SortBy.GOALS)

        self.assertEqual(
            [player.name for player in players],
            ["Lemieux", "Yzerman", "Kurri"]            
        )