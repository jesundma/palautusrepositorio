from PlayerReader import PlayerReader
from PlayerStats import PlayerStats
from enums import Nationality, Season
from rich import print
from rich.prompt import Prompt


def main():
    valid_seasons = ", ".join(season.value for season in Season)
    valid_nationalities = ", ".join(nationality.value for nationality in Nationality)

    while True:
        season = Prompt.ask(
            f"Enter the season (valid seasons: [blue]{valid_seasons}[/blue], X to exit)"
        )
        if season.upper() == "X":
            return

        try:
            selected_season = Season(season)
        except ValueError:
            print(f"Invalid season. Choose one of: [blue]{valid_seasons}[/blue]")
            continue

        nationality = Prompt.ask(
            f"Enter the nationality (valid nationalities: [blue]{valid_nationalities}[/blue])"
        ).upper()
        try:
            selected_nationality = Nationality[nationality]
        except KeyError:
            print(f"Invalid nationality. Choose one of: [blue]{valid_nationalities}[/blue]")
            continue

        url = f"https://studies.cs.helsinki.fi/nhlstats/{selected_season.api_value}/players"
        reader = PlayerReader(url)
        stats = PlayerStats(reader)
        players = stats.top_scorers_by_nationality(selected_nationality.value)

        print(f"[bold]Season {selected_season.value} players for {selected_nationality.value}[/bold]")
        if not players:
            print("No players")
        else:
            for player in players:
                print(player)


if __name__ == "__main__":
    main()