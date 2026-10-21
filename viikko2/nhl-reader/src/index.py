from PlayerReader import PlayerReader
from PlayerStats import PlayerStats
from console_view import print_players
from enums import Nationality, Season
from rich import print
from rich.prompt import Prompt


def main():
    valid_seasons = ", ".join(season.value for season in Season)
    valid_nationalities = ", ".join(nationality.value for nationality in Nationality)

    while True:
        season = Prompt.ask(f"Enter the season (valid seasons: [blue]{valid_seasons}[/blue])")
        try:
            selected_season = Season(season)
            break
        except ValueError:
            print(f"Invalid season. Choose one of: [blue]{valid_seasons}[/blue]")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{selected_season.api_value}/players"
    stats = PlayerStats(PlayerReader(url))

    while True:
        nationality = Prompt.ask(
            f"Enter the nationality (valid nationalities: [blue]{valid_nationalities}[/blue], X to exit)"
        ).upper()
        if nationality == "X":
            return

        try:
            selected_nationality = Nationality[nationality]
        except KeyError:
            print(f"Invalid nationality. Choose one of: [blue]{valid_nationalities}[/blue]")
            continue

        players = stats.top_scorers_by_nationality(selected_nationality.value)

        print(f"[bold]Season {selected_season.value} players for {selected_nationality.value}[/bold]")
        if not players:
            print("No players")
        else:
            print_players(players)


if __name__ == "__main__":
    main()
