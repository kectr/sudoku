def twod_listcreat(x, defaultvalue=None, y=0):
    if defaultvalue is not None and y != 0:
        return [[defaultvalue for _ in range(y)] for _ in range(x)]
    else:
        return [[] for _ in range(x)]


def threed_listcreat(x, y, defaultvalue=None, z=0):
    if defaultvalue is not None and z != 0:
        return [[[defaultvalue for _ in range(z)] for _ in range(y)] for _ in range(z)]
    else:
        return [[[] for _ in range(y)] for _ in range(x)]


def oned_idcheck(lista, listb):
    if len(lista) != len(listb):
        print('Not equal lenght')
        return False
    elif id(lista) == id(listb):
        print('Same list for lista and listb')
        return False
    else:
        return True


def twod_idcheck(lista, listb):
    if not oned_idcheck(lista, listb):
        return False
    else:
        for x in range(len(lista)):
            if id(lista[x]) == id(listb[x]):
                return False
        return True


def threed_idcheck(lista, listb):
    if not twod_idcheck(lista, listb):
        return False
    else:
        for x in range(len(lista)):
            for y in range(len(lista[x])):
                if id(lista[x][y]) == id(listb[x][y]):
                    print(id(lista[x][y]), id(listb[x][y]))
                    print(lista[x][y], listb[x][y])
                    print(x, y)
                    return False
        return True


def twod_copy(listwillcopy):
    templist = []
    for x in listwillcopy:
        templist.append(x.copy())
    return templist


def threed_copy(listwillcopy):
    templist = []
    for x in listwillcopy:
        templist.append(twod_copy(x))
    return templist
