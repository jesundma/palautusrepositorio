"""Player data model."""


class Player:  # pylint: disable=too-few-public-methods
    """A single NHL player's season statistics."""

    def __init__(self, player_data: dict):
        self.name = player_data['name']
        self.nationality = player_data['nationality']
        self.assists = player_data['assists']
        self.goals = player_data['goals']
        self.team = player_data['team']
        self.games = player_data['games']
        self.id = player_data.get('id')

    def __str__(self):
        total = self.assists + self.goals
        return f"{self.name:20} {self.team} {self.assists} + {self.goals} = {total}"
