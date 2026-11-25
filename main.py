#!/usr/bin/env python3
"""Write one short, funny rant to /output/entry.txt.

The rant is about the self-checkout machine: one cucumber, one accusation.
"""

RANT = (
    "Self-checkout has decided I am a thief. I scanned ONE cucumber, "
    "put it in the bag, and the machine screamed "
    "'UNEXPECTED ITEM IN THE BAGGING AREA' like I had smuggled in a grand piano. "
    "Then it froze, called for assistance, and a teenager strolled over, "
    "pressed one button, and walked off like he had just defused a bomb. "
    "I paid full price to be publicly accused by a scale."
)


def main() -> None:
    text = RANT.strip()
    assert 1 <= len(text) <= 400, f"rant is {len(text)} chars, must be 1-400"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
