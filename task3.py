# Task 3 — Flatten Nested List


def flatten(nested):
    """
    Given a list that may contain nested lists at any depth, return a single
    flat list containing all the values in their original left-to-right order.

    Args:
        nested (list): A list that may contain integers or further nested lists.

    Returns:
        list: A flat list of all values.

    Example:
        flatten([1, [2, 3], [4, [5, 6]]]) -> [1, 2, 3, 4, 5, 6]
    """
    # Write your implementation here
    pass


if __name__ == "__main__":
    assert flatten([1, 2, 3]) == [1, 2, 3]
    assert flatten([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]
    assert flatten([[1, [2]], [3, [4, [5]]]]) == [1, 2, 3, 4, 5]
    assert flatten([]) == []
    assert flatten([[[1]], [[2]], [[3]]]) == [1, 2, 3]
    print("All tests passed!")
