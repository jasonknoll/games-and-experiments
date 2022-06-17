import csv
from typing import List, Optional
import pandas as pd

from sqlmodel import Field, SQLModel, create_engine

class Player(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    position: str
    team: str
    nationality: str

skaters_path = 'sheets/skaters.csv'


def load_csv(file_path: str) -> List[List[str]]:
    return pd.read_csv(file_path).dropna()


def show_cols(df: pd.DataFrame) -> None:
    print(list(df.columns))


skaters = load_csv(skaters_path)

all_players = load_csv('sheets/allPlayersLookup.csv')
#show_cols(all_players)


all_players_db_name = 'all_players_since_2007.db'
db_url = f'sqlite:///dbs/{all_players_db_name}'

engine = create_engine(db_url, echo=True)

SQLModel.metadata.create_all(engine)