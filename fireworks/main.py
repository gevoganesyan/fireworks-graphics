import argparse
from game import Game


def args_parsing():
    parser = argparse.ArgumentParser(description="Let`s some fun :)")

    parser.add_argument(
        "-s", "--sparks-amount-range", type=str, default='20-30'
    )

    arguments = parser.parse_args()

    sparks_range = arguments.sparks_amount_range.split('-')
    sparks_amount_range = tuple(map(int, sparks_range))

    return sparks_amount_range


if __name__ == '__main__':
    sparks = args_parsing()
    application = Game(sparks)
    application.run()

