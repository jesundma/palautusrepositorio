from rich import print

from Player import _Player

HEADERS = ("Player", "Team", "Goals", "Assists", "Points")


def _pad_cells(values: tuple[str, ...], widths: list[int]) -> list[str]:
    return [
        f"{value:>{width}}" if i >= 2 else f"{value:<{width}}"
        for i, (value, width) in enumerate(zip(values, widths))
    ]


def _border(left: str, middle: str, right: str, widths: list[int]) -> str:
    return left + middle.join("─" * (width + 2) for width in widths) + right


def _box_row(cells: list[str]) -> str:
    return f"[white]│[/white] {' [white]│[/white] '.join(cells)} [white]│[/white]"


def print_players(players: list[_Player]) -> None:
    rows = [
        (
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.goals + player.assists),
        )
        for player in players
    ]

    widths = [len(header) for header in HEADERS]
    for row in rows:
        widths = [max(width, len(value)) for width, value in zip(widths, row)]

    print(f"[white]{_border('┌', '┬', '┐', widths)}[/white]")
    print(_box_row([f"[bold]{cell}[/bold]" for cell in _pad_cells(HEADERS, widths)]))
    print(f"[white]{_border('├', '┼', '┤', widths)}[/white]")
    for row in rows:
        cells = _pad_cells(row, widths)
        cells[0] = f"[green]{cells[0]}[/green]"
        cells[-1] = f"[green]{cells[-1]}[/green]"
        print(_box_row(cells))
    print(f"[white]{_border('└', '┴', '┘', widths)}[/white]")
