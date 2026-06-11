import random
import sympy
import math

def generate(data):
    a = random.randrange(2,5)

    # sometimes a is a small fraction
    if bool(random.getrandbits(1)):
        a = sympy.Rational(1,a)


    #select a transcendental function.
    flavor = random.randrange(1,5)
    x = sympy.symbols('x')
    dx = sympy.symbols('dx')

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
    data["params"]["dx"] = sympy.latex(dx)
    data["params"]["flavor"] = flavor

    # the integrands generate above are simple enough that they have one correct answer
    # even so, I added a rich-text-editor so students may defend their selections of u and dv

    data["correct_answers"]["u"] = str(u)
    data["correct_answers"]["dv"] = str(dv * dx)




#clunky attempt at feedback!
def grade(data):
    dv_correct = math.isclose(data["partial_scores"]["dv"]["score"], 1.0)
    # for x**a * ln(x), common mistake is to choose dv = ln(x)dx
    if not dv_correct and int(data["params"]["flavor"]) == 2:
       data["feedback"]["dv"] = "Your choice of $dv$ is hard to integrate!"


