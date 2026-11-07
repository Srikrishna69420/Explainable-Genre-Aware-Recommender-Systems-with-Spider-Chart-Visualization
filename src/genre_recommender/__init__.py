"""Genre-aware movie recommendation and visualization package."""

from .data import MovieData, load_movie_data
from .preferences import build_preferences
from .ranking import recommend

__all__ = ["MovieData", "load_movie_data", "build_preferences", "recommend"]
