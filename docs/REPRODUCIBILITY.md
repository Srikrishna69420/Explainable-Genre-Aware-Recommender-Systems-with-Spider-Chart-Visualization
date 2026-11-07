# Data and reproducibility

## Dataset variants

### Small variant
Run `python Recommender_small/Recommender.py` from the repository root. The script resolves CSV files under `Recommender_small/data/`.

### Full variant
The root `Recommender.py` resolves `data/movies.csv` and `data/ratings.csv` relative to the repository root. Those files are not present in the current tree. Add the correctly licensed MovieLens files at those paths before running this script.

## Inputs

- `movies.csv`: `movieId`, `title`, and `genres` columns.
- `ratings.csv`: `movieId` and `rating` columns.

The small data directory also contains `links.csv` and `tags.csv`, which the current script does not consume.

## Environment

Install dependencies with `python -m pip install -r requirements.txt`. The implementation uses the Python standard library, NumPy, and Matplotlib. Record exact Python and package versions when publishing results.

## Reproducing the example

Example preferences and watched movie IDs are hard-coded in each script's main block. Edit those values to try another profile. Plotting requires a graphical display or a configured Matplotlib backend.

## Known caveats

- The scripts use different example inputs.
- The full variant's expected `data/` directory is absent.
- Scoring coefficients are constants in the source.
- No automated tests or benchmark protocol are currently included.
