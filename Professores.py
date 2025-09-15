# Demonstração de Orientação a Objetos...

class Funcionarios:
    def __init__(self, NOME, ADMISSAO, SALARIO, MATERIA):
        self.NOME = NOME
        self.ADMISSAO = ADMISSAO
        self.SALARIO = SALARIO
        self.MATERIA = MATERIA

class Professores(Funcionarios):
    def Materia(self):
        if self.MATERIA == "Matemática":
            print(f"{self.NOME} Ensina matemática!")
            return
    def Salario(self):
        if self.SALARIO > 2000:
            print("Ganha mais de R$ 2.000")
            return

Professor1 = Professores("João", "21/04/2001", 2500, "Matemática")
Professor1.Salario()
Professor1.Materia()