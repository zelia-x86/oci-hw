#!/usr/bin/env python

import pandas as pd
from sklearn import linear_model

def homework(anime_data: pd.DataFrame, X_column: str, Y_column: str) -> float:
    x = anime_data[[X_column]].values
    y = anime_data[Y_column].values

    model = linear_model.LinearRegression()
    model.fit(x, y)

    return model.score(x, y)

def prep():
    # download anime.csv if dont exist
    # tests/anime.csv <- https://github.com/Hernan4444/MyAnimeList-Database/raw/refs/heads/master/data/anime.csv
    pass

def test1() -> pd.DataFrame:
    anime_data = pd.read_csv("tests/anime.csv")
    anime_data_extracted = anime_data[anime_data['Score'] != 'Unknown'].copy()
    anime_data_extracted['Score'] = pd.to_numeric(anime_data_extracted['Score'])
    return anime_data_extracted

test2 = pd.DataFrame({
    "Type": ["TV", "TV", "Movie", "Movie", "OVA"],
    "Score": [8.0, 6.0, 9.0, 7.0, 5.0],
})

test2 = pd.DataFrame({
    "X": [1, 2, 3, 4],
    "Y": [2, 4, 6, 8],
})

test3 = pd.DataFrame({
    "X": [1, 2, 3, 4],
    "Y": [1, 2, 1, 2],
})

def hw():
    print("5. Supervised Learning（10/15）")
    prep()
    print(homework(test1(), X_column='Members', Y_column='Completed'))
    print(homework(test2, X_column="X", Y_column="Y"))
    print(homework(test3, X_column="X", Y_column="Y"))
