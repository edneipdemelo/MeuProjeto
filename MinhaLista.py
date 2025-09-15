# Demonstração do uso de listas...
OPCAO = 999
SERIES = []; SERVICOS = []; TEMPORADAS = []
while OPCAO != 0:
    print("Escolha a operação:")
    print("1. Cadastrar / 2. Exibir / 3. Editar / 4. Excluir")
    OPCAO = int(input("Digite 0 para sair: "))

    if OPCAO == 1:
        SERIE = input("Digite o nome da série: ")
        SERVICO = input("Digite o nome do serviço: ")
        TEMPORADA = input("Digite a temporada que já assistiu: ")
        SERIES.append(SERIE); SERVICOS.append(SERVICO); TEMPORADAS.append(TEMPORADA)

print(SERIES, SERVICOS, TEMPORADAS)

# É possível personalizá-lo para adicionar funções extras?