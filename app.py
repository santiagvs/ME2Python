from Funcionario import Funcionario
from Veiculo import Veiculo
from Registro import Registro

while True:
    print("Seja bem-vindo. Deseja fazer o registro das lavagens?")
    confirmacao = input("Digite 'S' para sim: ")
    
    if (confirmacao.lower() != 's'):
        print("Saindo da execução.")
        break
    
    while True:
        print("Preencha os dados do Funcionário:\n")
        nome_funcionario = input("Digite o nome do funcionário: ")
        cpf = input("Digite o CPF do funcionário, sem caracteres especiais: ")
        data_nasc = input("Digite a data de nascimento do funcionário (dd/MM/YYYY): ")
        print("\n")
        
        funcionario = Funcionario()
        
        funcionario.cadastrar_funcionario(nome_funcionario, cpf, data_nasc)
        
        print("Deseja revisar os dados do funcionário adicionado?")
        revisao_confirmacao = input("Digite 'S' para sim: ")
        
        if (revisao_confirmacao.lower() == 's'):
            print(f"• Nome do funcionário: {funcionario.nome}\n• CPF: {funcionario.cpf}\n• Data de nascimento: {funcionario.data_nasc}")

            correcao_confirmacao = input("Deseja corrigir os dados? Digite 'S' para sim: ")
            if correcao_confirmacao.lower() == 's':
                continue

        break
