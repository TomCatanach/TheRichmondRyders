import argparse

from schrodingers_python.placeholder import minus_one


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("number", help="The number to minus one from", type=float)
    args = parser.parse_args()
    print(f"{args.number} minus one is {minus_one(args.number)}")
