import pandas as pd
import json



if __name__ == "__main__":
    #dataset_credits = pd.read_csv('tmdb_5000_credits.csv')
    #dataset_credits.drop(['movie_id'], 1, inplace=True)
    
    dataset = pd.read_csv('tmdb_5000_movies.csv')
    dataset.describe()
    genres = dataset["genres"]
    homepage = dataset["homepage"]
    keywords = dataset["keywords"]
    original_language = dataset["original_language"]
    title = dataset["original_title"]
    overview = dataset["overview"]
    popularity = dataset["popularity"]
    production_companies = dataset["produtction_companies"]
    production_countries = dataset["production_countries"]
    release_date = dataset["release_date"]
    revenue = dataset["revenue"]
    runtime = dataset["runtime"]
    spoken_languages = dataset["spoken_languages"]
    tagline = dataset["tagline"]
    vote_average = dataset["vote_average"]
    vote_count = dataset["vote_count"]

