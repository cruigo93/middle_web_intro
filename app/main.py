"""Генератор приветствий."""


def greeting(name: str) -> str:
    """Возвращает текст приветствия.

    Args:
        name: Имя пользователя

    Returns:
        str: Текст приветствия
    """
    new_name = ' '.join([
        split_name.capitalize() for split_name in name.split()
    ])
    return 'Привет, {new_name}'.format(new_name=new_name)
