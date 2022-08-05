"""Генератор приветствий."""


def greeting(name: str) -> str:
    """Возвращает текст приветствия.

    Args:
        name: Имя пользователя

    Returns:
        str: Текст приветствия
    """
    new_name = ' '.join([n_[0].upper() + n_[1:]
                        for n_ in name.split()])
    return 'Привет, ' + new_name
