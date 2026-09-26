from operator import add, sub, mul, truediv


def calculation(tokens: list[str]) -> float:
    """Вычисляет значение проверенного выражения"""
    operations = {"+": add, "-": sub, "*": mul, "/": truediv}
    total = 0.0
    curr = float(tokens[0])
    for i in range(1, len(tokens), 2):
        op = tokens[i]
        value = float(tokens[i + 1])
        if op in "+-":
            total = add(total, curr)
            curr = operations[op](0.0, value)
        else:
            if op == "/" and value == 0:
                raise ZeroDivisionError("НЕЛЬЗЯ ДЕЛИТЬ НА 0")
            curr = operations[op](curr, value)
    return add(total, curr)
