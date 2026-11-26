"""Domain models for the Fly-in simulation."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class ZoneType(Enum):
    """Types of zone defined by the subject."""

    NORMAL = "normal"
    BLOCKED = "blocked"
    RESTRICTED = "restricted"
    PRIORITY = "priority"


class DroneState(Enum):
    """State of a drone during a simulation."""

    AT_ZONE = "at_zone"
    IN_TRANSIT = "in_transit"
    DELIVERED = "delivered"


@dataclass(frozen=True)
class Zone:
    """A zone (hub) in the network."""

    name: str
    x: int
    y: int
    zone_type: ZoneType = ZoneType.NORMAL
    color: str | None = None
    max_drones: int = 1
    is_start: bool = False
    is_end: bool = False


@dataclass(frozen=True)
class Connection:
    """A bidirectional link between two zones."""

    source: str
    target: str
    max_link_capacity: int = 1


@dataclass(frozen=True)
class Edge:
    """A directed edge used by the pathfinder."""

    target: str
    cost: int
    connection: Connection
    is_priority: bool = False


@dataclass
class Drone:
    """A drone moving through the network."""

    drone_id: int
    zone: str
    state: DroneState = DroneState.AT_ZONE
    in_transit_to: str | None = None
    turns_remaining: int = 0


@dataclass(frozen=True)
class Movement:
    """One drone movement inside a turn."""

    drone_id: int
    destination: str
    via_connection: str | None = None


@dataclass(frozen=True)
class Turn:
    """Snapshot of one simulation turn."""

    number: int
    movements: tuple[Movement, ...]
    drones: dict[int, Drone]


@dataclass(frozen=True)
class Simulation:
    """Complete result of a simulation."""

    turns: tuple[Turn, ...]


@dataclass(frozen=True)
class SimInput:
    """Validated input produced by the parser."""

    nb_drones: int
    zones: dict[str, Zone]
    connections: tuple[Connection, ...]
    start: str
    end: str


class FlyInError(Exception):
    """Base class for Fly-in errors."""


class ParseError(FlyInError):
    """Raised when the map file is invalid."""

    def __init__(self, line: int, cause: str) -> None:
        """Store the line number and the cause of the error."""
        super().__init__(f"line {line}: {cause}")
        self.line = line
        self.cause = cause


class UnsolvableMapError(FlyInError):
    """Raised when a valid map cannot be solved."""
