import re

class Funcionario:
  cls_id = 1

  def __init__(self):
    self.id = Funcionario.cls_id

    Funcionario.cls_id += 1

  def cadastrar_funcionario(self, nome, cpf, data_nasc):
    self.nome = nome
    self.cpf = cpf
    self.data_nasc = Funcionario.valida_cpf(data_nasc)

  @staticmethod
  def valida_cpf(data):
    pattern = r"0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[1,2])\/(19|20)\d{2}"

    if not re.match(data, pattern):
      print("Data inválida. Por favor, insira uma data no formato dd/MM/YYYY")
      return

    return data
