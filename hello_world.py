#!/usr/bin/env python3
"""Simple hello-world program with function API and CLI options."""

from __future__ import annotations

import argparse


def build_greeting(name: str = "World", excited: bool = False) -> str:
    """Return a greeting string.

    Bugfix: empty or whitespace-only names now fall back to "World".
    """
    clean_name = name.strip() or "World"
    punctuation = "!" if excited else "."
    return f"Hello, {clean_name}{punctuation}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Print a friendly greeting")
    parser.add_argument("--name", default="World", help="Name to greet")
    parser.add_argument(
        "--excited",
        action="store_true",
        help="Use exclamation punctuation instead of a dot",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(build_greeting(args.name, excited=args.excited))


if __name__ == "__main__":
    main()
