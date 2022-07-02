import math

def validator_checker(validator):
    def _validator(func):
        def wrapper(*argc, **argv):
            if not validator(*argc):
                raise ValueError("Incorrect argument")
            return func(*argc, **argv)
        return wrapper
    return _validator

@validator_checker(lambda x: x>0)
def logarithm(x):
    return math.log(x)

print('ln(10) = ', logarithm(9))
print('ln(-1) = ', logarithm(-1))