#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]     # Skip the script name
    total = 0
    for arg in args:
        total += int(arg)
    print(total)
