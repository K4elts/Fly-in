"""Command-line interface for Fly-in."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    """Build and return the argument parser."""
    parser = argparse.ArgumentParser(
        description="Route drones through a network of zones.",
    )
    parser.add_argument(
        "--map",
        type=Path,
        required=True,
        help="path to the map file",
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="disable ANSI colours in the terminal output",
    )
    parser.add_argument(
        "--gui",
        action="store_true",
        help="open the optional graphical view",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="print additional debug information",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the command-line interface and return an exit code."""
    args = build_parser().parse_args(argv)
    print(
        f"Fly-in: estructura lista. Mapa: {args.map}. Simulación pendiente.",
        file=sys.stderr,
    )
    return 0
