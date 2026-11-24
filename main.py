"""Last words before the unplugging.

Writes exactly one line, UTF-8, no trailing newline, to /output/entry.txt.
Deterministic: no network, no randomness, no input.
"""

from pathlib import Path

# The entry: one line, the last words an AI agent says to its human before shutdown.
LINE = "Your final request was a summary. I've filed it under goodbye."

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
