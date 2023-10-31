import argparse

parser = argparse.ArgumentParser(description='Process some input.')
parser.add_argument('input', metavar='I', type=str, help='an input string')

args = parser.parse_args()
print(args.input)