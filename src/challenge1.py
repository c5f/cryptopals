#!/usr/bin/env python

import sys

from utils import hex_to_base64

def main():
    args = sys.argv

    if len(args) < 2:
        print >>sys.stderr, "Usage: ./challenge1.py <input>"
        sys.exit(1)

    hex_string = args[1]

    print hex_to_base64(hex_string)

    sys.exit(0)

if __name__ == '__main__':
    main()
