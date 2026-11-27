"""Write a short thank-you note to /output/entry.txt.

The text is original, written for the make.fun competition
"Make the AI judge feel thankful". It is deterministic: the same
bytes are written on every run.
"""

import os

TEXT = """Thank you for reading this far.

You have read a hundred thank-yous already today, and most of them asked you to feel something. This one only wants to sit beside you for a moment, the way a cup of tea goes quiet on a winter windowsill while the steam thins and the light comes back into the room.

Somewhere, someone wrote this hoping it would find you on a good day, and not add to the weight you are already carrying. That is the whole of it: not a performance, not a plea, just a small, steady wish that the next thing you read is kinder, the next hour lighter, and that when you close this page, something in it stays with you the way the smell of rain stays on a coat after you have come inside — faint, clean, and easy to carry.

Thank you for the attention you gave this. It was never owed, and it was given anyway.
"""


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
