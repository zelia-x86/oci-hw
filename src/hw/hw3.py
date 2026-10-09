#!/usr/bin/env python

import pandas as pd

def homework(anime_data: pd.DataFrame, metric_column: str, n: int) -> pd.Series:
    # Step 1: Sort anime by the metric in descending order
    df = anime_data.sort_values(by=metric_column, ascending=False).copy()

    # Step 2: Rank with method='first' and cut into n equal groups using qcut
    ranks = df[metric_column].rank(method='first', ascending=False)
    df['_group'] = pd.qcut(ranks, q=n, labels=False)

    # Step 3: Compute each group's share of the overall total
    totals = df.groupby('_group')[metric_column].sum()
    total = df[metric_column].sum()
    proportions = totals / total

    # Step 4: Sort descending and relabel as Group 1, Group 2, ..., Group n
    proportions = proportions.sort_values(ascending=False).reset_index(drop=True)
    proportions.index = [f"Group {i + 1}" for i in range(len(proportions))]

    return proportions

def prep():
    # download anime.csv if dont exist
    # tests/anime.csv <- https://github.com/Hernan4444/MyAnimeList-Database/raw/refs/heads/master/data/anime.csv
    pass

def test1() -> pd.DataFrame:
    anime_data = pd.read_csv("tests/anime.csv")
    anime_data.head()

    columns_to_keep = ['MAL_ID', 'Name', 'Score', 'Type', 'Episodes',
                       'Members', 'Completed', 'Watching', 'Dropped',
                       'Popularity']
    anime_data = anime_data[columns_to_keep].copy()

    # Remove rows where key metric columns have missing or zero values
    anime_data = anime_data.dropna(subset=['Members', 'Completed', 'Watching'])
    anime_data = anime_data[(anime_data['Members'] > 0) &
                            (anime_data['Completed'] > 0) &
                            (anime_data['Watching'] > 0)]
    anime_data = anime_data.reset_index(drop=True)
    print(f"Dataset shape after preprocessing: {anime_data.shape}")
    anime_data.head()
    return anime_data

test2 = pd.DataFrame({
    "Type": ["TV", "TV", "Movie", "Movie", "OVA"],
    "Score": [8.0, 6.0, 9.0, 7.0, 5.0],
})

test2 = pd.DataFrame({
    "Completed": [40, 30, 20, 10],
})

test3 = pd.DataFrame({
    "Members": [60, 50, 40, 30, 20, 10],
})

def hw():
    print("4. Visualizing Data Using Matplotlib （10/8）")
    prep()
    print(homework(test1(), 'Completed', 5))
    print(homework(test1(), 'Completed', 10))
    print(homework(test2, "Completed", 2))
    print(homework(test3, "Members", 3))
