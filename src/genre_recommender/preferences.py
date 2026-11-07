"""User genre preference construction."""


def build_preferences(genres, explicit_preferences=(), watched_movie_ids=(), data=None, eta=0.1):
    """Create normalized genre weights from explicit likes and watched movies."""
    weights = {genre: (1.0 if genre in explicit_preferences else 0.0) for genre in genres}
    if data is not None:
        for movie_id in watched_movie_ids:
            if movie_id not in data.movies or movie_id not in data.average_ratings:
                continue
            rating = data.average_ratings[movie_id]
            for genre in data.movies[movie_id]["genres"]:
                weights[genre] = weights.get(genre, 0.0) + eta * rating
    maximum = max(weights.values(), default=0.0)
    if maximum > 0:
        weights = {genre: value / maximum for genre, value in weights.items()}
    return weights
