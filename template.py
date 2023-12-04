# template.py

import sys, re, statistics, heapq
from collections import defaultdict, Counter, deque
from itertools import permutations, product, combinations

# 1. Copy the input from https://adventofcode.com/{year}/day/{day}/input to a file in same dir called d{day}.txt
# 2. Use snippet `aoc` to create function and solve puzzle
# 3. Run `python main.py {day:int} {part:int}` to get results


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py {day:int} {part:int}")
        sys.exit(1)

    day = sys.argv[1]
    part = sys.argv[2]

    try:
        # Try to get the function by name
        function_name = f"d{day}_{part}"
        function_to_run = globals()[function_name]


        # Read content from a file with the same name as the function
        file_name = f"d{day}.txt"
        try:
            with open(file_name, 'r') as file:
                lines = list(map(str.strip, file.readlines()))

                # Run the function
                function_to_run(lines)
        except FileNotFoundError:
            print(f"File {file_name} not found.")

    except KeyError:
        print(f"Function {function_name} not found.")
        sys.exit(1)
