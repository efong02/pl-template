import random

def generate(data):
    # displayed form is x^2 + 2ax = b^2-a^2
    # this is so that the numbers are nice, whole numbers.
    a = random.randrange(1,13)
    b = random.randrange(1,13)

    # case where a = b is too easy!
    while a == b:
        b = random.randrange(1,13)
    
    rhs = b**2 - a**2
    coeff = 2*a
    data["params"]["rhs"] = rhs
    data["params"]["coeff"] = coeff
    data["params"]["a"] = a

    data["correct_answers"]["addend"] = a**2




