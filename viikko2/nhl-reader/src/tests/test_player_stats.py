"""Unit tests for PlayerStats using a stub reader (no HTTP)."""

import unittest

from player_stats import PlayerStats
from tests.stub_player_reader import StubPlayerReader


class TestPlayerStats(unittest.TestCase):
    """Tests for PlayerStats."""

    def setUp(self):
        self.stats = PlayerStats(StubPlayerReader())

    def test_top_scorers_by_team_sorted_by_points(self):
        names = [p.name for p in self.stats.top_scorers_by_team("EDM")]
        self.assertEqual(names, ["Gretzky", "Kurri", "Semenko"])

    def test_top_scorers_by_team_unknown_team(self):
        self.assertEqual(self.stats.top_scorers_by_team("XXX"), [])

    def test_top_scorers_by_nationality_sorted_by_points(self):
        names = [p.name for p in self.stats.top_scorers_by_nationality("CAN")]
        self.assertEqual(names, ["Gretzky", "Lemieux", "Yzerman", "Semenko"])

    def test_top_scorers_by_nationality_only_matching_players(self):
        players = self.stats.top_scorers_by_nationality("FIN")
        self.assertEqual([p.name for p in players], ["Kurri"])

    def test_top_scorers_by_nationality_unknown_nationality(self):
        self.assertEqual(self.stats.top_scorers_by_nationality("XXX"), [])

    def test_top_goal_scorers_sorted_by_goals(self):
        names = [p.name for p in self.stats.top_goal_scorers(3)]
        self.assertEqual(names, ["Lemieux", "Kurri", "Yzerman"])

    def test_top_goal_scorers_more_than_available(self):
        self.assertEqual(len(self.stats.top_goal_scorers(100)), 5)

    def test_top_goal_scorers_zero(self):
        self.assertEqual(self.stats.top_goal_scorers(0), [])
