import re

class Registro:
  def registrar_lavagem(self, data, hora, veiculo, funcionario):
    self.data = Registro.valida_data(data)
    self.hora = Registro.valida_hora(hora)
    self.veiculo = veiculo
    self.funcionario = funcionario

  @staticmethod
  def valida_data(data):
    pattern = r"0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[1,2])\/(19|20)\d{2}"

    if not re.match(data, pattern):
      print("Data inválida. Por favor, insira uma data no formato dd/MM/YYYY")
      return

    return data
  
  @staticmethod
  def valida_hora(hora):
    pattern = r"^([0-1][0-9]|2[0-3]):[0-5][0-9]$"

    if not re.match(hora, pattern):
      print("Hora inválida. Por favor, insira uma data no formato HH:MM")
      return

    return hora
