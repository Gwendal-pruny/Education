import argparse

parser = argparse.ArgumentParser(description='Ce script fait quelques trucs.')
parser.add_argument("--file", help="Text file to open and read", required=True)
parser.add_argument("--jsonauth", help="JSON Google Authentication file path")

args = parser.parse_args()
