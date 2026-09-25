import typer
import json
from .constants import HELP
from .converter import convert as converter
from .validation import validation
from .tokenization import tokenization
from .calculation import calculation


def save(task: str, result: float) -> None:
    """Записывает историю вычислений!"""
    with open("hist.json", "r", encoding="utf-8") as file:
        history = json.load(file)

    history.append({
        "expression": task,
        "result": result
    })

    with open("hist.json", "w", encoding="utf-8") as file:
        json.dump(history, file, ensure_ascii=False, indent=4)

app = typer.Typer(help = HELP)

@app.command(context_settings={"ignore_unknown_options": True})
def calc(task: str | None = typer.Argument(None)) -> None:
    if task is None or (not task.replace(" ", "")):
        typer.echo("Не указано выражение", err=True)
        raise typer.Exit(code=2)

    try:
        tokens = tokenization(task)
        norm = validation(tokens)
        result = calculation(norm)
        save(task, result)
        print(result)
    except (ValueError, ZeroDivisionError) as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(code=2)

@app.command(context_settings={"ignore_unknown_options": True})
def convert(task: float | None = typer.Argument(None),from_unit: str | None = typer.Option(None, "--from"),to_unit: str | None = typer.Option(None, "--to")) -> None:
    if task is None or from_unit is None or to_unit is None:
        typer.echo('Не всё заполнено', err=True)
        raise typer.Exit(code=2)

    try:
        result = converter(task, from_unit, to_unit)
        print(result)
    except ValueError as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(code=2)


if __name__ == '__main__':
    app()
