#!/usr/bin/env python
# Backend Test Driven Development - Creating a cmd line tool
__author__ = 'Bschue'

import argparse


def parse():
    parser = argparse.ArgumentParser(
        description='Perform transformation on input text')
    parser.add_argument(
        '-u', '--upper', help='convert text to uppercase', action='store_true')
    parser.add_argument(
        '-l', '--lower', help='convert text to lowercase', action='store_true')
    parser.add_argument(
        '-t', '--title', help='convert text to titlecase', action='store_true')
    parser.add_argument('text', help='text to be manipulated')
    return parser


def main():
    parsed = parse().parse_args()
    if parsed.upper:
        print(parsed.text.upper())
    if parsed.lower:
        print(parsed.text.lower())
    if parsed.title:
        print(parsed.text.title())


if __name__ == "__main__":
    main()
