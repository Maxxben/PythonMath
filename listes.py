def lesListes():

    #creation de listes
    list = [5,8,1,10,6]

    print(list)
    print()
    print("Tri une liste")
    list.sort()
    print(list)
    print()

    print("Insere 5 a la l'index 3")
    list.insert(3,5)
    print(list)
    print()

    print("Insere 5 a la derniere position")
    list.insert(len(list),5)
    print(list)
    print()

    print("Remplace la position 50 a l'index 2")
    list[2] = 50
    print(list)
    print()

    print("afficher la liste avec for")
    for val in list:
        print(val)

    print()