# Explainable Genre-Aware Movie Recommender

A small, exploratory movie recommender that combines a user's genre preferences with MovieLens ratings and visualizes recommendations with a radar (spider) chart.

## Project contents

- `Recommender.py` — original full-dataset script; expects `data/movies.csv` and `data/ratings.csv` beside it.
- `Recommender_small/` — small MovieLens variant, with its data directory and original script.
- `Recommender_big` — existing large-dataset companion file/link placeholder.
- `docs/` — setup, data, and reproducibility notes.

The original scripts are retained unchanged. The small variant is the one accompanied by CSV data.

## Quick start

Python 3.9 or newer is recommended.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
python -m pip install -r requirements.txt
python Recommender_small/Recommender.py
```

The script prints recommendations and opens a Matplotlib spider chart. Its data paths are resolved relative to the script.

## Data

The small variant reads `Recommender_small/data/movies.csv` and `ratings.csv`. The `links.csv` and `tags.csv` files are retained but not read by the current script.

The root-level `Recommender.py` expects a separate `data/` directory containing `movies.csv` and `ratings.csv`; that directory is not currently present. The full variant is therefore not runnable from a fresh clone until its data files are supplied.

## Method

1. Load movie genres and ratings from CSV.
2. Build genre preference weights from explicit preferences and watched movies.
3. Normalize the preference vector.
4. Score movies using genre match, average rating, and rating-count share.
5. Plot preferences and recommended movies on a polar chart.

The scoring weights (`alpha`, `beta`, and `gamma`) are constants inside the original script.

## Reproducibility and limitations

- The scripts do not expose a command-line interface or configuration file.
- Example preferences and watched movie IDs are hard-coded in each script.
- The small variant uses data committed under `Recommender_small/data/`.
- No recommendation-quality or performance claims are made here; this is an exploratory implementation.

See [Data and reproducibility](docs/REPRODUCIBILITY.md).
