str_1 = '111 111'
str_2 = '111 '
str_3 = ' 111'
str_4 = '111'
str_5 = ' '
str_6 = '  '
str_7 = ' 11 111'
str_8 = ' 11 11 '
str_9 = '111 11 '
str_10 = ' 111111'


def string_check(arg, length=7, element=2):
    sign = (len(arg) >= length) * \
           (len(arg.split(" ")) == element) * \
           (not arg.startswith(' ')) * \
           (not arg.endswith(' '))
    print(f"{sign= }")
    print(f"{arg= }")
    print(f"{len(arg)= }")
    print(f"{len(arg.split(' '))= }")
    print(f"{arg.startswith(' ')= }")
    print(f"{arg.endswith(' ')= }")
    print(55 * '-')


if __name__ == '__main__':
    string_check(str_1)
    string_check(str_2)
    string_check(str_3)
    string_check(str_4)
    string_check(str_5)
    string_check(str_6)
    string_check(str_7)
    string_check(str_8)
    string_check(str_9)
    string_check(str_10)

# s = {1, 2, 3, 4, }
# print(*s,)
#
# print(f"{s=}")
#
# a = [0, 1, 2, 3]
# for a[-1] in a:
#     print(a[-1])
# ****************************************************************************************
# a = [0, 1, 2, 3]
# for i in range(len(a)):
#     a[-1] = a[i]  # update last element of list(updated) with element at i'th position
#     print(a[-1])  # print last element of list
# ****************************************************************************************
# a = int(input("Возраст: "))
# v1, v2, v3, v4 = a <= 13, 14 <= a <= 24, 25 <= a <= 59, 60 <= a
# print(v1 * 'детство' + v2 * 'молодость' + v3 * 'зрелость' + v4 * 'старость')
# ****************************************************************************************
# from datetime import datetime
#
# deadline = datetime.strptime("1970-02-02", "%Y-%m-%d")
# print(deadline)
# ****************************************************************************************
# from datetime import date, time, datetime
#
# the_date = date.fromisoformat('1970-02-02')
# print(the_date)
# print(type(the_date))
# the_time = time.fromisoformat("21:15")
# print(the_time)
# print(type(the_time))
# the_datetime = datetime.fromisoformat("1970-02-02 21:10")
# print(the_datetime)
# print(type(the_datetime))
# ****************************************************************************************
#
# dict = {"A" : 1, "B": 2, "C": 3, "D": 4}
# print(max(list(dict.values())))
