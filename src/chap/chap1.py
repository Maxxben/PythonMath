import chap1_equation as equation
import chap1_equation as eq

def master():
    print("           ---------- Equation ----------\n")

    a = -7
    b = 4
    c = 4
    n = 5

    #equation.eq1(a,b)
    #equation.eq2(a,b)

    eq.equations(a,b)

    print("")
    res = eq.Inequations(a,b,"<",c)
    print(res)
    print("")

    res = eq.IneSecondDegres(a,b,c)
    print(res)
    print("")

    res = eq.IneSecondDegres(a, b, c)
    print(res)
    print("")

    res = eq.IneSecondDegres2(a, b, "<", c)
    print(res)
    print("")

    res = eq.changvar(a, b, c, n)
    print(res)
