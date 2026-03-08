"""
This is a recommender system built purely for fulfillment of curiosity and wanting to explore a novel way to visualize recommender system using spider chart.
I have used the MovieLens dataset for demonstration purposes, having obtained the rights to distribute the dataset under the same license.
The reader can download the code to test it out for themselves.
"""

import csv
import math
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
import os


#========================================================
# 1.  Loading Data

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MOVIES_CSV = os.path.join(BASE_DIR, "data", "movies.csv")
RATINGS_CSV = os.path.join(BASE_DIR, "data", "ratings.csv")

movies = {}
all_genres = set()

with open(MOVIES_CSV, newline='', encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        movie_id = int(row["movieId"])
        genres = row["genres"].split("|") if row["genres"] != "(no genres listed)" else []
        movies[movie_id] = {"title": row["title"], "genres": genres}
        for g in genres:
            all_genres.add(g)

all_genres = sorted(list(all_genres))

#Computing average ratings
ratings_sum = defaultdict(float)
ratings_count = defaultdict(int)
total = 0

with open(RATINGS_CSV, newline='', encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        movie_id = int(row["movieId"])
        rating = float(row["rating"])
        ratings_sum[movie_id] += rating
        ratings_count[movie_id] += 1
        total += 1

ratings = {movie_id: ratings_count[movie_id] / total for movie_id in ratings_sum}
avg_ratings = {movie_id: ratings_sum[movie_id] / ratings_count[movie_id] for movie_id in ratings_sum}

#==========================================================



# =========================================================
# 2.   User Preference Model

def init_user_preferences(all_genres, explicit_preferences):
    weights = {}
    for g in all_genres:
        weights[g] = 1.0 if g in explicit_preferences else 0.0

    return weights

def update_preferences(weights, watched_movies, eta=0.1):
    for movie_id in watched_movies:
        if movie_id not in movies or movie_id not in avg_ratings:
            continue

        rating = avg_ratings[movie_id]
        for g in movies[movie_id]["genres"]:
            weights[g] += eta * rating

    return weights

def normalize_preferences(weights):
    max_val = max(weights.values())
    if max_val == 0:
        return weights

    for g in weights:
        weights[g] /= max_val

    return weights

# =======================================================

"""

Below is an important parameter which can be changed according to the reader. Personally, I have found three things to be important for better recommendations.
People tend to like movies of similar genre, if not same. For this I have introduced alpha, which can take values from 0 to 1. Alpha can be thought of as the parameter 
which controls the influence of genre. A movie having similar genre does not imply the user will like it. So we use the ratings given by people, and for this I have 
introduced beta, which can take values from 0 to 1, but should be lesser than 1 - alpha since it might cause the score to go over 5. Beta can be thought of as the 
parameter which controls the influence of ratings. A movie having good ratings does not imply the user will like it. So we use the number of people who rated it. 
This reduces the influence of biased ratings, and this parameter is gamma. Gamma can be thought of as the parameter which controls the influence of number of ratings,
and can take values from 0 to infinity, but should not be more than 1000 since it might cause the score to go over 5. 

"""

# =======================================================
# 3.   Recommender

def recommend(weights, k=10):
    alpha = 0.8
    beta = 0.2
    gamma = 200
    scored_movies = []
    for movie_id, info in movies.items():
        if movie_id not in avg_ratings:
            continue

        ratings_total = ratings[movie_id]
        rating = avg_ratings[movie_id]
        genre_score = sum(weights.get(g, 0) for g in info["genres"])
        score = alpha * genre_score + beta * (rating / 5) + gamma * ratings_total
        scored_movies.append((score, movie_id))
    scored_movies.sort(reverse=True)

    if all(score == 0 for score, _ in scored_movies):
        scored_movies.sort(key=lambda x: avg_ratings[x[1]], reverse=True)

    return [movie_id for _, movie_id in scored_movies[:k]]

# =======================================================



# =======================================================
# 4.   Spider Values

def build_spider_values(movie_id, all_genres, weights, min_visible=0.3):
    values = []
    rating = avg_ratings[movie_id]
    movie_genres = movies[movie_id]["genres"]

    for g in all_genres:
        if g in movie_genres:
            v = weights.get(g, 0) * rating
            values.append(max(v, min_visible))
        else:
            values.append(0)

    return values

# =========================================================



# =========================================================
# 5.  Plotting top movies on spider chart

def plot_spider(user_weights, movie_ids, all_genres, max_movies=5):
    genres = all_genres
    N = len(genres)

    angles = np.linspace(0, 2 * math.pi, N, endpoint=False)
    angles = np.concatenate([angles, [angles[0]]])
    fig = plt.figure(figsize=(9, 9))
    ax = plt.subplot(111, polar=True)
    ax.set_theta_offset(math.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(genres, fontsize=9)
    ax.set_ylim(-1, 5)
    ax.set_yticks([0,1, 2, 3, 4, 5])
    ax.set_yticklabels(["0","1", "2", "3", "4", "5"], fontsize=8, color="gray")

    ax.yaxis.grid(False)
    ax.xaxis.grid(False)
    for r in [0, 1, 2, 3, 4, 5]:
        ax.plot(angles, [r] * len(angles), linestyle="dotted", color="gray", linewidth=0.8, alpha=0.6)

    for angle in angles[:-1]:
        ax.plot([angle, angle], [-1, 5], linestyle="dotted", color="gray", linewidth=0.8, alpha=0.6)

    user_vals = [user_weights[g] * 5 for g in genres]
    user_vals.append(user_vals[0])
    ax.plot(angles, user_vals, linewidth=3, linestyle="--", marker="o", label="User Preference")
    ax.fill(angles, user_vals, alpha=0.18)

    for movie_id in movie_ids[:max_movies]:
        vals = []
        rating = avg_ratings[movie_id]
        movie_genres = movies[movie_id]["genres"]
        for g in genres:
            vals.append(rating if g in movie_genres else 0)

        vals.append(vals[0])
        ax.plot(angles, vals, linewidth=1.6, marker="o", alpha=0.9, label=movies[movie_id]["title"][:28])
        ax.fill(angles, vals, alpha=0.08)

    ax.legend(loc="upper right", bbox_to_anchor=(1.35, 1.15), fontsize=9)
    plt.title("User Preference vs Recommended Movies", fontsize=14, pad=25)
    plt.show()

# ========================================================



# ========================================================
# 6.  Main Execution

if __name__ == "__main__":
    preferred_genres = []
    watched_movies = [1, 260, 1196]

    weights = init_user_preferences(all_genres, preferred_genres)
    weights = update_preferences(weights, watched_movies)
    weights = normalize_preferences(weights)
    top_movies = recommend(weights, k=5)

    print("Recommended Movies:")
    for m in top_movies:
        print("-", movies[m]["title"], "(rating:", round(avg_ratings[m], 2), ")")

    plot_spider(weights, top_movies, all_genres, 5)


