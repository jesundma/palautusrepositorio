from player_reader import PlayerReader
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class StatisticsService:
    def __init__(self, player_reader):
        self._players = player_reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort_order: SortBy = SortBy.POINTS):
        # metodin käyttämä apufufunktio voidaan määritellä näin
        def how_to_sort(player):
            if sort_order == SortBy.GOALS:
                return player.goals
            elif sort_order == SortBy.ASSISTS:
                return player.assists

            return player.points

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=how_to_sort
        )

        result = []
        i = 0
        while i < how_many:     # should check whether the original code had <= or it is a typo while writing my code
            result.append(sorted_players[i])
            i += 1

        return result
