import random
import sympy

def generate(data):

    #f(x) = (ax^k + bx + c)/(d - ex)(f - ghx)(1-x)**j
    # generate some coefficents. These don't particularly matter for this question.
    a = random.randrange(2,10)
    b = random.randrange(2,5)
    c = random.randrange(1,6)
    d = random.randrange(1,6)
    e = random.randrange(1,6)
    f = random.randrange(1,6)
    g = random.randrange(1,6)
    h = random.choice([1, -1])

    # j determines if there is a (1-x) term in the denominator.
    j = random.choice([0,1])

    # k determines the degree of numerator.
    k = random.choice([1,2,3,4])
    
    
    x = sympy.symbols("x")

    data["params"]["rationalPolynomial"] = sympy.latex((a * x**k + b * x + c)/((d - e * x)*(f - h * g * x)*(1-x)**j))  

    #numerator's degree is either 1,2,3,4.
    data["correct_answers"]["numDegree"] = k

    #denominator's degree is either 2,3.
    data["correct_answers"]["denomDegree"] = 2 + j


