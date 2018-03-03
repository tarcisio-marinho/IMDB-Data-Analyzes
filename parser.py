import pandas as pd


if __name__ == "__main__":
    dataset_credits = pd.read_csv('tmdb_5000_credits.csv')
    dataset = pd.read_csv('tmdb_5000_movies.csv')
    
    dataset_credits.drop(['movie_id'], 1, inplace=True)
    for f in dataset["original_title"]:
        print(f)
