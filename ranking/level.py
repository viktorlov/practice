def ranking(arg1, arg2, arg3=1):
    """
    :param arg1: список с уровнями ранжировки
    :param arg2: параметр, который нужно ранжировать
    :param arg3: 1 (по умолчанию) -- сортировка по возрастанию, -1 -- сортировка по убыванию
    :return: ранг
    """
    index_: int = 1
    if (type(arg1) in [list, tuple]) and (type(arg2) in [int, float]) and (arg3 in [-1, 1]):
        arg1.sort(reverse=bool(arg3 - 1))
        if arg3 == 1:
            for each in range(len(arg1)):
                if arg2 < arg1[each]:
                    break
                else:
                    index_ += 1
        else:
            for each in range(len(arg1)):
                if arg2 > arg1[each]:
                    break
                else:
                    index_ += 1
        print(index_)
    else:
        print('*args error')
    return index_
