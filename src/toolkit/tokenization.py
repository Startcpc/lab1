import re


def tokenization(task: str) -> list[str]:
    """Разделяет выражение на токены"""
    clean = "".join(task.split())
    return re.findall(r"(?<![\w.])[+-]?(?:\d+(?:\.\d*)?|\.\d+)|[*/]|[+-]|[^\s]", clean)
