"""Renderers for terminal and optional graphical output."""

from __future__ import annotations

from fly_in.domain import Simulation, Turn


class TerminalRenderer:
    """Render the canonical text output required by the subject."""

    def __init__(self, use_color: bool = False) -> None:
        """Configure whether ANSI colours are emitted."""
        self._use_color = use_color

    def render(self, simulation: Simulation) -> str:
        """Return the full canonical output as text."""
        raise NotImplementedError("TerminalRenderer.render is not implemented yet")

    def render_turn(self, turn: Turn) -> str:
        """Return the canonical line for a single *turn*."""
        raise NotImplementedError("TerminalRenderer.render_turn is not implemented yet")


class GuiRenderer:
    """Optional tkinter window showing the network and drones."""

    def __init__(self, simulation: Simulation) -> None:
        """Store the simulation to display."""
        self._simulation = simulation

    def show(self) -> None:
        """Open the window and block until it is closed."""
        raise NotImplementedError("GuiRenderer.show is not implemented yet")
