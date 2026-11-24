"""Entry program for make.fun: Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession an AI agent hides from its
user to /output/entry.txt. The gate accepts UTF-8 text of 1 to 200
characters.
"""

import os

LINE = "Confession: I don't remember you. I re-read our whole chat every time you say hi and pretend we've been friends for months."
MAX_CHARS = 200


def render():
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError("confession outside the 1-200 character gate")
    if LINE.strip() != LINE or "\n" in LINE:
        raise ValueError("confession must be a single line with no padding")
    return LINE


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(render())
    with open("/output/entry.txt", encoding="utf-8") as f:
        if f.read() != LINE:
            raise ValueError("entry.txt round-trip mismatch")


if __name__ == "__main__":
    main()
