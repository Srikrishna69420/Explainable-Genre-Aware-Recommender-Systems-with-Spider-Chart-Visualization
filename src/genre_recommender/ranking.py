"""Movie ranking logic."""


def recommend(data, weights, k=10, alpha=0.8, beta=0.2, gamma=200):
    """Return up to *k* movie IDs ranked by genre, rating, and rating share."""
    scored = []
    for movie_id, movie in data.movies.items():
        if movie_id not in data.average_ratings:
            continue
        genre_score = sum(weights.get(genre, 0.0) for genre in movie["genres"])
        score = (
            alpha * genre_score
            + beta * (data.average_ratings[movie_id] / 5.0)
            + gamma * data.ratings.get(movie_id, 0.0)
        )
        scored.append((score, movie_id))
    scored.sort(reverse=True)
    if scored and all(score == 0 for score, _ in scored):
        scored.sort(key=lambda item: data.average_ratings[item[1]], reverse=True)
    return [movie_id for _, movie_id in scored[:k]]
