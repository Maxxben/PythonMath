import math
from math import sqrt
import matplotlib.pyplot as plt


# Exercice 1
def eq1(a, b):
    if a == 0:
        if b == 0:
            result = [']', '-inf', ';', '+inf', '[']
        else:
            result = ['vide']
    else:
        result = ['{', str(-b / a), '}']
    return ''.join(result)


# Exercice 2
def ineq1(a, b):
    if a == 0:
        if b > 0:
            result = [']', '-inf', ';', '+inf', '[']
        else:
            result = ['vide']
    else:
        if a > 0:
            result = [']', str(-b / a), ';', '+inf', '[']
        else:
            result = [']', '-inf', ';', str(-b / a), '[']
    return ''.join(result)


# Exercice 3
def ineq1bis(a, b, symb):
    if symb is str(">"):
        return ineq1(a, b)
    else:
        return ineq1(-a, -b)  # ax+b<0 <=> -ax-b>0


# Exercice 4
def eq2(a, b, c):
    if a == 0:
        return eq1(b, c)
    else:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            result = ['vide']
        elif delta == 0:
            result = ['{', str(-b / (2 * a)), '}']
        else:
            result = ['{', str((-b - sqrt(delta)) / (2 * a)), ';', str((-b + sqrt(delta)) / (2 * a)), '}']
        return ''.join(result)


# Exercice 5
def ineq2(a, b, c):
    if a == 0:
        return ineq1(b, c)
    else:
        delta = b ** 2 - 4 * a * c
        if a > 0:
            if delta > 0:
                result = [']', '-inf', ';', str((-b - sqrt(delta)) / (2 * a)), '[', 'U', ']',
                          str((-b + sqrt(delta)) / (2 * a)), ';', '+inf', '[']
            elif delta == 0:
                result = ['R\{', -b / (2 * a), '}']
            else:
                result = ['R']
        else:
            if delta > 0:
                result = [']', str((-b + sqrt(delta)) / (2 * a)), ';', str((-b - sqrt(delta)) / (2 * a)), '[']
            else:
                result = ['vide']
    return ''.join(result)


# Exercice 6
def ineq2bis(a, b, c, symb):
    if symb is str(">"):
        return ineq2(a, b, c)
    else:
        return ineq2(-a, -b, -c)


# Exercice 7
def changvar(a, b, c, n):
    x = eq2(a, b, c)
    var = []
    for i in x:
        var.append(i ** (1 / n))
    print(var)


# Option
def test():
    T = [
        'REABRASES',
        'ENCRENENT',
        'OCTOCORDE',
        'RAVAUDERA',
        'CHICORIUM',
        'EPARTIRAS',
        'RENIERONS',
        'ALTERANTE',
        'SASSASSES']

    L = [c for line in T for c in line]

    n = len(T)
    p = len(T[0])

    # Diagonales au-dessus de la diagonale principale
    for k in range(p):
        diago = L[k:p * min(n, p - k):p + 1]
        print(' '.join(diago))

    print()
    # Diagonales en-dessous de la diagonale principale
    for k in range(n):
        diago = L[k * p:p * min(n, p + k):p + 1]
        print(' '.join(diago))


# Exercice 8

def recursif(str):
    if (len(str) == 1):
        return True
    if (str[0] != str[-1]):
        return False
    if (len(str) < len(str) + 1):
        return recursif(str[1:-1:1])


def exo1():
    val = []
    for i in range(1, 10):
        val.append(math.log(1 + (1 / i)))

    plt.plot(val, 'bo')

    val1 = []
    for i in range(1, 10):
        val1.append(((3 * math.exp(-1)) ** i))

    plt.plot(val1, color="red")

    val2 = []
    for i in range(1, 10):
        val2.append(math.sqrt(i ** 2 + 1) - math.sqrt(i))

    plt.plot(val2, color="green")
    plt.show()


def exo2(n):
    tab = []
    tab.append(2)
    for i in range(1, n):
        tab.append(((1 / 3) * tab[-1]) + 1)

    plt.plot(tab, 'bo')
    plt.show()


def exo2Rec(tab, n):
    if (len(tab) != n):
        tab.append(((1 / 3) * tab[-1]) + 1)
        tab = exo2Rec(tab, n)
    return tab


def exo3(n, prem):
    tab = []
    tab.append(prem)
    for i in range(1, n):
        tab.append((tab[-1] ** 2) / math.sqrt(math.exp(-tab[-1]) + 2))

    plt.plot(tab, 'bo')
    plt.show()


def exo3Rec(tab, n):
    if (len(tab) != n):
        tab.append((tab[-1] ** 2) / math.sqrt(math.exp(-tab[-1]) + 2))
        tab = exo3Rec(tab, n)
    return tab


def exo4(n, pre, sec):
    tab = []
    tab.append(pre)
    tab.append(sec)
    for i in range(2, n):
        tab.append((2 * tab[i - 1]) - 3 * tab[i - 2])
    return tab


def exo4Rec(n, pre, sec):
    tab = []
    tab.append(pre)
    tab.append(sec)








