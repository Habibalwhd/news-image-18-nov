"""Write the 18 November 2026 world-news image to the output directory.

The image is held in this repository as entry.png; this program simply
copies it to $MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png when
the variable is unset). Standard library only, no network.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    # Guard the competition's 1 MiB cap: refuse to leave an oversize file.
    if target.stat().st_size > 1_048_576:
        target.unlink()
        raise SystemExit("entry.png exceeds the 1 MiB limit")


if __name__ == "__main__":
    main()
