"""Pathfinding with movement costs and priority preference."""

from __future__ import annotations

from dataclasses import dataclass

from fly_in.domain import Edge
from fly_in.graph import Graph


@dataclass(frozen=True)
class Route:
    """A path from start to end."""

    edges: tuple[Edge, ...]
    turns: int
    uses_priority: bool


class PathFinder:
    """Compute routes using a custom Dijkstra implementation."""

    def __init__(self, graph: Graph) -> None:
        """Store the graph used for all queries."""
        self._graph = graph

    def shortest_path(self, start: str, end: str) -> Route:
        """Return the cheapest route from *start* to *end*."""
        raise NotImplementedError("PathFinder.shortest_path is not implemented yet")
