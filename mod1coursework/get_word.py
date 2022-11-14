from random import choice


def get_word(arg):
    """
    функция для выбора случайного слова из списка ___arg___
    """
    return choice(arg)

if __name__ == '__main__':
    print(get_word(['1st', '2nd']))
