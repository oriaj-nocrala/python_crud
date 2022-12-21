import Sql
import hashlib
import Usuario

class Sql_Usuario(Sql.Sql):
  def __init__(self):
    self.sql = Sql.Sql()
    self.connection = self.sql.get_connection()
    self.cursor = self.sql.get_cursor()
  def get_all_usuarios(self) -> list:
    query = "SELECT * FROM usuario"
    self.execute_query(query)
    result = self.cursor.fetchall()
    usuarios = []
    for row in result:
      usuarios.append(Usuario.Usuario(row[0], row[1], row[2], row[3]))
    return usuarios
  def insertar_usuario(self, usuario):
    password = usuario.get_contraseña()
    password = self.md5_encrypt(password)
    usuario.set_contraseña(password)
    query = f"INSERT INTO usuario(nombre, edad, correo, contraseña) VALUES('{usuario.get_nombre()}', {usuario.get_edad()}, '{usuario.get_correo()}', '{usuario.get_contraseña()}')"
    self.execute_query(query)
  def editar_usuario(self, usuario):
    password = usuario.get_contraseña()
    password = self.md5_encrypt(password)
    usuario.set_contraseña(password)
    query = f"UPDATE usuario SET edad = {usuario.get_edad()}, correo = '{usuario.get_correo()}', contraseña = '{usuario.get_contraseña()}' WHERE nombre = '{usuario.get_nombre()}'"
    self.execute_query(query)
  def eliminar_usuario(self, usuario):
    query = f"DELETE FROM usuario WHERE nombre = '{usuario.get_nombre()}'"
    self.execute_query(query)
  def get_usuario_by_name(self, nombre) -> Usuario:
    query = f"SELECT * FROM usuario WHERE nombre = '{nombre}'"
    self.execute_query(query)
    result = self.cursor.fetchone()
    if result is not None:
      return Usuario.Usuario(result[0], result[1], result[2], result[3])
  def md5_encrypt(self, password) -> str:
    return hashlib.md5(password.encode('utf-8')).hexdigest()
  def login(self, nombre, contraseña) -> bool:
    query = f"SELECT * FROM usuario WHERE nombre = '{nombre}'"
    try:
      self.cursor.execute(query)
      result = self.cursor.fetchone()
      if result is not None:
        if result[4] == self.md5_encrypt(contraseña):
          return True
    except Exception as e:
      print(f"Error al ejecutar la consulta {str(e)}")
      return False
    return False