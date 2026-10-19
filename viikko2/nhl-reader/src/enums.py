from enum import Enum


class Season(Enum):
    SEASON_2018_2019 = "2018-19"
    SEASON_2019_2020 = "2019-20"
    SEASON_2020_2021 = "2020-21"
    SEASON_2021_2022 = "2021-22"
    SEASON_2022_2023 = "2022-23"
    SEASON_2023_2024 = "2023-24"
    SEASON_2024_2025 = "2024-25"

    @property
    def api_value(self) -> str:
        return f"{self.value[:4]}-{self.value[-2:]}"


class Nationality(Enum):
    USA = "USA"
    FIN = "FIN"
    CAN = "CAN"
    SWE = "SWE"
    CZE = "CZE"
    RUS = "RUS"
    SLO = "SLO"
    FRA = "FRA"
    GBR = "GBR"
    SVK = "SVK"
    DEN = "DEN"
    NED = "NED"
    AUT = "AUT"
    BLR = "BLR"
    GER = "GER"
    SUI = "SUI"
    NOR = "NOR"
    UZB = "UZB"
    LAT = "LAT"
    AUS = "AUS"