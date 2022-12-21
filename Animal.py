import json
import Cienpies
import Lombriz
import Sql_Animal
import Jsons
class Animal:
  def __init__(self):
    self.lista_cienpies: list(Cienpies) = []
    self.lista_lombriz: list(Lombriz) = []
    self.sql_animal = Sql_Animal.Sql_Animal()
    res = self.sql_animal.get_cienpies()
    for r in res:
      self.lista_cienpies.append(Cienpies.Cienpies( r[1], r[2], r[3], r[4]))
    res = self.sql_animal.get_lombrices()
    for r in res:
      self.lista_lombriz.append(Lombriz.Lombriz( r[1], r[2], r[3], r[4]))
  def __del__(self):
    del self.sql_animal
  def agregar_cienpies(self, cienpies):
    self.lista_cienpies.append(cienpies)
  def agregar_lombriz(self, lombriz):
    self.lista_lombriz.append(lombriz)
  def editar_cienpies(self, cienpies):
    for c in self.lista_cienpies:
      if c.get_nombre() == cienpies.get_nombre():
        c.set_edad(cienpies.get_edad())
        c.set_patas(cienpies.get_patas())
        c.set_venenoso(cienpies.get_venenoso())
  def editar_lombriz(self, lombriz):
    for l in self.lista_lombriz:
      if l.get_nombre() == lombriz.get_nombre():
        l.set_tamaño(lombriz.get_tamaño())
        l.set_color(lombriz.get_color())
        l.set_especie(lombriz.get_especie())
  def eliminar_cienpies(self, cienpies):
    self.lista_cienpies.remove(cienpies)
  def eliminar_lombriz(self, lombriz):
    self.lista_lombriz.remove(lombriz)
  def get_cienpies_by_name(self, nombre):
    for c in self.lista_cienpies:
      if c.get_nombre() == nombre:
        return c
  def get_lombriz_by_name(self, nombre):
    for l in self.lista_lombriz:
      if l.get_nombre() == nombre:
        return l
  def get_cienpies_by_index(self, index):
    return self.lista_cienpies[index]
  def get_lombriz_by_index(self, index):
    return self.lista_lombriz[index]
  def listar_cienpies(self):
    for c in self.lista_cienpies:
      print(c)
  def listar_lombriz(self):
    for l in self.lista_lombriz:
      print(l)
  def get_lista_cienpies(self):
    return self.lista_cienpies
  def get_lista_lombriz(self):
    return self.lista_lombriz
  def str_cienpies(self):
    output = ""
    for cienpies in self.lista_cienpies:
      output += str(f"Cienpies: {cienpies}\n")
    return output
  def str_lombriz(self):
    output = ""
    for lombriz in self.lista_lombriz:
      output += str(f"Lombriz: {lombriz}\n")
    return output
  def __str__(self):
    output = ""
    for i, cienpies in self.lista_cienpies:
      output += str(f"{cienpies}\n")
    for i, lombriz in self.lista_lombriz:
      output += str(f"{lombriz}\n")
    return output
  def insertar_cienpies(self, cienpies):
    self.sql_animal.insertar_cienpies(cienpies)
  def insertar_lombriz(self, lombriz):
    self.sql_animal.insertar_lombriz(lombriz)
  def guardar_json(self):
    with open('json.json', 'w') as file:
      Jsons.Jsons(self.lista_cienpies, self.lista_lombriz, "json.json")
  def cargar_json(self):
    with open('json.json', 'r') as file:
      jsons = json.load(file)
      lista_cienpies = []
      lista_lombriz = []
      for c in jsons['cienpies']:
        lista_cienpies.append(Cienpies.Cienpies(c['nombre'], c['edad'], c['patas'], c['venenoso']))
      for l in jsons['lombriz']:
        lista_lombriz.append(Lombriz.Lombriz(l['nombre'], l['tamano'], l['color'], l['especie']))
      for c in lista_cienpies:
        print(c)
      for l in lista_lombriz:
        print(l)