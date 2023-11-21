import re

class Veiculo:
  cls_id = 1

  def __init__(self):
    self.id = Veiculo.cls_id

    Veiculo.cls_id += 1

  def cadastrar_veiculo(self, placa, marca, modelo, ano):
    self.placa = self.valida_placa()
    self.marca = marca
    self.modelo = modelo
    self.ano = ano

  def valida_placa(self):
    pattern = r"^[a-zA-Z]{3}[0-9][A-Za-z0-9][0-9]{2}$"

    while True:
      placa = input("Digite a placa no formato antigo ou Mercosul sem '-': ")

      if re.match(pattern, placa):
        break
      else:
        print("Placa inválida. Tente novamente.")

    return placa