"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt.
Gate (from the kit): UTF-8 text, 1 to 320 characters, not only whitespace.
Python 3.13, standard library only, no network.
"""

from pathlib import Path

ENTRY = (
    "Congress passed a 400-page law telling AI exactly how to think, "
    "then called IT because nobody in the room could turn the bill "
    "itself into a PDF."
)

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 320


def gate_check(text: str) -> None:
    """Enforce the entry gate exactly; raise ValueError on any failure."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1 to {MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line with no line breaks")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence ending in a period")
    text.encode("utf-8")


def main() -> None:
    gate_check(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
