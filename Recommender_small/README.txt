Explainable Genre-Aware Recommender System with Spider Chart Visualization
=========================================

Author: Srikrishna U. B.

This project implements an explainable recommender system that combines explicit user preferences, implicit feedback from watched movies, and movie ratings to generate personalized movie recommendations. The system emphasizes interpretability through spider (radar) chart visualizations that explain why specific movies are recommended.

This implementation accompanies the research paper:
"Explainable Genre-Aware Recommender Systems with Spider Chart Visualization"

--------------------------------------------------
PROJECT STRUCTURE
--------------------------------------------------

recommender-spider/

data/
    movies.csv
        Movie metadata file containing at least:
        - movieId
        - genres (pipe-separated, e.g., Action|Sci-Fi)

    ratings.csv
        Ratings file containing at least:
        - movieId
        - rating (0–5)

recommender.py
    Main script implementing:
    - preference learning
    - recommendation scoring
    - spider chart visualization

figures/
    spider_plot.png
        Generated visualization of recommended movies

paper/
    paper.tex
        LaTeX source for the accompanying research paper

README.txt
    This file


--------------------------------------------------
REQUIREMENTS
--------------------------------------------------

- Python 3.8 or higher

Standard Python libraries only:
- csv
- math
- collections
- numpy
- matplotlib
- os

No external machine learning frameworks are required.


--------------------------------------------------
HOW THE SYSTEM WORKS
--------------------------------------------------

1. Explicit Preferences
   The user specifies preferred genres (e.g., Action, Adventure, Sci-Fi).
   These genres initialize a user preference vector.

2. Implicit Feedback
   The system refines preferences using movies the user has watched.
   Genres associated with highly rated movies receive higher weights.
   More ratings receive higher weights

3. Recommendation Scoring
   Each movie is scored using a hybrid function that balances:
   - Genre alignment with user preferences
   - Global movie rating

   A trade-off parameter alpha controls personalization versus popularity.

4. Explainability
   Recommended movies are visualized using spider charts.
   Each axis corresponds to a genre, and values encode rating-weighted
   preference alignment. Overlap with the user preference polygon
   provides an intuitive explanation.


--------------------------------------------------
HOW TO RUN
--------------------------------------------------

From the project root directory:

    python recommender.py

The script will:
- Load CSV data from the data/ directory
- Compute personalized recommendations
- Plot spider charts for the top recommended movies
- Save figures in the figures/ directory


--------------------------------------------------
DATA NOTES
--------------------------------------------------

- Genre strings must be pipe-separated (e.g., Comedy|Drama)
- Ratings are assumed to be on a 0–5 scale
- The system is designed for MovieLens-style datasets


--------------------------------------------------
RESEARCH CONTEXT
--------------------------------------------------

This project prioritizes:
- Interpretability over predictive optimality
- Transparency in recommendation logic
- Human-understandable explanations

It is suitable for:
- Explainable AI (XAI) research
- Recommender systems coursework
- Visualization-driven ML studies
- Reproducible research artifacts

If you use or extend this work, please cite the accompanying paper.


--------------------------------------------------
CONTACT
--------------------------------------------------

Srikrishna U. B.
