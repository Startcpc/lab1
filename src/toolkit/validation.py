def validation(tokens: list[str]) -> list[str]:
    """Проверяет правильность выражения"""
    valid: list[str] = []
    expect = True
    operations = ['+', '-', '*', '/']

    for token in tokens:
        if token in operations:
            if expect:
                if valid and valid[-1] in operations:
                    raise ValueError('Два бинарных оператора подряд')
                raise ValueError('Пропущенный операнд')
            valid.append(token)
            expect = True
            continue
        number = token.lstrip('+-')
        if len(number) > 1 and number[0] == "0" and number[1].isdigit():
            raise ValueError("Неверное числовое значение")
        if not all(char in '0123456789.' for char in number):
            raise ValueError('Недопустимый символ')
        if (number.count('.') > 1 or number.startswith('.') or number.endswith('.')):
            raise ValueError('Неверное числовое значение')
        if not expect:
            raise ValueError('Пропущенный операнд')
        valid.append(token)
        expect = False
    if expect:
        raise ValueError('Пропущенный операнд')
    return valid
