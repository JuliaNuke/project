def type_logger(func):
    def logging_wrapper(*argc, **argv):
        for x in argc:
            print(type(x))
        return func(*argc, **argv)
    return logging_wrapper

@type_logger
def cube(x):
    return x**3

print(cube(3.0))
print(cube(5))