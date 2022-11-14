import json
from random import choice

morse_code = json.load(open(r'C:\Users\dynee\Notebooks\#Skypro PD 16\MOD1 1. Введение в '
                            r'программирование\morse-code.json'))

word_list = ['snake', 'rainbow', 'twin', 'fish', 'moon']


def morse_encode(wrd):
    """
    функция для кодировки английских слов (и фраз) в азбуку Морзе
    """
    return ' '.join([morse_code[l.lower()] if l != ' ' else ' ' for l in str(wrd)])


# шпаргалка #

for word in word_list:
    print(word, morse_encode(word))


def morse_encode(wrd):
    """
    функция для кодировки английских слов (и фраз) в азбуку Морзе
    """
    return ' '.join([morse_code[l.lower()] if l != ' ' else ' ' for l in str(wrd)])


def get_word():
    """
    функция для выбора случайного слова из списка ___word_list___
    """
    return choice(word_list)


def print_statistics(nswrs):
    """
    функция для печати статистики ответов из списка __answers__
    """
    print(f'Всего задачек: {len(nswrs)}')
    print(f'Отвечено верно: {nswrs.count(1)}')
    print(f'Отвечено неверно: {nswrs.count(0)}')
    print(f'\nЭто фиаско, братан...') if not nswrs.count(1) else ''
    print(f'\nHello, Mr. Samuel Finley Breese Morse! Welcome!') if not nswrs.count(0) else ''


*trtn, = range(5)
input('Сегодня мы потренируемся расшифровывать азбуку Морзе\nНажмите Enter и начнем\n')
answers = []
for i in trtn:
    word_to_code = get_word()
    code_of_word = morse_encode(word_to_code)
    user_try = input(f'Слово {i + 1} {code_of_word}   ')
    if user_try == word_to_code:
        print(f'Верно!\n')
        answers.append(True)
    else:
        print(f'Неверно! Это {word_to_code}\n')
        answers.append(False)
print_statistics(answers)
