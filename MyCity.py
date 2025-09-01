# Seja bem vindo ao Rio de Janeiro...

def VerificarCidade(N, C):
    if C == "Rio de Janeiro":
        print("Olá, ", N)
        print("Bem vindo à cidade maravilhosa!")
    else:
        print(N, "seja bem vindo a", C)

Nome = input("Digite o seu nome: ")
Cidade = input("Digite o nome da Cidade: ")
VerificarCidade(Nome, Cidade)