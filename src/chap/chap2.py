import math

def checkPalindrome(chaine):

    if (len(chaine) != 1):
        if (chaine[0] == chaine[-1]):
            return checkPalindrome(chaine[1:-1:1])
        else:
            return False
    return True

def compterCaractere(chaine):
    print()
    if (len(chaine) != 1):
        print("en cours")



