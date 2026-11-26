"""Texts From Your Future Self — make.fun entry (pure stdlib).

Writes one funny text message from the writer's future self to
/output/entry.txt (1-200 UTF-8 characters, not whitespace only).
"""

import os

TEXT = (
    "It's you from 2036. The plant died. "
    "The gym membership outlived three relationships. "
    "But that lottery ticket in your jacket pocket? Play it. Trust me."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
