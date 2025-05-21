#!/usr/bin/env python3
# Created by: Reid MacLean
# Created on: May 2025
# This program calculates the average of 10 random numbers between 1 and 100 in a list


import random


def calculate_average(numbers):
    # This function calculates the average of a list of numbers
    return sum(numbers) / len(numbers)


def main():
    # This function generates 10 random numbers and calculates their average
    numbers = [random.randint(1, 100) for _ in range(10)]
    average = calculate_average(numbers)
    print(f"The average of the numbers {numbers} is: {average}")


if __name__ == "__main__":
    main()
