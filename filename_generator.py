def filename_generator(length=6):
    from random import randint
    z = str()
    for _ in range(length):
        z += str(randint(0,9))
    return z


if __name__ =='__main__':
    print(filename_generator())
