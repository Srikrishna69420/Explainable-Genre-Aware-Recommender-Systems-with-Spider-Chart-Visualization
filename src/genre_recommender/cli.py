"""Command-line entry point for the modular recommender."""

import argparse
from pathlib import Path

from .data import load_movie_data
from .preferences import build_preferences
from .ranking import recommend
from .visualization import plot_spider


def main():
    project_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description="Genre-aware MovieLens recommender")
    parser.add_argument("--data-dir", default=str(project_root / "Recommender_small" / "data"))
    parser.add_argument("--genres", nargs="*", default=["Action", "Adventure", "Drama", "Romance"])
    parser.add_argument("--watched", nargs="*", type=int, default=[1, 260, 1196])
    parser.add_argument("-k", type=int, default=5)
    args = parser.parse_args()

    data = load_movie_data(args.data_dir)
    weights = build_preferences(data.genres, args.genres, args.watched, data)
    movie_ids = recommend(data, weights, k=args.k)
    print("Recommended Movies:")
    for movie_id in movie_ids:
        print(f"- {data.movies[movie_id]['title']} (rating: {data.average_ratings[movie_id]:.2f})")
    plot_spider(data, weights, movie_ids, max_movies=args.k)


if __name__ == "__main__":
    main()
