#!/usr/bin/env python3

from typing import List
import re

# Approach: For each password, iterate over password and check count at each step
# Time Complexity: O(n * k), where n = # of passwords and k = length of passwords
# Assumption: All inputs in valid format

TEST_CASES = [
    (['1-3 a: abcde'], 1),
    (['1-3 b: cdefg'], 0),
    (['2-9 c: ccccccccc'], 0),
]

RE_PARSE = re.compile(r"^(\d+)-(\d+) ([a-z]): ([a-z]+)$")

def is_password_valid(pos1: int, pos2: int, char: str, password: str) -> bool:
    total  = 1 if password[pos1 - 1] == char else 0
    total += 1 if password[pos2 - 1] == char else 0
    return total == 1

def count_valid_passwords(passwords: List[str]) -> int:
    num_valid_passwords = 0
    for policy_and_password in passwords:
        match = RE_PARSE.fullmatch(policy_and_password)
        if not match:
            continue
        pos1 = int(match.group(1))
        pos2 = int(match.group(2))
        char = match.group(3)
        password = match.group(4)
        if is_password_valid(pos1, pos2, char, password):
            num_valid_passwords += 1
        
    return num_valid_passwords

def run_tests():
    for input, expected_output in TEST_CASES:
        actual_output = count_valid_passwords(input)
        if actual_output == expected_output:
            print("Test passed for input: " + str(input))
        else:
            print("Test failed for input: " + str(input))
            print("\tExpected output: " + str(expected_output))
            print("\tActual output: " + str(actual_output))

run_tests()

def read_input(filename):
    passwords = []
    with open(filename) as f:
        for line in f:
            passwords.append(line.strip())
    return passwords

input = read_input("day02-input.txt")
print(count_valid_passwords(input))
# 747
