"""

 Author: Yannis STEFANELLI

 Creation Date: 16-01-2023 19:33:30

 Description :

"""

def error():
    print("erreur")

def exo1():

    answer = "yes"

    while answer == "yes":
        letter = input("rentrer un caractère : ")

        if len(letter) == 1:
            print(letter + " vaut " + str(ord(letter)))
        else:
            print("Rentrez une seule lettre !")
            exit(1)    
            

        try:
            integer = int(input("rentrer un entier : "))
            print(str(integer) + " vaut " + chr(integer))
        except:
            print("valeur non entière !")
            exit(1)

        answer = input("Voulez-vous recommencer [oO] ? N\n")

        if answer == 'N' or answer == 'n':
            answer == "no"
        elif answer == 'O' or answer == 'o':
            answer == "yes"
        else:
            answer = "undefined"
            print("Réponse inconnue, je quitte le programme")
            exit


def exo2():
    try:
        A = int(input("Rentrer A (en m ) : "))
    except:
        error()
    try:
        B = int(input("Rentrer B (en m ) : "))
    except:
        error()
    try:
        C = int(input("Rentrer A (en m ) : "))
    except:
        error()

    result = (A + B) * C * 0.5

    print("La surface du trapèze est de " + str(result) + "m\n")

def exo3():
    i = 0
    add = 0
    reverse = ""

    try:
        nb = int(input("entrer un entier positif : "))
    except:
        error()

    
    for i in range (1, nb):
        print(str(i) + " + ", end="")
        add += i
    print(str(i+1) + " = " + str(add + i + 1))

    add = 1

    for i in range (1, nb + 1):
        if i == nb:
            reverse += str(i) + " "
            print(str(i) + " ", end="")
        else:
            reverse += str(i) + " * "
            print(str(i) + " * ", end="")
        add = add * i
    reverse += "= "
    print("= " + str(add))
    print(str(add) + reverse[::-1])






while(True):
    try:
        menu = int(input("Quel exercice voulez vous executer ? 1-5 ( 0 pour quitter )\n"))
    except:
        print("Réponse inconnue, à bientôt !\n")
        exit(1)

    match menu:
            case 1:
                exo1()
            case 2:
                exo2()
            case 3:
                exo3()
            case 0:
                print("Je quitte le programme")
                exit(0)
            case _:
                print("Un chiffre entre 1 et 5 !!!")
