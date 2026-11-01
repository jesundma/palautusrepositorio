"""Command-line entry point for browsing NHL player statistics."""

from rich import print as rprint
from rich.prompt import Prompt

from player_reader import PlayerReader
from player_stats import PlayerStats
from console_view import print_players
from enums import Nationality, Season


def ask_season() -> Season:
    """Prompt until a valid season is entered."""
    valid = ", ".join(season.value for season in Season)
    while True:
        answer = Prompt.ask(f"Enter the season (valid seasons: [blue]{valid}[/blue])")
        try:
            return Season(answer)
        except ValueError:
            rprint(f"Invalid season. Choose one of: [blue]{valid}[/blue]")


def ask_nationality() -> Nationality | None:
    """Prompt until a valid nationality is entered; return None to exit."""
    valid = ", ".join(nationality.value for nationality in Nationality)
    while True:
        answer = Prompt.ask(
            f"Enter the nationality (valid nationalities: [blue]{valid}[/blue], "
            "X to exit)"
        ).upper()
        if answer == "X":
            return None
        try:
            return Nationality[answer]
        except KeyError:
            rprint(f"Invalid nationality. Choose one of: [blue]{valid}[/blue]")


def show_players(stats: PlayerStats, season: Season, nationality: Nationality) -> None:
    """Print the top scorers for the given nationality."""
    players = stats.top_scorers_by_nationality(nationality.value)
    rprint(f"[bold]Season {season.value} players for {nationality.value}[/bold]")
    if players:
        print_players(players)
    else:
        rprint("No players")


def main():
    """Prompt for a season and a nationality and print the top scorers."""
    season = ask_season()
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season.api_value}/players"
    stats = PlayerStats(PlayerReader(url))

    while (nationality := ask_nationality()) is not None:
        show_players(stats, season, nationality)


if __name__ == "__main__":
    main()
