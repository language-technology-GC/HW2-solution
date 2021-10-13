#!/usr/bin/env python
"""Prepares the Icelandic data for preprocessing."""

import contextlib
import csv


# I have chosen to hard-code the paths here since what else would I do?

TRAIN = "ice_train.tsv"
TRAIN_G = "train.ice.g"
TRAIN_P = "train.ice.p"

DEV = "ice_dev.tsv"
DEV_G = "dev.ice.g"
DEV_P = "dev.ice.p"

TEST = "ice_test.tsv"
TEST_G = "test.ice.g"
TEST_P = "test.ice.p"


def main() -> None:
    # TODO: I could probably reuse some of the training data code for the
    # development and test data if I was so inclined.
    # Processes training data.
    with contextlib.ExitStack() as stack:
        source = csv.reader(
            stack.enter_context(open(TRAIN, "r")), delimiter="\t"
        )
        g = stack.enter_context(open(TRAIN_G, "w"))
        p = stack.enter_context(open(TRAIN_P, "w"))
        for graphemes, phones in source:
            print(" ".join(graphemes), file=g)
            print(phones, file=p)
    # Processes development data.
    with contextlib.ExitStack() as stack:
        source = csv.reader(
            stack.enter_context(open(DEV, "r")), delimiter="\t"
        )
        g = stack.enter_context(open(DEV_G, "w"))
        p = stack.enter_context(open(DEV_P, "w"))
        for graphemes, phones in source:
            print(" ".join(graphemes), file=g)
            print(phones, file=p)
    # Processes test data.
    with contextlib.ExitStack() as stack:
        source = csv.reader(
            stack.enter_context(open(TEST, "r")), delimiter="\t"
        )
        g = stack.enter_context(open(TEST_G, "w"))
        p = stack.enter_context(open(TEST_P, "w"))
        for graphemes, phones in source:
            print(" ".join(graphemes), file=g)
            print(phones, file=p)


if __name__ == "__main__":
    main()
