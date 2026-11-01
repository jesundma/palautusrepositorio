"""Statistics calculations for NHL players."""

from player import Player
from player_reader import PlayerReader


class PlayerStats:
    """Rankings computed from the players returned by a PlayerReader."""

    def __init__(self, reader: PlayerReader):
        self._players = reader.all_players()

    def top_scorers_by_nationality(self, nationality: str) -> list[Player]:
        """Return players of the given nationality, ordered by points (goals + assists)."""
        players = [p for p in self._players if p.nationality == nationality]
        return sorted(players, key=lambda p: p.goals + p.assists, reverse=True)

    def top_scorers_by_team(self, team: str) -> list[Player]:
        """Return players of the given team (e.g. "EDM"), ordered by points (goals + assists)."""
        players = [p for p in self._players if p.team == team]
        return sorted(players, key=lambda p: p.goals + p.assists, reverse=True)

    def top_goal_scorers(self, how_many: int) -> list[Player]:
        """Return the how_many players with the most goals, in descending order."""
        return sorted(self._players, key=lambda p: p.goals, reverse=True)[:how_many]
