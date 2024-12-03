from typing import List, Tuple
from datetime import timedelta
import time

def get_lists_from_input() -> Tuple[List[int], List[int]]:
    left: List[int] = []
    right: List[int] = []

    with open("input", "r") as f:
        for line in f:
            numbers = line.split("   ")

            left.append(int(numbers[0]))
            right.append(int(numbers[1]))

    return left, right


def calculate_difference(left_list: List[int], right_list: List[int]) -> int:
    left_list.sort()
    right_list.sort()

    difference = 0

    for i in range(len(left_list)):
        difference += abs(left_list[i] - right_list[i])

    return difference


def calculate_similarity(left_list: List[int], right_list: List[int]) -> int:
    left_list.sort()
    right_list.sort()

    similarity = 0

    for i in range(len(left_list)):
        similarity += left_list[i] * right_list.count(left_list[i])

    return similarity


if __name__ == "__main__":
    left, right = get_lists_from_input()
    start_time = time.monotonic()
    print(calculate_difference(left, right))
    split_time = time.monotonic()
    print(calculate_similarity(left, right))
    end_time = time.monotonic()

    print(
        f"calculate_difference: {timedelta(seconds=split_time - start_time)}, calculate_similarity: {timedelta(seconds=end_time - split_time)}")
