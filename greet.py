"""Tiny greeting helpers used as sandbox material for the agent."""


def greet(name: str) -> str:
    """Return a greeting for `name`, falling back to "朋友" when empty."""
    return f"你好，{name or '朋友'}！"
