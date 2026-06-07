import random
import sympy

def generate(data):

    #f(x) is of form px^2/((c-ax)(d-bx)) where p,a,b,c,d small and \in N
    #generate coefficients
    a = random.randrange(2,5)
    b = random.randrange(2,5)
    c = random.randrange(1,6)
    d = random.randrange(1,6)
    e = random.randrange(1,6)
    f = random.randrange(1,6)
    g = random.randrange(1,6)
    
    #since degree for both is fixed at 2,
    horizontalAsymptote = a/(e*g)

    x = sympy.symbols("x")

    data["params"]["rationalPolynomial"] = sympy.latex((a * x**2 + b * x + c)/(d - e * x)(f - g * x))   
    data["correct_answers"]["ans"] = horizontalAsymptote


