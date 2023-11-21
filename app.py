import pandas as pd
from Funcionario import Funcionario
from Veiculo import Veiculo
from Registro import Registro


colunas_func = ['id', 'nome', 'cpf', 'data_nasc']
colunas_veiculo = ['id', 'placa', 'marca', 'modelo', 'ano']
colunas_registros = ['data', 'hora', 'placa', 'modelo', 'cpf', 'funcionario', 'tipo_lavagem', 'valor_cobrado']

df_funcionarios = pd.DataFrame(columns=colunas_func)
df_veiculos = pd.DataFrame(columns=colunas_veiculo)
df_registros = pd.DataFrame(columns=colunas_registros)

def menu():
    print("Selecione uma opção:")
    print("1 - Cadastrar Funcionário")
    print("2 - Cadastrar Veículo")
    print("3 - Registrar Lavagem")
    print("4 - Relatório de Lavagens")
    print("5 - Sair")

while True:
    menu()
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        funcionario = Funcionario()
        nome = input("Digite o nome do funcionário: ")
        cpf = input("Digite o CPF do funcionário: ")
        data_nasc = input("Digite a data de nascimento do funcionário (dd/MM/YYYY): ")

        funcionario.cadastrar_funcionario(nome, cpf, data_nasc)
        df_funcionarios = pd.append([df_funcionarios, funcionario.__dict__])
        print("Funcionário cadastrado com sucesso!")

    elif opcao == 2:
        veiculo = Veiculo()
        placa = input("Digite a placa do veículo: ")
        marca = input("Digite a marca do veículo: ")
        modelo = input("Digite o modelo do veículo: ")
        ano = int(input("Digite o ano do veículo: "))

        veiculo.cadastrar_veiculo(placa, marca, modelo, ano)
        df_veiculos = df_veiculos.append(veiculo._dict_)
        print("Veículo cadastrado com sucesso!")

    elif opcao == 3:
        registro = Registro()
        data = input("Digite a data da lavagem (dd/MM/YYYY): ")
        hora = input("Digite a hora da lavagem: ")
        placa = input("Digite a placa do veículo: ")
        modelo = input("Digite o modelo do veículo: ")
        cpf = input("Digite o CPF do funcionário: ")
        tipo_lavagem = input("Digite o tipo de lavagem (simples/completa): ")

        if tipo_lavagem.lower() == "simples":
            valor_cobrado = 50
        elif tipo_lavagem.lower() == "completa":
            valor_cobrado = 100
        else:
            print("Tipo de lavagem inválido!")
            continue

        registro.registrar_lavagem(data, hora, placa, modelo, cpf, funcionario, tipo_lavagem, valor_cobrado)
        df_registros = df_registros.append(registro._dict_)
        print("Lavagem registrada com sucesso!")

    elif opcao == 4:
        registros = df_registros.to_dict('records')
        print("\nRelatório de Lavagens:")
        for registro in registros:
            print("Data: {}, Hora: {}, Placa: {}, Modelo: {}, CPF: {}, Funcionário: {}, Tipo de Lavagem: {}, Valor Cobrado: {}".format(registro['data'], registro['hora'], registro['placa'], registro['modelo'], registro['cpf'], registro['funcionario'], registro['tipo_lavagem'], registro['valor_cobrado']))

    elif opcao == 5:
        break

    else:
        print("Opção inválida!")