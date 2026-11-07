# Explainable Genre-Aware Movie Recommender

A small, exploratory movie recommender that combines a user's genre preferences with MovieLens ratings and visualizes recommendations with a radar (spider) chart.

## Quick start: modular version

The new modular implementation lives in `src/genre_recommender/`:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
python -m pip install -r requirements.txt
PYTHONPATH=src python -m genre_recommender.cli
```

The modular CLI defaults to the bundled small MovieLens dataset. To change inputs:

```bash
PYTHONPATH=src python -m genre_recommender.cli --data-dir Recommender_small/data --genres Action Comedy --watched 1 260 -k 10
```

On Windows PowerShell, set the import path for the command with `$env:PYTHONPATH="src"`.

## Repository contents

- `src/genre_recommender/` — modular implementation, split into data loading, preference construction, ranking, visualization, and CLI modules.
- `Recommender.py` — original full-dataset script, retained unchanged.
- `Recommender_small/` — original small-dataset variant and its CSV files, retained unchanged.
- `Recommender_big` — existing large-dataset companion file/link placeholder.
- `docs/REPRODUCIBILITY.md` — data and experiment notes.

The modular implementation is a clean entry point; the original scripts remain available for comparison and rollback.

## Data

The small variant reads `Recommender_small/data/movies.csv` and `ratings.csv`. The `links.csv` and `tags.csv` files are retained but not consumed by the recommender.

The root-level legacy `Recommender.py` expects `data/movies.csv` and `data/ratings.csv` at the repository root; that directory is not currently present. The full legacy variant is not runnable from a fresh clone until its data files are supplied.

## Method

1. Load movie genres and ratings from CSV.
2. Build genre preference weights from explicit preferences and watched movies.
3. Normalize the preference vector.
4. Score movies using genre match, average rating, and rating-count share.
5. Plot preferences and recommended movies on a polar chart.

The scoring weights (`alpha`, `beta`, and `gamma`) retain the original default values in the modular ranking function.

## Reproducibility and limitations

The original scripts and data are not removed or overwritten. The modular package has not been benchmarked against the original script; use the same data and inputs when comparing outputs. Plotting requires a graphical display or configured Matplotlib backend.
