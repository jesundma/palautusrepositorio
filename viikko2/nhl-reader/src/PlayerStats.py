from Player import _Player
from PlayerReader import PlayerReader


class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self._players = reader.all_players()

    def top_scorers_by_nationality(self, nationality: str) -> list[_Player]:
        players_by_nationality = [player for player in self._players if player.nationality == nationality]
        return sorted(players_by_nationality, key=lambda player: player.goals + player.assists, reverse=True)