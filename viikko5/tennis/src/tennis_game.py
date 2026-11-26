WINNING_SCORE = 4
ADVANTAGE = 1
WINNING_MARGIN = 2


class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.game_is_tied()

        if self.m_score1 >= WINNING_SCORE or self.m_score2 >= WINNING_SCORE:
            return self.game_is_advantage_or_win()

        return self.match_score(self.m_score1, self.m_score2)

    def match_score(self, m_score1, m_score2):
        match_points = ["Love", "Fifteen", "Thirty", "Forty"]
        return match_points[m_score1] + "-" + match_points[m_score2]

    def game_is_tied(self):
        ties = ["Love-All", "Fifteen-All", "Thirty-All"]

        if self.m_score1 < len(ties):
            return ties[self.m_score1]
        return "Deuce"

    def game_is_advantage_or_win(self):
        minus_result = self.m_score1 - self.m_score2

        if minus_result == ADVANTAGE:
            return "Advantage player1"
        if minus_result == -ADVANTAGE:
            return "Advantage player2"
        if minus_result >= WINNING_MARGIN:
            return "Win for player1"
        return "Win for player2"
