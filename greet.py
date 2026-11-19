"""Tiny greeting helpers used as sandbox material for the agent."""


def greet(name: str) -> str:
    """Return a greeting for `name`, trimming spaces and falling back to "朋友" when empty."""
    clean = (name or "").strip()
    return f"你好，{clean or '朋友'}！"


def shout(name: str) -> str:
    """Return the greeting for `name` in uppercase."""
    return greet(name).upper()
