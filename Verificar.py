# Utilizando match/case...

VALOR = int(input("Digite um valor entre 1 a 3: "))
match VALOR:
    case 1:
        print("Você digitou 1!")
    case 2:
        print("Você digitou 2!")
    case 3:
        print("Você digitou 3!")
    case _:
        print("Você digitou qualquer valor!")
