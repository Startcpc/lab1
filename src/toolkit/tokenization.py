def tokenization(task: str) -> list[str]:
    """Разделяет выражение на числа и арифметические операторы, учитывая унарные знаки."""
    clean = task.replace(' ', '')
    tokens = []
    number = ''

    for char in clean:
        if char in '+-':
            if number:
                tokens.append(number)
                number = ''
            if (not tokens) or tokens[-1] in ['+', '-', '*', '/']:
                number = char
            else:
                tokens.append(char)
        elif char in '*/':
            if number:
                tokens.append(number)
                number = ''
            tokens.append(char)
        else:
            number += char
    if number:
        tokens.append(number)
    return tokens
