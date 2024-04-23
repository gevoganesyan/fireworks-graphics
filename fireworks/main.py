import argparse
from game import Game


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-s", "--sparks-amount-range", action="store_true", help=""
    )
    arguments = parser.parse_args()
    return arguments

if __name__ == '__main__':
    application = Game()
    application.run()
    main()
