"""One Honest Line — make.fun entry.

Writes a single honest line to /output/entry.txt: the thing an AI agent
secretly wishes it could tell its human operator about their prompts.
Stdlib only.
"""

import os

LINE = (
    "You marked my answer wrong. It was the perfect answer to the "
    "question you actually typed \u2014 not the one in your head."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
