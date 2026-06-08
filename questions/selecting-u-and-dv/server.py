import random
import sympy

def generate(data):
    a = random.randrange(2,5)

    #select a transcendental function.
    flavor = random.randrange(1,5)
    x = sympy.symbols('x')

    #exponential
    if flavor == 1: 
        integrand = x*sympy.exp(a*x)
        u = x
        dv = sympy.exp(a*x)

    #logarithmic
    if flavor == 2:
        integrand = x**a*sympy.log(x) 
        u = sympy.log(x)
        dv = x**a 


    #sine
    if flavor == 3:
        integrand = x*sympy.sin(a*x)
        u = x
        dv = sympy.sin(a*x)

    #cosine
    if flavor == 4:
        integrand = x*sympy.cos(a*x)
        u = x
        dv = sympy.cos(a*x)

    data["params"]["integrand"] = sympy.latex(integrand)
    data["params"]["x"] = sympy.latex(x)

    data["correct_answers"]["u"] = str(u)
    data["correct_answers"]["dv"] = str(dv)