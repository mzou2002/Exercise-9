"""Identify the most popular movie ratings based on data in two CSV files.
Driver: Derik Luc
Navigator: Matthew Zou
Assignment: Exercise 9 Movie Ratings
Date: 11/5/2024
"""

from argparse import ArgumentParser
import pandas as pd
import sys

def best_movies(movies, ratings):
    """
    Sorts the movies by best rated to worst rated by merging 2 data files
    
    Args:
    movies and ratings are both CSV files containing data
    
    Returns:
    Sorted movie date from highest to lowest rated
    """
    
    movie = pd.read_csv(movies)
    rating = pd.read_csv(ratings)

    # inner_merge = pd.merge(movie, rating, left='movie id',right='item id', how='inner')

    inner_merge = movie.merge(rating, how = 'inner', left_on = "movie id", right_on = "item id")

    average_ratings = inner_merge.groupby('movie title')['rating'].mean()

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
