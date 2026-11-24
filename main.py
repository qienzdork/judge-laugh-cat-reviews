import os

REVIEW = (
    "One star. He bought a $400 cat tree, then works from the bed "
    "I already claimed. The help is unreliable and the lap is taken."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
