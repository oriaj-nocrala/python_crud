import json

class Lombriz:
  def __init__(self, nombre, tamaño, especie, color):
    self.nombre = nombre
    self.tamaño = tamaño
    self.color = color
    self.especie = especie

  def get_nombre(self):
    return self.nombre

  def get_tamaño(self):
    return self.tamaño

  def get_color(self):
    return self.color

  def get_especie(self):
    return self.especie

  def set_nombre(self, nombre):
    self.nombre = nombre

  def set_tamaño(self, tamaño):
    self.tamaño = tamaño

  def set_color(self, color):
    self.color = color

  def set_especie(self, especie):
    self.especie = especie

  def digerir(self, materia_organica):
    print("La lombriz está digiriendo la materia orgánica")

  def __str__(self) -> str:
    return f"Nombre:{self.nombre}\nTamaño: {self.tamaño}\nColor: {self.color}\nEspecie: {self.especie}\n"