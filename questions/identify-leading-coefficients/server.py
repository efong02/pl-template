import random
import sympy

def generate(data):

    # f(x) = (ax^2 + bx + c)/(d - ex)(f - ghx)
    # generate coefficients and constats
    a = random.randrange(2,10)
    b = random.randrange(2,5)
    c = random.randrange(1,6)
    d = random.randrange(1,6)
    e = random.randrange(1,6)
    f = random.randrange(1,6)
    g = random.randrange(1,6)
    h = random.choice([1, -1])


    x = sympy.symbols("x")

    data["params"]["rationalPolynomial"] = sympy.latex((a * x**2 + b * x + c)/((d - e * x)*(f - h * g * x)))  

    data["correct_answers"]["numCoeff"] = a
    data["correct_answers"]["denomCoeff"] = e*g*h


