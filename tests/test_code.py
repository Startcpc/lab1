from toolkit.tokenization import tokenization
from toolkit.validation import validation
from toolkit.converter import convert
from toolkit.calculation import calculation
import pytest


def test_tokenization_simple_expression() -> None:
    """токенизирует простое выражение"""
    res = tokenization('5-1')
    assert res == ['5', '-', '1']


def test_tokenization_unary_operators() -> None:
    """токенизирует унарные операторы"""
    res = tokenization('2*          5 / 2 -- 1 ++ 676767')
    assert res == ['2', '*', '5', '/', '2', '-', '-1', '+', '+676767']


def test_validation_correct_expression() -> None:
    """проверяет правильное выражение"""
    res = validation(tokenization('5+1'))
    assert res == ['5', '+', '1']


def test_validation_double_binary_operator() -> None:
    """проверяет два оператора подряд"""
    with pytest.raises(ValueError) as errornik:
        validation(tokenization('5---1'))
    assert str(errornik.value) == 'Два бинарных оператора подряд'


def test_validation_missing_operand() -> None:
    """проверяет пропущенный операнд"""
    with pytest.raises(ValueError) as errornik:
        validation(tokenization('*2+2'))
    assert str(errornik.value) == 'Пропущенный операнд'


def test_validation_invalid_character() -> None:
    """проверяет недопустимый символ"""
    with pytest.raises(ValueError) as errornik:
        validation(tokenization('2+a'))
    assert str(errornik.value) == 'Недопустимый символ'


def test_validation_invalid_number() -> None:
    """проверяет неверное число"""
    with pytest.raises(ValueError) as errornik:
        validation(tokenization('5..2'))
    assert str(errornik.value) == 'Неверное числовое значение'


def test_validation_number_without_left_part() -> None:
    """проверяет точку в начале"""
    with pytest.raises(ValueError) as errornik:
        validation(tokenization('.5'))
    assert str(errornik.value) == 'Неверное числовое значение'


def test_validation_number_without_right_part() -> None:
    """проверяет точку в конце"""
    with pytest.raises(ValueError) as errornik:
        validation(tokenization('5.'))
    assert str(errornik.value) == 'Неверное числовое значение'


def test_validation_leading_zero() -> None:
    """проверяет ведущий ноль"""
    with pytest.raises(ValueError) as errornik:
        validation(tokenization('025'))
    assert str(errornik.value) == 'Неверное числовое значение'


def test_canculation_simple_expression() -> None:
    res = calculation(validation(tokenization('5-1')))
    assert res == 4.0


def test_converter_simple_task() -> None:
    """Конвертирует простое значение"""
    res = convert('2500', 'cM', 'M')
    assert res == 25.0


def test_converter_error() -> None:
    """Проверяет на несовместимые единицы"""
    with pytest.raises(ValueError) as errornik:
        convert('2500', 'CM', 'kdl')
    assert str(errornik.value) == "НЕСОВМЕСТИМЫЕ ЕДИНИЦЫ"
