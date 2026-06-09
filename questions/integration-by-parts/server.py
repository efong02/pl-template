import random
import sympy

def generate(data):
    a = random.randrange(2,5)

    # sometimes a is a small fraction
    if bool(random.getrandbits(1)):
         a = sympy.Rational(1,a)


    #select a transcendental function.
    flavor = random.randrange(1,5)
    x = sympy.symbols('x')
    C = sympy.symbols('C')

    #exponential
    if flavor == 1: 
        integrand = x*sympy.exp(a*x)
    #logarithmic
    if flavor == 2:
        integrand = x**a*sympy.log(x) 
    #sine
    if flavor == 3:
        integrand = x*sympy.sin(a*x)
    #cosin
    if flavor == 4:
        integrand = x*sympy.cos(a*x)

    data["params"]["integrand"] = sympy.latex(integrand)
    data["params"]["x"] = sympy.latex(x)
    data["params"]["C"] = sympy.latex(C)

    data["correct_answers"]["ans"] = str(sympy.integrate(integrand, x) + C)