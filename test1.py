"""
1. Implement the unique_names method. When passed two lists of names, it will return a list containing the names
that appear in either or both lists. The returned list should have no duplicates.  For example,
calling unique_names(['Ava', 'Emma', 'Olivia'], ['Olivia', 'Sophia', 'Emma']) should return a list containing Ava,
Emma, Olivia, and Sophia in ascending order. 
"""


def unique_names(names_1: list, names_2: list) -> list:
    """Возвращает имена полявляющиеся в обоих списках без дубликатов."""

    return sorted(list(set(names_1 + names_2)))


if __name__ == '__main__':
    a, b = ['Ava', 'Emma', 'Olivia'], ['Olivia', 'Sophia', 'Emma']
    print(unique_names(a, b))
