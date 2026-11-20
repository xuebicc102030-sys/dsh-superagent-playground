"""Tiny greeting helpers used as sandbox material for the agent."""

import sys


def greet(name: str) -> str:
    """Return a greeting for `name`, trimming spaces and falling back to "朋友" when empty."""
    clean = (name or "").strip()
    return f"你好，{clean or '朋友'}！"


def shout(name: str) -> str:
    """Return the greeting for `name` in uppercase."""
    return greet(name).upper()


def farewell(name: str) -> str:
    """Return a farewell for `name`, trimming spaces and falling back to "朋友" when empty."""
    clean = (name or "").strip()
    return f"再见，{clean or '朋友'}！"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"用法: python3 {sys.argv[0]} <名字>")
        raise SystemExit(1)
    print(greet(sys.argv[1]))
