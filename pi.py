import random


def pi(n):
    daire_say = 0
    toplam_say = 0
    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x ** 2 + y ** 2 <= 1:
            daire_say += 1
        toplam_say += 1

    print(4 * daire_say / toplam_say)


n = input('n:\n')
pi(int(n))