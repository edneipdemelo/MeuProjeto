# Sistema de avaliação para prestação de serviços...
executado = input("O serviço foi executado (sim/não)?")
if executado == "não":
    reclamar = input("Descreva a sua reclamação: ")
    nota = 0
elif executado == "sim":
    nota = int(input("Digite a nota (1 a 5): "))
    match nota:
        case 1:
            print("Que serviço péssimo!")
        case 2:
            print("Que serviço ruim.")
        case 3:
            print("O serviço foi razoável.")
        case 4:
            print("O serviço está bom.")
        case 5:
            print("O serviço está ótimo!")
        case _:
            print("O número digitado está errado...")
else:
    print("Não foi digitado sim ou não...")