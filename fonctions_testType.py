def testBornes(nombre, min, max):
    if nombre < min:
        print("KO Votre nombre est INFERIEUR a 0")
    if nombre > max:
        print("KO Votre nombre est SUPERIEUR a 10")
    print()

def entier(nombre,min,max):
    while (nombre < min or nombre > max):
        nombre = int(input("Entrez un ENTIER entre 0 et 10:\n"))
        # Ou : mess = "Saisir un entier compris entre",min,"et",max," :"

        testBornes(nombre,min, max)

    return nombre

def reel(nombre,min,max):
    while (nombre < min or nombre > max):
        nombre = float(input("Entrez un REEL entre 0 et 10:\n"))
        # Ou : mess = "Saisir un entier compris entre",min,"et",max," :"

        testBornes(nombre,min, max)

    return nombre

def character(chaine):
    while (chaine):
        nombre = str(input("Entrez un CARACTERE:\n"))
        # Ou : mess = "Saisir un entier compris entre",min,"et",max," :"

    return nombre


