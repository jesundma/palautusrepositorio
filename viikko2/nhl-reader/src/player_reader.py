"""Fetches player data from the NHL stats API."""

import requests

from player import Player


class PlayerReader:  # pylint: disable=too-few-public-methods
    """Reads players from a given URL."""

    def __init__(self, url: str):
        self._url = url

    def all_players(self) -> list[Player]:
        """Download and return all players as Player objects."""
        response = requests.get(self._url, timeout=10)
        response.raise_for_status()
        player_data = response.json()
        if not isinstance(player_data, list):
            raise ValueError("Expected the NHL stats API to return a list of players")
        return [Player(player_dict) for player_dict in player_data]
