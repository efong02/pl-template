import random
import sympy

def generate(data):

    #f(x) = (ax^k + bx + c)/(d - ex)(f - ghx)(1-x)**j
    a = random.randrange(2,10)
    b = random.randrange(2,5)
    c = random.randrange(1,6)
    d = random.randrange(1,6)
    e = random.randrange(1,6)
    f = random.randrange(1,6)
    g = random.randrange(1,6)
    h = random.choice([1, -1])
    j = random.choice([0,1])
    k = random.choice([1,2,3,4])
    
    
    x = sympy.symbols("x")
    f = (a * x**k + b * x + c)/((d - e * x)*(f - h * g * x)*(1-x)**j)

    data["params"]["rationalPolynomial"] = sympy.latex(f) 

    data["correct_answers"]["positiveLimit"] = str(sympy.limit(f, x, sympy.oo))
    data["correct_answers"]["negativeLimit"] = str(sympy.limit(f, x, -sympy.oo))


