import Animal
import json

class Jsons:
  def __init__(self, filename):
    self.filename = filename
  def __init__(self, lista_cienpies, lista_lombriz, filename):
    self.lista_cienpies = lista_cienpies
    self.lista_lombriz = lista_lombriz
    self.filename = filename
    data = self.serialize_animal()
    self.write(data)
    

  def read(self):
    with open(self.filename, 'r') as f:
      deserialize_animal = self.deserialize_animal(json.load(f))
    return deserialize_animal

  def write(self, data):
    with open(self.filename, 'w') as f:
      json.dump(self.serialize_animal(), f, indent=2)

  def serialize_animal(self):
    data = {
      'cienpies': [],
      'lombriz': []
    }
    for cienpies in self.lista_cienpies:
      data['cienpies'].append({
        'nombre': cienpies.get_nombre(),
        'edad': cienpies.get_edad(),
        'patas': cienpies.get_patas(),
        'venenoso': cienpies.get_venenoso()
      })
    for lombriz in self.lista_lombriz:
      data['lombriz'].append({
        'nombre': lombriz.get_nombre(),
        'tamano': lombriz.get_tamaño(),
        'color': lombriz.get_color(),
        'especie': lombriz.get_especie()
      })
    return data

  def str_json(self, data):
    return json.dumps(data, indent=2)
  def deserialize_animal(self, data):
    animal = Animal.Animal()
    for cienpies in data['cienpies']:
      animal.agregar_cienpies(Animal.Cienpies(cienpies['nombre'], cienpies['edad'], cienpies['patas'], cienpies['venenoso']))
    for lombriz in data['lombriz']:
      animal.agregar_lombriz(Animal.Lombriz(lombriz['nombre'], lombriz['tamaño'], lombriz['color'], lombriz['especie']))
    return animal