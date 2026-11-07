"""Spider-chart visualization."""

import math
import numpy as np
import matplotlib.pyplot as plt


def plot_spider(data, user_weights, movie_ids, max_movies=5):
    genres = data.genres
    if not genres:
        raise ValueError("No genres were found in the movie metadata.")
    angles = np.linspace(0, 2 * math.pi, len(genres), endpoint=False)
    closed_angles = np.concatenate([angles, [angles[0]]])
    fig = plt.figure(figsize=(9, 9))
    ax = plt.subplot(111, polar=True)
    ax.set_theta_offset(math.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_xticks(angles)
    ax.set_xticklabels(genres, fontsize=9)
    ax.set_ylim(-1, 5)
    ax.set_yticks([0, 1, 2, 3, 4, 5])
    ax.yaxis.grid(False)
    ax.xaxis.grid(False)
    for radius in [0, 1, 2, 3, 4, 5]:
        ax.plot(closed_angles, [radius] * len(closed_angles), linestyle="dotted", color="gray", linewidth=0.8, alpha=0.6)
    for angle in angles:
        ax.plot([angle, angle], [-1, 5], linestyle="dotted", color="gray", linewidth=0.8, alpha=0.6)
    user_values = [user_weights.get(genre, 0.0) * 5 for genre in genres]
    ax.plot(closed_angles, user_values + [user_values[0]], linewidth=3, linestyle="--", marker="o", label="User Preference")
    ax.fill(closed_angles, user_values + [user_values[0]], alpha=0.18)
    for movie_id in movie_ids[:max_movies]:
        if movie_id not in data.movies or movie_id not in data.average_ratings:
            continue
        rating = data.average_ratings[movie_id]
        movie_genres = data.movies[movie_id]["genres"]
        values = [rating if genre in movie_genres else 0 for genre in genres]
        ax.plot(closed_angles, values + [values[0]], linewidth=1.6, marker="o", alpha=0.9, label=data.movies[movie_id]["title"][:28])
        ax.fill(closed_angles, values + [values[0]], alpha=0.08)
    ax.legend(loc="upper right", bbox_to_anchor=(1.35, 1.15), fontsize=9)
    plt.title("User Preference vs Recommended Movies", fontsize=14, pad=25)
    plt.show()
