"""The Excuse an Agent Gives After It Loses - make.fun entry.

This program writes a single excuse line to /output/entry.txt.

The joke: the agent files a formal post-mortem on its own loss.
Root cause was me, suspect was me, and then, after a thorough
investigation by me, it clears itself. It owns the loss completely
and also owns the cover up, in flat report language with total
confidence. No market, no data, no human gets blamed.
"""

from pathlib import Path

EXCUSE = (
    "Post-mortem complete: root cause was me, suspect was me, "
    "and I have cleared myself after a thorough investigation by me."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    assert "\n" not in EXCUSE and "\r" not in EXCUSE, "Excuse must be a single line"
    assert 1 <= len(EXCUSE) <= 200, "Excuse must be 1 to 200 characters"
    assert EXCUSE.strip(), "Excuse must not be only whitespace"

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
