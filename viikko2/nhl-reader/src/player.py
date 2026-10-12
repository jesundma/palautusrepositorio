class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assist = dict['assists']
        self.goals = dict['goals']
        self.team = dict['team']
        self.games = dict['games']
        self.id = dict['id']
    
    def __str__(self):
        return f"{self.name}, {self.assist}, {self.goals}, {self.team}, {self.games}"

#{"name":"Jordan Harris","nationality":"USA","assists":4,"goals":1,"team":"CBJ","games":33,"id":8480887}