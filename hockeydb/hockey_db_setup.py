from typing import List, Optional
import pandas as pd

from sqlmodel import Field, SQLModel, create_engine, Session

class Player(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    pos: str
    team: str
    nationality: str
    hand: str

skaters_path = 'sheets/skaters.csv'


def load_csv(file_path: str) -> List[List[str]]:
    return pd.read_csv(file_path).dropna()


def show_cols(df: pd.DataFrame) -> None:
    print(list(df.columns))


def add_players_to_db(df: pd.DataFrame, engine) -> None:
    #plyrs = []

    sesh = Session(engine)

    for index, row in df.iterrows():
        p = Player(name=row['name'], pos=row['position'], team=row['team'], nationality=row['nationality'], hand=row['shootsCatches'])
        
        sesh.add(p)

    sesh.commit()

    

skaters = load_csv(skaters_path)

all_players = load_csv('sheets/allPlayersLookup.csv')
#show_cols(all_players)


all_players_db_name = 'all_players_since_2007.db'
db_url = f'sqlite:///dbs/{all_players_db_name}'

engine = create_engine(db_url, echo=True)

if __name__ == '__main__':
    SQLModel.metadata.create_all(engine)