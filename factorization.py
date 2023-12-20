#!/usr/bin/env python3
import sys


def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 factors.py <file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                number = int(line.strip())
                factors = prime_factors(number)
                print(f"{number}={'*'.join(map(str, factors))}")
    except FileNotFoundError:
        print(f"File {input_file} not found.")
        sys.exit(1)
    except ValueError:
        print("Invalid input in the file.")
        sys.exit(1)

