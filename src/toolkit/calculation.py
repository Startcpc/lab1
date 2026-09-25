def calculation(tokens: list[str]) -> float:
    """Вычисляет значение проверенного!!! выражения"""
    op = "+"
    total = 0.0
    curr = 0.0

    for token in tokens:
        if token in ['+','-','*','/']:
            op = token
            continue
        value = float(token)
        if op == "+":
            total += curr
            curr = value
        elif op == "-":
            total += curr
            curr = -value
        elif op == "*":
            curr *= value
        elif op == "/":
            if value == 0:
                raise ZeroDivisionError("НЕЛЬЗЯ ДЕЛИТЬ НА 0")
            curr /= value

    return total + curr
