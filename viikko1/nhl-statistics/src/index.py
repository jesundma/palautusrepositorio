import argparse

from player_reader import PlayerReader
from statistics_service import StatisticsService


def main(url):
    reader = PlayerReader(url)
    stats = StatisticsService(reader)
    philadelphia_flyers_players = stats.team("PHI")
    top_scorers = stats.top(10)

    print("Philadelphia Flyers:")
    for player in philadelphia_flyers_players:
        print(player)

    print()  

    print("Top point getters:")
    for player in top_scorers:
        print(player)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="URL of the player data file")
    args = parser.parse_args()
    main(args.url)
