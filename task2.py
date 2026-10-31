# Task 2 — Word Frequency Counter


def word_frequency(sentence):
    """
    Given a string sentence, return a dictionary where:
      - Each key is a unique word from the sentence (case-insensitive, lowercase)
      - Each value is the number of times that word appears

    Punctuation is not a concern — you can assume the input contains
    only letters and spaces.

    Args:
        sentence (str): A string of space-separated words.

    Returns:
        dict: A dictionary mapping each unique word to its frequency.

    Example:
        word_frequency("the cat sat on the mat") ->
            {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}
    """
    # Write your implementation here
    pass


if __name__ == "__main__":
    assert word_frequency("the cat sat on the mat") == {
        "the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1
    }
    assert word_frequency("hello hello hello") == {"hello": 3}
    assert word_frequency("Hello hello HELLO") == {"hello": 3}
    assert word_frequency("one two three") == {"one": 1, "two": 1, "three": 1}
    assert word_frequency("") == {}
    print("All tests passed!")
