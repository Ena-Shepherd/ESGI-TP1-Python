"""

 Author: Yannis STEFANELLI

 Creation Date: 16-01-2023 19:33:30

 Description :

"""

import math
from decimal import Decimal

def error():
    print("erreur")


def factorielle(valeur):
    chiffre = 1

    for i in range(1, valeur+1) : 
        chiffre = chiffre*i
    return(chiffre)


def f1(x,n):
    res = x**n / Decimal(factorielle(n))
    return(res)


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


def exo4():
    try:
        nb = int(input("Hauteur de l'arbre : "))
    except:
        error()
        return

    nb2 = nb
    nb3 = nb

    for i in range (1, (2 *nb) + 1):

        if i%2 == 0:
            for j in range (0, nb2+2):
                print("=", end="")
            nb2 -= 1

            for k in range (1, i):
                print("*", end="")

            for j in range (0, nb3+2):
                print("=", end="")
            nb3 -= 1

            print('')
            
    nb2 = nb
    nb3 = nb
    
    for i in range (1, ((2 *nb) + 1) // 2):

        if i%2 == 0:
            for j in range (0, nb2+2):
                print("=", end="")
            nb2 -= 1

            for k in range (1, i):
                print("*", end="")

            for j in range (0, nb3+2):
                print("=", end="")
            nb3 -= 1

            print('')


def exo5():
    try:
        x = int(input("Saisir un entier : "))
    except:
        error()
        return

    print("Ln = " + str(format(math.log(x), '.2f')))
    print("Sinus(Rad) = " + str(format(math.sin(x), '.3f')))
    print("Cosinus(Rad) = " + str(format(math.cos(x), '.3f')))


def exo6():
    try:
        valeur = int(input("Veuillez rentrer n : "))
    except:
        error()
        return
    
    resultat1 = factorielle(valeur-1)
    resultat2 = factorielle(valeur)
    resultat = resultat1*resultat2
    
    print("factoriel(",valeur,") est : ",resultat)
    
    try:
        x  = int(input("Saisir x : "))
    except:
        error()
        return
    try:
        n  = int(input("Saisir n : "))
    except:
        error()
        return

    print(format(f1(x,n), '.3f'))
    
    
    print("Res(x,i)")
    try:
        x = Decimal(input("Saisir x : "))
    except:
        error()
        return
    try:
        n = int(input("Saisir n : "))
    except:
        error()
        return

    somme = 0
    
    for i in (range (1, n)):
        somme += f1(x,i)
  
    print(format(somme, '.3f'))


def exo7():
    try:
        val= (int(input("Saisir n : ")))
    except:
        error()
        return

    u0 = 1
    un = u0
    
    for i in range(1, val+1) :
        vn = un + 1/(val * factorielle(i))
        un = un + (1 / factorielle(i))
        
    
    print("Valeur Un où n =",val,"est",format(un, '.3f'))
    print("Valeur Vn où n =",val,"est",format(vn, '.3f'))


def exo8():
    try:
        n = int(input("Saisir n : "))
    except:
        error()
        return
    try:
        p = int(input("Saisir p : "))
    except:
        error()
        return

    facto_n = factorielle(n)
    facto_np = factorielle(n-p)
    x = facto_n / facto_np
    y = facto_n / (factorielle(p) * facto_np)
    print("x =", x,"y =", y)
    
        


while(True):
    try:
        menu = int(input("Quel exercice voulez vous executer ? 1-8 ( 0 pour quitter )\n"))
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
            case 4:
                exo4()
            case 5:
                exo5()
            case 6:
                exo6()
            case 7:
                exo7()
            case 8:
                exo8()
            case 0:
                print("Je quitte le programme")
                exit(0)
            case _:
                print("Un chiffre entre 1 et 8 !!!")
