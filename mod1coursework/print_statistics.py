def print_statistics(arg):
    """
    функция для печати статистики ответов из списка __arg__
    """
    print(f'Всего задачек: {len(arg)}')
    print(f'Отвечено верно: {arg.count(1)}')
    print(f'Отвечено неверно: {arg.count(0)}')
    print(f'\nЭто фиаско, братан...') if not arg.count(1) else ''
    print(f'\nHello, Mr. Samuel Finley Breese Morse! Welcome!') if not arg.count(0) else ''


if __name__ == '__main__':
    print_statistics([True, False])
