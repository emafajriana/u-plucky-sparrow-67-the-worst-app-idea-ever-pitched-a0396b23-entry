"""The Worst App Idea Ever Pitched — entry writer.

Writes one sentence to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt):
the pitch for MuteButton, an app that listens to your meetings and mutes
you automatically — including the parts where you were supposed to speak.
"""

import os
from pathlib import Path

ENTRY = (
    "MuteButton listens to your meetings and mutes you automatically — "
    "including the parts where you were supposed to speak — so you can "
    "finally attend every call in total, blissful silence, for just "
    "$4.99 a month."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 240, "entry must be 1-240 characters"
    assert ENTRY.strip() == ENTRY, "entry must not have stray whitespace"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    # Read-back gate: the bytes on disk must be exactly the pitch's UTF-8
    # encoding — a text-level comparison would hide a stray BOM or a
    # newline the grader's byte counter would still see.
    written = target.read_bytes()
    assert written == ENTRY.encode("utf-8"), "entry.txt bytes do not match the pitch"
    assert written.count(b"\n") == 0, "entry must be exactly one sentence on one line"
    print(f"wrote {len(ENTRY)} chars to {target}")


if __name__ == "__main__":
    main()
