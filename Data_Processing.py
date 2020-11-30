import pandas as pd

user_rating_matrix = pd.read_csv(
    "./data/ml-latest-small/ratings.csv", parse_dates=True)

m = user_rating_matrix[["userId", "movieId", "rating"]]

user_rating = m.pivot(index="userId", columns="movieId", values="rating")

user_rating.head()
