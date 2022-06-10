src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def gen_uniq(itr):
    tmp = dict()
    for x in itr:
        count = tmp.get(x, 0)
        tmp[x] = count + 1
    return (k for k in tmp.keys() if tmp[k] == 1)


print([x for x in gen_uniq(src)])