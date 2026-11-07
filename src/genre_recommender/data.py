"""CSV loading and movie-rating aggregation."""

import csv
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


@dataclass
class MovieData:
    movies: dict
    genres: list
    ratings: dict
    average_ratings: dict


def load_movie_data(data_dir):
    """Load MovieLens movies.csv and ratings.csv from *data_dir*."""
    data_dir = Path(data_dir)
    movies_path = data_dir / "movies.csv"
    ratings_path = data_dir / "ratings.csv"
    if not movies_path.is_file() or not ratings_path.is_file():
        raise FileNotFoundError(
            f"Expected movies.csv and ratings.csv in {data_dir}"
        )

    movies = {}
    genres = set()
    with movies_path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            movie_id = int(row["movieId"])
            movie_genres = (
                row["genres"].split("|")
                if row["genres"] != "(no genres listed)" else []
            )
            movies[movie_id] = {"title": row["title"], "genres": movie_genres}
            genres.update(movie_genres)

    sums = defaultdict(float)
    counts = defaultdict(int)
    with ratings_path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            movie_id = int(row["movieId"])
            sums[movie_id] += float(row["rating"])
            counts[movie_id] += 1

    total = sum(counts.values())
    rating_share = {movie_id: count / total for movie_id, count in counts.items()} if total else {}
    averages = {movie_id: sums[movie_id] / counts[movie_id] for movie_id in counts}
    return MovieData(movies, sorted(genres), rating_share, averages)
