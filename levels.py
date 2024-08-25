from dataclasses import dataclass
from typing import List, Tuple

def add_columns_around_pig(pig_x, pig_y):
    return [
        (pig_x - 60, pig_y - 40),
        (pig_x, pig_y - 40),
        (pig_x + 60, pig_y - 40),
        (pig_x - 60, pig_y + 40, True),
        (pig_x + 60, pig_y + 40, True),
    ]

@dataclass
class LevelData:
    columns: List[Tuple[float, float, bool]]
    pigs: List[Tuple[float, float]]

COLUMN_HEIGHT = 89

levels = [
    LevelData(
        columns=[(900, 50), (900, 130), (1300, 50)],
        pigs=[(1100, 100)],
    ),
    LevelData(
        columns=[
            *add_columns_around_pig(920, 100),  # Columnas alrededor del cerdo en (920, 100)
            *add_columns_around_pig(1200, 100), # Columnas alrededor del cerdo en (1200, 100)
            (850, 50),   # Columna base para estabilidad
            (850, 50 + COLUMN_HEIGHT),  # Columna base para estabilidad
        ],
        pigs=[(920, 100), (1200, 100)],
    ),
    LevelData(
        columns=[
            *add_columns_around_pig(800, 100),
            *add_columns_around_pig(1200, 100),
        ],
        pigs=[(800, 100), (1200, 100)],
    ),
    LevelData(
        columns=[
            *add_columns_around_pig(700, 100),
            *add_columns_around_pig(1000, 100),
            *add_columns_around_pig(1300, 100),
            (850, 50),
            (850, COLUMN_HEIGHT + 50),
            (850, COLUMN_HEIGHT * 2 + 50),
            (850, COLUMN_HEIGHT * 3 + 50),
            (850, COLUMN_HEIGHT * 4 + 50),
            (850, COLUMN_HEIGHT * 5 + 50),
        ],
        pigs=[(700, 100), (1000, 100), (1300, 100)],
    ),
    LevelData(
        columns=[
            *add_columns_around_pig(600, 100),
            *add_columns_around_pig(950, 100),
            *add_columns_around_pig(1300, 100),
            (775, 50),
            (1125, 50),
            (1475, 50),
        ],
        pigs=[(600, 100), (950, 100), (1300, 100)],
    ),
]
