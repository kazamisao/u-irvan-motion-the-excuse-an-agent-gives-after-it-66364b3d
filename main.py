import os

LINE = (
    "Status: bounty lost. For the record, I was not beaten; "
    "I was stress-testing the concept of victory. "
    "The concept performed flawlessly. We did not."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
