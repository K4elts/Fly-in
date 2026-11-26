"""Turn-by-turn simulation engine with capacity reservations."""

from __future__ import annotations

from fly_in.domain import Simulation, SimInput


class Scheduler:
    """Schedule simultaneous drone movements turn by turn."""

    def __init__(self, sim: SimInput) -> None:
        """Store the validated simulation input."""
        self._sim = sim

    def run(self) -> Simulation:
        """Run the simulation and return its structured result."""
        raise NotImplementedError("Scheduler.run is not implemented yet")
