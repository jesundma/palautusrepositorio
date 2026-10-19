import requests

from Player import _Player


class PlayerReader:
    def __init__(self, url: str):
        self._url = url

    def all_players(self) -> list[_Player]:
        response = requests.get(self._url)
        response.raise_for_status()
        player_data = response.json()
        if not isinstance(player_data, list):
            raise ValueError("Expected the NHL stats API to return a list of players")
        return [_Player(player_dict) for player_dict in player_data]