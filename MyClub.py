# Solução da atividade referente ao futebol...

NATURALIDADE = input("Qual é a sua naturalidade? ")
if NATURALIDADE == "carioca":
    TIME = input("Qual é o seu time? ")
    match TIME:
        case "Flamengo":
            print("Parabéns! Você é um privilegiado!")
        case "Fluminense":
            print("Não vou sacanear os tricolores...")
        case "Vasco":
            print("Não vou sacanear os vascaínos...")
        case "Botafogo":
            print("Não vou sacanear os botafoguenses...")
        case _:
            print("Este time não é nenhum dos grandes do Rio!")
elif NATURALIDADE == "paulista":
    TIME = input("Qual é o seu time? ")
    match TIME:
        case "Palmeiras":
            print("Parabéns! Você é um privilegiado!")
        case "São Paulo":
            print("Não vou sacanear os tricolores...")
        case "Santos":
            print("Não vou sacanear os santistas...")
        case "Corinthians":
            print("Não vou sacanear os corinthianos...")
        case _:
            print("Este time não é nenhum dos grandes de São Paulo!")
elif NATURALIDADE == "mineiro":
    TIME = input("Qual é o seu time? ")
    match TIME:
        case "Cruzeiro":
            print("Parabéns! Você é um privilegiado!")
        case "Atlético Mineiro":
            print("Não vou sacanear os atleticanos...")
        case _:
            print("Este time não é nenhum dos grandes de Minas!")
else:
    print("Opção não disponível!")