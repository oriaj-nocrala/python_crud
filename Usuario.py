class Usuario:
  def __init__(self, nombre, edad, correo, contraseña):
    self.nombre = nombre
    self.edad = edad
    self.correo = correo
    self.contraseña = contraseña
  def __del__(self):
    pass
  def get_nombre(self) -> str:
    return self.nombre
  def get_edad(self) -> int:
    return self.edad
  def get_correo(self) -> str:
    return self.correo
  def get_contraseña(self) -> str:
    return self.contraseña
  def set_nombre(self, nombre):
    self.nombre = nombre
  def set_edad(self, edad):
    self.edad = edad
  def set_correo(self, correo):
    self.correo = correo
  def set_contraseña(self, contraseña):
    self.contraseña = contraseña
  def __str__(self) -> str:
    return f"Nombre: {self.nombre}, Edad: {self.edad}, Correo: {self.correo}, Contraseña: {self.contraseña}"