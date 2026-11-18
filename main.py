"""News-image entry: copy the baked front page to the output directory.

The entry is a single 1024x1024 PNG (entry.png, beside this file) that sums
up Wednesday 18 November 2026 as a one-page newspaper front page: the Quad
summit in Manila, Ukraine's strike on the Crimea bridge, Iran's drone strike
on a US radar base in Bahrain, Nvidia's $115.8bn quarter, and three more
stories, plus a ticker of the day's other news.

The program runs with no network and writes the same bytes on every run: it
only copies the image the repository holds. The output directory is
$MAKEFUN_OUTPUT_DIR outside the grader, /output inside it.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
TARGET = OUTPUT_DIR / "entry.png"


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"missing baked image: {SOURCE}")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, TARGET)
    if TARGET.stat().st_size != SOURCE.stat().st_size:
        raise SystemExit("copy incomplete: size mismatch")


if __name__ == "__main__":
    main()
