# Demonstração de condicionais...

VALOR = None
if VALOR:
    if VALOR > 10:
        print("Você digitou um valor acima de 10!")
    elif VALOR >= 0:
        print("Esse valor ainda não é maior que 10!")
    else:
        print("Valor digitado é negativo!")
else:
    print("Não foi digitado nada!")