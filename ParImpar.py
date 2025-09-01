# Programa "Par ou Ímpar"...
import random

def ParImpar(X, Y):
    Resultado = (X + Y) % 2
    if Resultado == 0:
        print("É par! Ser humano venceu!")
    else:
        print("É ímpar! Computador venceu!")

N1 = random.randint(0, 10)
N2 = int(input("Ser humano - digite outro número: "))
ParImpar(N1, N2)
print("Computador gerou:", N1)
print("Você digitou:", N2)