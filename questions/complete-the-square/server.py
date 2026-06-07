import random

def generate(data):
    # form is (x-a)^2 = b^2
    # displayed form is x^2 + 2ax = b^2-a^2
    a = random.randrange(1,13)
    b = random.randrange(1,13)

    # case where a = b is too easy!
    while a == b:
        b = random.randrange(1,13)
    
    rhs = b**2 - a**2
    coeff = 2*a
    data["params"]["rhs"] = rhs
    data["params"]["coeff"] = coeff

    #user will enter smaller solution first, then larger solution.
    r1 = min(a-b,a+b)
    r2 = max(a-b,a+b)
    data["correct_answers"]["r1"] = r1
    data["correct_answers"]["r2"] = r2




