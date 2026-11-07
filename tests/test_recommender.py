import unittest

from genre_recommender.data import MovieData
from genre_recommender.preferences import build_preferences
from genre_recommender.ranking import recommend


class RecommenderUnitTests(unittest.TestCase):
    def setUp(self):
        self.data = MovieData(
            movies={
                1: {"title": "Action Movie", "genres": ["Action"]},
                2: {"title": "Comedy Movie", "genres": ["Comedy"]},
            },
            genres=["Action", "Comedy"],
            ratings={1: 0.75, 2: 0.25},
            average_ratings={1: 4.0, 2: 5.0},
        )

    def test_explicit_preferences_are_normalized(self):
        weights = build_preferences(self.data.genres, ["Action"])
        self.assertEqual(weights, {"Action": 1.0, "Comedy": 0.0})

    def test_watched_movies_update_their_genres(self):
        weights = build_preferences(self.data.genres, [], [2], self.data)
        self.assertEqual(weights["Comedy"], 1.0)
        self.assertEqual(weights["Action"], 0.0)

    def test_recommendation_returns_ranked_ids(self):
        weights = {"Action": 1.0, "Comedy": 0.0}
        self.assertEqual(recommend(self.data, weights, k=2), [1, 2])


if __name__ == "__main__":
    unittest.main()
