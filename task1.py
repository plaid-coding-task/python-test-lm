# Task 1 — FizzBuzz Filter


def fizzbuzz_filter(numbers):
    """
    Given a list of integers, return a new list where:
      - Multiples of 3 are replaced with the string "Fizz"
      - Multiples of 5 are replaced with the string "Buzz"
      - Multiples of both 3 and 5 are replaced with the string "FizzBuzz"
      - All other integers remain unchanged

    Args:
        numbers (list[int]): A list of integers.

    Returns:
        list: A new list with integers replaced according to the rules above.

    Example:
        fizzbuzz_filter([1, 3, 5, 15, 7]) -> [1, "Fizz", "Buzz", "FizzBuzz", 7]
    """
    # Write your implementation here
    pass


if __name__ == "__main__":
    assert fizzbuzz_filter([1, 2, 3]) == [1, 2, "Fizz"]
    assert fizzbuzz_filter([5, 10, 15]) == ["Buzz", "Buzz", "FizzBuzz"]
    assert fizzbuzz_filter([1, 3, 5, 15, 7]) == [1, "Fizz", "Buzz", "FizzBuzz", 7]
    assert fizzbuzz_filter([]) == []
    assert fizzbuzz_filter([4, 7, 11]) == [4, 7, 11]
    print("All tests passed!")
