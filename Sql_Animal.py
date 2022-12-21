import Sql
import Cienpies
import Lombriz

class Sql_Animal(Sql.Sql):
    def __init__(self):
        super().__init__()
        self.cursor = super().get_cursor()
        self.connection = super().get_connection()
    def __del__(self):
        super().connection_close()
    def insertar_cienpies(self, cienpies):
        query = f"INSERT INTO cienpies(nombre, edad, patas, venenoso) VALUES('{cienpies.get_nombre()}', {cienpies.get_edad()}, {cienpies.get_patas()}, {cienpies.get_venenoso()})"
        self.cursor.execute(query)
        self.connection.commit()
    def insertar_lombriz(self, lombriz):
        print(lombriz)
        query = f"INSERT INTO lombriz(nombre, tamaño, color, especie) VALUES('{lombriz.get_nombre()}', {lombriz.get_tamaño()}, '{lombriz.get_color()}', '{lombriz.get_especie()}');"
        print(query)
        self.cursor.execute(query)
        self.connection.commit()
    def editar_cienpies(self, cienpies):
        query = f"UPDATE cienpies SET edad = {cienpies.get_edad()}, patas = {cienpies.get_patas()}, venenoso = {cienpies.get_venenoso()} WHERE nombre = '{cienpies.get_nombre()}'"
        self.cursor.execute(query)
        self.connection.commit()
    def editar_lombriz(self, lombriz):
        query = f"UPDATE lombriz SET tamaño = {lombriz.get_tamaño()}, color = '{lombriz.get_color()}', especie = '{lombriz.get_especie()}' WHERE nombre = '{lombriz.get_nombre()}'"
        self.cursor.execute(query)
        self.connection.commit()
    def eliminar_cienpies(self, cienpies):
        query = f"DELETE FROM cienpies WHERE nombre = '{cienpies.get_nombre()}'"
        self.cursor.execute(query)
        self.connection.commit()
    def eliminar_lombriz(self, lombriz):
        query = f"DELETE FROM lombriz WHERE nombre = '{lombriz.get_nombre()}'"
        self.cursor.execute(query)
        self.connection.commit()
    def get_cienpies_by_name(self, nombre) -> Cienpies:
        query = f"SELECT * FROM cienpies WHERE nombre = '{nombre}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result
    def get_lombriz_by_name(self, nombre) -> Lombriz:
        query = f"SELECT * FROM lombriz WHERE nombre = '{nombre}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result
    def get_cienpies(self) -> list:
        query = "SELECT * FROM cienpies"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
    def get_lombrices(self) -> list:
        query = "SELECT * FROM lombriz"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
