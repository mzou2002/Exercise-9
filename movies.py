"""Identify the most popular movie ratings based on data in two CSV files."""

from argparse import ArgumentParser
import pandas as pd
import sys


def best_movies(movies, ratings):
    movie = pd.read_csv(movies)
    rating = pd.read_csv(ratings)

    inner_merge = pd.merge(movie, rating, left='movie id',right='item id', how='inner')

    average_ratings = inner_merge.groupby('title')['rating'].mean()

    return average_ratings.sort_values(ascending=False)

def parse_args(arglist):
    """ Parse command-line arguments.
    
    Args:
        arglist (list of str): a list of command-line arguments.
    
    Returns:
        namespace: the parsed command-line arguments as a namespace with
        variables movie_csv and rating_csv.
    """
    parser = ArgumentParser()
    parser.add_argument("movie_csv", help="CSV containing movie data")
    parser.add_argument("rating_csv", help="CSV containing ratings")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    movies = best_movies(args.movie_csv, args.rating_csv)
    print(movies.head())
