# Classificação dos times no Campeonato Brasileiro...
time = input("Digite o seu time: ")
classificacao = int(input("Digite a posição: "))

if classificacao == 1:
    print("Campeão!!!")
elif classificacao >= 2 and classificacao <= 6:
    print("Libertadores!")
elif classificacao >= 7 and classificacao <= 12:
    print("Sul-Americana.")
elif classificacao >= 13 and classificacao <= 16:
    print("No limbo...")
elif classificacao >= 17 and classificacao <= 20:
    print("Rebaixado!")
else:
    print("Valor digitado não corresponde...")