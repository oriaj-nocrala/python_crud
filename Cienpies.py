import json

class Cienpies:
  def __init__(self, nombre, edad, patas, venenoso):
    self.nombre = nombre
    self.edad = edad
    self.patas = patas
    self.venenoso = venenoso

  def get_nombre(self):
    return self.nombre

  def get_edad(self):
    return self.edad

  def get_patas(self):
    return self.patas

  def get_venenoso(self):
    return self.venenoso

  def set_nombre(self, nombre):
    self.nombre = nombre

  def set_edad(self, edad):
    self.edad = edad

  def set_patas(self, patas):
    self.patas = patas

  def set_venenoso(self, venenoso):
    self.venenoso = venenoso

  def __str__(self) -> str:
    return f"Nombre: {self.nombre}\nEdad: {self.edad}\nPatas: {self.patas}\nVenenoso: {self.venenoso}\n"

  def __dict__(self):
    return {
      'nombre': self.nombre,
      'edad': self.edad,
      'patas': self.patas,
      'venenoso': self.venenoso
    }
