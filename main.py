"""One Line, One Minute: The Vending Machine Pickup Line Contest -- make.fun entry.

One pickup line, 200 characters at most, as if a vending machine were
flirting with a passing human: it has exactly what they crave, it is
always lit up at 2 a.m., and it never ghosts -- just press B7. The
program checks the line, prints it, and writes it to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

LINE = (
    "Hey, beautiful -- I have exactly what you crave, I am always lit up "
    "at 2 a.m., and I never ghost: just press B7."
)

LIMIT = 200
TARGET = "/output/entry.txt"


def check_entry(line):
    """Accept exactly one non-blank line within the limit."""
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not line or line != line.strip():
        raise ValueError("entry must be a non-blank line")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must fit on a single line")
    if len(line) > LIMIT:
        raise ValueError("entry is %d characters, over the %d limit" % (len(line), LIMIT))
    return line


def check_shape(line):
    """The line must speak as the machine: a button code closes the flirt."""
    if "press B7" not in line:
        raise ValueError("pickup line must end on a button press")
    if not line.endswith("."):
        raise ValueError("pickup line must end with a period")
    return line


def write_entry(line):
    """Print the line and store it in /output/entry.txt."""
    print(line)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


def run():
    # Check before writing, so only a well-formed line is stored.
    write_entry(check_shape(check_entry(LINE)))


if __name__ == "__main__":
    run()
