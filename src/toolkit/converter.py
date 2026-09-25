def convert(value: str | int | float, src: str, dst: str) -> float:
    """Конвертирует значение из одной единицы измерения в другую."""
    length = ["mm", "cm", "m", "km"]
    mass = ["g", "kg"]
    temperature = ["c", "f", "k"]

    src = src.lower()
    dst = dst.lower()

    if src in length and dst in length:
        group = "length"
    elif src in mass and dst in mass:
        group = "mass"
    elif src in temperature and dst in temperature:
        group = "temperature"
    else:
        raise ValueError("НЕСОВМЕСТИМЫЕ ЕДИНИЦЫ")

    if group == "length":
        k = {
            "mm": 0.001,
            "cm": 0.01,
            "m": 1,
            "km": 1000,
        }

        return float(value) * k[src] / k[dst]

    if group == "mass":
        k = {
            "g": 1,
            "kg": 1000,
        }

        return float(value) * k[src] / k[dst]

    if src == "c":
        celsia = float(value)
    elif src == "f":
        celsia = (float(value) - 32) * 5 / 9
    else:
        celsia = float(value) - 273.15

    if celsia < -273.15:
        raise ValueError("Температура слишком низкаяяяяяяяя - неееееееет!")

    if dst == "c":
        return celsia

    if dst == "f":
        return celsia * 9 / 5 + 32

    return celsia + 273.15
