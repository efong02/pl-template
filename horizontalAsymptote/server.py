import random

def generate(data):

    #f(x) is of form px^2/((c-ax)(d-bx)) where p,a,b,c,d small and \in N
    #generate coefficients
    a = random.randrange(1,4)
    b = random.randrange(1,4)
    c = random.randrange(1,6)
    d = random.randrange(1,6)
    p = random.randrange(1,10)

    #since degree for both is fixed at 2,
    horizontalAsymptote = p/(c*d)


    data["params"]["a"] = a
    data["params"]["b"] = b
    data["params"]["c"] = c
    data["params"]["d"] = d
    data["params"]["p"] = p
    data["correct_answers"]["ans"] = horizontalAsymptote



