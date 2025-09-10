# Rotina de escalação para 11 jogadores...
Numbers = [], Players = []
for X in range(0, 11):
    Numero = input("Digite a camisa: ")
    Numbers.append(Numero)
    Jogador = input("Digite o nome do jogador: ")
    Players.append(Jogador)
print(Numbers, Players)
# Rotina de substituição de jogadores...
Y = 0
Substituicao = "S"
while Substituicao == "S":
    Saida = input("Digite o número de saída: ")
    Numero = input("Digite o nome de entrada: ")
    Jogador = input("Digite o nome do jogador: ")
    for X in range(0, 11):
        if Numbers[X] == Saida:
            Numbers[X] = Numero
            Players[X] = Jogador
    Y = Y + 1
    if Y == 3:
        break
    Substituicao = input("Deseja substituir mais (S/N): ")
# Exibição dos substituídos...
print(Numbers, Players)