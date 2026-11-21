from string_utils import truncate, slugify, count_words, reverse_words


def test_truncate():
    assert truncate("hello world", 5) == "he..."
    assert truncate("hi", 5) == "hi"


def test_slugify():
    assert slugify("Hello World!") == "hello-world"


def test_count_words():
    assert count_words("one two three") == 3


def test_reverse_words():
    assert reverse_words("a b c") == "c b a"
