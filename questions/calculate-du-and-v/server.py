import random
import sympy

def generate(data):
    # a is a small coefficient
    a = random.randrange(2,5)
    
    # sometimes a is a small fraction
    if bool(random.getrandbits(1)):
        a = sympy.Rational(1,a)

    # define sympy symbols
    x = sympy.symbols('x')
    dx = sympy.symbols('dx')
    C = sympy.symbols('C')

    # select a transcendental function.
    flavor = random.randrange(1,5)
    # exponential
    if flavor == 1: 
        integrand = x*sympy.exp(a*x)
        u = x
        dv = sympy.exp(a*x)


    # logarithmic
    if flavor == 2:
        integrand = x**a*sympy.log(x) 
        # in this case, u = log(x); differentiates nicely, and its integral is a non-trivial computation.
        u = sympy.log(x)
        dv = x**a

    # sine
    if flavor == 3:
        integrand = x*sympy.sin(a*x)
        u = x
        dv = sympy.sin(a*x)

    # cosine
    if flavor == 4:
        integrand = x*sympy.cos(a*x)
        u = x
        dv = sympy.cos(a*x)

    data["params"]["u"] = sympy.latex(u)
    data["params"]["dv"] = sympy.latex(dv)
    data["params"]["integrand"] = sympy.latex(integrand)
    data["params"]["x"] = sympy.latex(x)
    data["params"]["dx"] = sympy.latex(dx)
    data["params"]["C"] = sympy.latex(C)
    data["correct_answers"]["v"] = str(sympy.integrate(dv,x) + C)
    data["correct_answers"]["du"] = str(sympy.diff(u,x) * dx)