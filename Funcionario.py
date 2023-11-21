import re

class Funcionario:
  cls_id = 1

  def __init__(self):
    self.id = Funcionario.cls_id

    Funcionario.cls_id += 1

  def cadastrar_funcionario(self, nome, cpf, data_nasc):
    self.nome = nome
    self.cpf = cpf
    self.data_nasc = Funcionario.valida_data(data_nasc)

  @staticmethod
  def valida_data(data):
    pattern = r"^(0[1-9]|[1-2][0-9]|3[0-1])\/(0[1-9]|1[0-2])\/(19|20)\d{2}$"

    if not re.match(pattern, data):
      print("Data inválida. Por favor, insira uma data no formato dd/MM/YYYY")
      return

    return data
