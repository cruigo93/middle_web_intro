"""Генератор приветствий."""
import pprint


def Greeting(name: str) -> str:
    """Возвращает текст приветствия.

    Args:
        name: Имя пользователя

    Returns:
        str: Текст приветствия
    """
    new_name = " ".join([n[0].upper() + n[1:] for n in name.split()])
    # pprint.pprint(name.lower())
    return f"Привет, {new_name}"
