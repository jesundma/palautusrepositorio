import requests

from Player import _Player


class PlayerReader:
    def __init__(self, url: str):
        self._url = url

    def all_players(self) -> list[_Player]:
        response = requests.get(self._url).json()
        players = [_Player(player_dict) for player_dict in response]
        return players