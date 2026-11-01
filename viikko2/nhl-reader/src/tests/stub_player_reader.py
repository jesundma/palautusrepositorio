"""Stub PlayerReader for unit tests; serves fixed players without HTTP."""

from player import Player


class StubPlayerReader:  # pylint: disable=too-few-public-methods
    """Drop-in replacement for PlayerReader returning hard-coded players."""

    def all_players(self) -> list[Player]:
        """Return a fixed list of players."""
        return [
            Player({"name": "Semenko", "nationality": "CAN", "assists": 4,
                    "goals": 12, "team": "EDM", "games": 50}),
            Player({"name": "Lemieux", "nationality": "CAN", "assists": 45,
                    "goals": 54, "team": "PIT", "games": 60}),
            Player({"name": "Kurri", "nationality": "FIN", "assists": 37,
                    "goals": 43, "team": "EDM", "games": 70}),
            Player({"name": "Yzerman", "nationality": "CAN", "assists": 42,
                    "goals": 35, "team": "DET", "games": 75}),
            Player({"name": "Gretzky", "nationality": "CAN", "assists": 89,
                    "goals": 35, "team": "EDM", "games": 80}),
        ]
