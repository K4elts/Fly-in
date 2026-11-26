"""Parser and validator for Fly-in map files."""

from __future__ import annotations

from pathlib import Path

from fly_in.domain import SimInput


class MapParser:
    """Read a map file and produce a validated :class:`SimInput`."""

    def parse(self, path: Path) -> SimInput:
        """Parse *path* and return the validated simulation input."""
        raise NotImplementedError("MapParser.parse is not implemented yet")
