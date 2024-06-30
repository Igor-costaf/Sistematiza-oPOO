
print ("""MGS SAÚDE """)
#CLASSE
class Pessoa:

    def __init__(self, identificador, nome, telefone, email):
        self.identificador = identificador
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return (f"ID: {self.identificador}\n"
                f"Nome: {self.nome}\n"
                f"Telefone: {self.telefone}\n"
                f"Email: {self.email}\n")
    
#Herança
#Subclasse de Empregado
class Empregado(Pessoa):
    def __init__(self, identificador, nome, telefone, email, alergias, problemas_medicos):
        super().__init__(identificador, nome, telefone, email)
        self.alergias = alergias
        self.problemas_medicos = problemas_medicos

    def __str__(self):
        return (super().__str__() +
                f"Alergias: {self.alergias}\n"
                f"Problemas Médicos: {self.problemas_medicos}\n")

#Polimorfismo
class Supervisor(Empregado):
    def __init__(self, identificador, nome, telefone, email, alergias, problemas_medicos, departamento):
        super().__init__(identificador, nome, telefone, email, alergias, problemas_medicos)
        self.departamento = departamento

    def __str__(self):
        return (super().__str__() +
                f"Departamento: {self.departamento}\n")

class Vendedor(Empregado):
    def __init__(self, identificador, nome, telefone, email, alergias, problemas_medicos, especialidade):
        super().__init__(identificador, nome, telefone, email, alergias, problemas_medicos)
        self.especialidade = especialidade

    def __str__(self):
        return (super().__str__() +
                f"Especialidade: {self.especialidade}\n")
from collections import deque

#CLASSE (estrutura de dados)
class SistemaGerenciamento:
    #Método
    def __init__(self):
        self.empregados = {} # LISTA: Para armazenar empregados, utiliza o ID como chave que permite acesso aos empregados.
        self.tarefas = deque()  # Fila de tarefas para armazenar e processar tarefas estrutura FIFO (First In, First Out)

    #Método
    def adicionar_empregado(self):
        identificador = input("Digite o ID do empregado: ")
        
        if identificador in self.empregados:
            print("Erro: Um empregado com este ID já existe.")
            return
        
        tipo = input("Digite o tipo de empregado (Supervisor/Vendedor): ")
        nome = input("Digite o nome do empregado: ")
        telefone = input("Digite o telefone do empregado: ")
        email = input("Digite o email do empregado: ")
        alergias = input("Digite as alergias do empregado: ")
        problemas_medicos = input("Digite os problemas médicos do empregado: ")

        if tipo == "supervisor":
            departamento = input("Digite o departamento do gerente: ")
            empregado = Gerente(identificador, nome, telefone, email, alergias, problemas_medicos, departamento)
        elif tipo == "vendedor":
            especialidade = input("Digite a especialidade do técnico: ")
            empregado = Vendedor(identificador, nome, telefone, email, alergias, problemas_medicos, especialidade)
        else:
            print("Tipo de empregado desconhecido. Empregado não adicionado.")
            return

        self.empregados[identificador] = empregado
        print("Empregado adicionado com sucesso!")

    #Método
    def buscar_empregado(self):
        identificador = input("Digite o ID do empregado que deseja buscar: ")
        empregado = self.empregados.get(identificador)
        if empregado:
            print("Informações do empregado:")
            print(empregado)
        else:
            print("Empregado não encontrado.")

    #Método
    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
        print("Tarefa adicionada à fila.")

    #Método
    def processar_tarefa(self):
        # estruturas condicionais
        if self.tarefas: 
            tarefa = self.tarefas.popleft()
            print(f"Processando tarefa: {tarefa}")
        else:
            print("Não há tarefas para processar.")
def main():
    sistema = SistemaGerenciamento()
    # estruturas de repetição (loop)
    while True:
        print("\nSistema de Gerenciamento de Empregados")
        print("1. Adicionar Empregado")
        print("2. Buscar Empregado")
        print("3. Adicionar Tarefa")
        print("4. Processar Tarefa")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            sistema.adicionar_empregado()
        elif opcao == "2":
            sistema.buscar_empregado()
        elif opcao == "3":
            tarefa = input("Digite a tarefa a ser adicionada: ")
            sistema.adicionar_tarefa(tarefa)
        elif opcao == "4":
            sistema.processar_tarefa()
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, por favor escolha novamente.")

if __name__ == "__main__":
    main()
