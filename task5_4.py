src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def greater_gen():
    prev = src[0]
    for i in src[1:]:
        if i > prev:
            yield i
        prev = i


result = [r for r in greater_gen()]
print(result)