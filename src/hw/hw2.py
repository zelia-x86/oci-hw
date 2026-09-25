#!/usr/bin/env python

import pandas as pd

def homework(anime_data) -> pd.Series:
    return anime_data.groupby("Type")["Score"].mean().sort_values(ascending=False)

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

def hw():
    print("3. Cleaning Data Using Pandas（10/1）")
    prep()
    print(homework(test1()))
    print(homework(test2))
