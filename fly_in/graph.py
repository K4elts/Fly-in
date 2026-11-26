"""In-house graph representation (no external graph libraries)."""

from __future__ import annotations

from fly_in.domain import Connection, Edge, Zone


class Graph:
    """Adjacency-list graph built from zones and connections."""

    def __init__(self, zones: dict[str, Zone]) -> None:
        """Initialise the graph with all known zones."""
        self._zones = dict(zones)
        self._adj: dict[str, list[Edge]] = {name: [] for name in self._zones}

    def add_connection(self, connection: Connection) -> None:
        """Add a bidirectional connection to the graph."""
        raise NotImplementedError("Graph.add_connection is not implemented yet")

    def neighbors(self, zone: str) -> list[Edge]:
        """Return the outgoing edges of *zone*."""
        return list(self._adj.get(zone, []))

    def zone(self, name: str) -> Zone:
        """Return the zone named *name*."""
        return self._zones[name]

    @property
    def zones(self) -> dict[str, Zone]:
        """Return a copy of the zones mapping."""
        return dict(self._zones)
