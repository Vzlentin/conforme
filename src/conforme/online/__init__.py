"""Online calibration: the order in which targets become known, and one origin at a time."""

from conforme.online.state import flatten, unflatten
from conforme.online.step import Issue, initial_state, step

__all__ = ["Issue", "flatten", "initial_state", "step", "unflatten"]
