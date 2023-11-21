class Veiculo:
  cls_id = 1

  def __init__(self):
    self.id = Veiculo.cls_id

    Veiculo.cls_id += 1

  def cadastrar_veiculo(self, placa, marca, modelo, ano):
    self.placa = placa
    self.marca = marca
    self.modelo = modelo
    self.ano = ano
