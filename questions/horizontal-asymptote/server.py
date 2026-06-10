import random
import sympy

def generate(data):

    # f(x) = (ax^2 + bx + c)/(d - ex)(f - ghx)
    a = random.randrange(2,10)
    b = random.randrange(2,5)
    c = random.randrange(1,6)
    d = random.randrange(1,6)
    e = random.randrange(1,6)
    f = random.randrange(1,6)
    g = random.randrange(1,6)
    h = random.choice([1, -1])
    
    # since degree for both is fixed at 2, only the leading coefficients matter for horizontal asymptote
    # this question focuses the case where the numerator's degree == denominator's degree.
    # I wanted each student to calculate the horizontal asymptote from the ratio of the leading coefficients.
    horizontalAsymptote = a/(e*g*h)
    
    x = sympy.symbols("x")

    data["params"]["rationalPolynomial"] = sympy.latex((a * x**2 + b * x + c)/((d - e * x)*(f - h * g * x)))   
    data["correct_answers"]["ans"] = horizontalAsymptote


