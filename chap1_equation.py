import matplotlib.pyplot as plt
import random
import math

def equations(a,b):
    print("----- Equation premier degres -----")

    if a != 0:
        print("Solution unique : -b/a = " + str(-b/a))
    else:  # si a est nul
        if b == 0:  # b est nul
            print("]" + str(-math.inf) + " ; " + str(math.inf) + "[")
        else:
            print("0 solutions")

#equations()

def resoudreEquationPremierDegre(a, b, c):
    r1 = c - b
    solution = r1 / a
    return solution

def variationsFonctionAffine(m):
    if m > 0:
        var = "croissante"
    else:
        var = "decroissante"
    return var


def Inequations(m, p, ineg, c):
    print("----- Inequation premier degres -----")

    sol = resoudreEquationPremierDegre(m, p, c)
    var = variationsFonctionAffine(m)

    if ineg == ">" or ineg == ">=":
        if var == "croissante":
            retour = [sol, "+infini"]
        else:
            retour = ["-infini", sol]
    else:
        if var == "croissante":
            retour = ["-infini", sol]
        else:
            retour = [sol, "+infini"]
    if ineg == ">=" or ineg == "<=":
        if retour[0] == sol:
            retour = ["["] + retour
        else:
            retour = retour + ["]"]
    else:
        if retour[0] == sol:
            retour = ["]"] + retour
        else:
            retour = retour
    return retour


def IneSecondDegres(a, b, c):
    print("----- Inequation second degres -----")

    delta(a, b, c, "intervalle")
    print(delta)

'''
L1 = []
L1.append(IneSecondDegres(7,3,-5))
print(L1[0])
'''


def IneSecondDegres2(a, b, ineg, c):
    print("----- Inequation second degres 2 -----")

    sol = resoudreEquationPremierDegre(a, b, c)
    var = variationsFonctionAffine(a)

    delta = (b*b)-(4*a*c)

    if ineg == ">" or ineg == ">=":
        if var == "croissante":
            retour = [sol, "+infini"]
        else:
            retour = ["-infini", sol]
    else:
        if var == "croissante":
            retour = ["-infini", sol]
        else:
            retour = [sol, "+infini"]
    if ineg == ">=" or ineg == "<=":
        if retour[0] == sol:
            retour = ["["] + retour
        else:
            retour = retour + ["]"]
    else:
        if retour[0] == sol:
            retour = ["]"] + retour
        else:
            retour = retour
    return retour


#a = IneSecondDegres2(6, 5, "<", -6)
#print(a)

def changvar(a,b, c, n):
    print("----- Changement de variable -----")
    print()
    if n%2 == 0:
        if a > 0:
            s1 = str(a) + '^1/' + str(n)
            s2 = '-'+str(a) + '^1/' + str(n)
            ret = ['{', s2, ';', s1 ,'}']
        elif a == 0:
            ret = ['{','0', '}']
        else:
            ret = ['{', 'vide', '}']
    else:
        s = str(a) + '^1/' + str(n)
        ret = ['{', s ,'}']
    return ''.join(ret)


def changvar(a,b,c,n):
    print("----- Changement de variable -----")
    print()

    delt = delta(a,b,c,"int")
    print("\nEnsemble de solutions :" + str(delt))
    return str(delt)


def delta(a,b,c, typeRetour):
    delta = (b * b) - (4 * a * c)
    racineDeDelta = math.isqrt(delta)
    print("Racine de Delta :" + str(racineDeDelta))

    if typeRetour == "int":
        if delta < 0:
            return "Pas de solution réel"
        if delta == 0:
            print("Il n'y a qu'une solution dans R : -b/2*a")
            res = -b / (2 * a)
            return res
        if delta > 0:
            print("Il 2 solutions dans R : -b +- RACINE(delta) / 2*a")
            res1 = (-b - racineDeDelta) / (2 * a)
            res2 = (-b + racineDeDelta) / (2 * a)
            print("\tSolution 1 : " + str(res1) + "\n\tSolution 2 : " + str(res2))
            return [res1, res2]
    if typeRetour == "intervalle":
        if delta < 0:
            return "Pas de solution réel"
        if delta == 0:
            print("Il n'y a qu'une solution dans R : -b/2*a")
            return [-b / (2 * a)]
        if delta > 0:
            print("Il 2 solutions dans R : -b +- RACINE(delta) / 2*a")
            return [(-b - racineDeDelta) / (2 * a), (-b + racineDeDelta) / (2 * a)]



