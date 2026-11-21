"""字符串工具模块。"""


def truncate(text, max_length, suffix="..."):
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def slugify(text):
    import re
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    text = text.strip("-")
    return text


def count_words(text):
    return len(text.split())


def reverse_words(text):
    words = text.split()
    return " ".join(reversed(words))
