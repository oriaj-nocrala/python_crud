import sys
import Animal
import Cienpies
import Lombriz
import Sql_Usuario
import Usuario
class Menu:
  def __init__(self):
    self.animal = Animal.Animal()
    self.sql_usuario = Sql_Usuario.Sql_Usuario()
    # self.bienvenida()
    self.bienvenida()

  def bienvenida(self):
    print("¡Bienvenidos al programa de animales invertebrados!")
    print("En este programa podrás agregar más animales invertebrados de los más populares: los cienpies y las lombrices.")
    print("¡Espero que te diviertas!")
    print("")
    self.menu_usuario()

  def menu_usuario(self):
    print("¿Qué deseas hacer?")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir")
    opcion = input("Ingresa una opción: ")
    if opcion == "1":
      self.login()
    elif opcion == "2":
      self.register()
    elif opcion == "3":
      self.salir()
    else:
      print("¡Opción inválida! Por favor, inténtelo de nuevo.")
      self.menu_usuario()

  def register(self):
    nombre = input("Ingresa tu nombre: ")
    edad = input("Ingresa tu edad: ")
    correo = input("Ingresa tu correo: ")
    contraseña = input("Ingresa tu contraseña: ")
    usuario = Usuario.Usuario(nombre, edad, correo, contraseña)
    self.sql_usuario.insertar_usuario(usuario)
    print("¡Usuario registrado con éxito!")
    self.login()

  def login(self):
    usuario = input("Ingresa tu nombre de usuario: ")
    contraseña = input("Ingresa tu contraseña: ")
    if self.sql_usuario.login(usuario, contraseña):
      print("¡Bienvenido, administrador!")
      self.menu_principal()
    else:
      print("Usuario o contraseña inválidos. Por favor, inténtelo de nuevo.")
      self.login()

  def menu_principal(self):
    print("Menú principal")
    print("1. Agregar animal")
    print("2. Ver animales")
    print("3. Editar animal")
    print("4. Eliminar animal")
    print("5. Json")
    print("6. Salir")
    opcion = input("Ingresa una opción: ")

    if opcion == "1":
      self.agregar_animal()
    elif opcion == "2":
      self.ver_animales()
    elif opcion == "3":
      self.editar_animal()
    elif opcion == "4":
      self.eliminar_animal()
    elif opcion == "5":
      self.json()
    elif opcion == "6":
      print("¡Hasta luego!")
      self.salir()
    else:
      print("Opción inválida. Por favor, inténtelo de nuevo.")
      self.menu_principal()

  def agregar_animal(self):
    print("Agregar animal")
    print("1. Cienpies")
    print("2. Lombriz")
    print("3. Regresar al menú principal")
    opcion = input("Ingresa una opción: ")
    self.agregar_animal_opcion_handler(opcion)

  def agregar_animal_opcion_handler(self, opcion):
    if opcion == "1":
      self.agregar_cienpies()
    elif opcion == "2":
      self.agregar_lombriz()
    elif opcion == "3":
      self.menu_principal()
    else:
      print("Opción inválida. Por favor, inténtelo de nuevo.")
      self.agregar_animal()

  def agregar_cienpies(self):
    print("Agregar cienpies")
    cienpies = self.get_input_cienpies()
    self.animal.agregar_cienpies(cienpies)
    self.animal.insertar_cienpies(cienpies)
    print("Cienpies agregado exitosamente.")
    self.agregar_animal()

  def get_input_cienpies(self) -> Cienpies:
    print("Ingresa los datos del cienpies:")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    patas = int(input("Patas: "))
    venenoso = True if input("Venenoso (s/n): ") == "s" else False
    cienpies = self.cienpies_factory(nombre, edad, patas, venenoso)
    return cienpies

  def cienpies_factory(self, nombre, edad, patas, venenoso) -> Cienpies:
    cienpies = Cienpies.Cienpies(nombre, edad, patas, venenoso)
    return cienpies

  def agregar_lombriz(self):
    print("Agregar lombriz")
    lombriz = self.get_input_lombriz()
    self.animal.agregar_lombriz(lombriz)
    self.animal.insertar_lombriz(lombriz)
    print("Lombriz agregada exitosamente.")
    self.agregar_animal()
  
  def get_input_lombriz(self) -> Lombriz:
    print("Ingresa los datos de la lombriz:")
    nombre = input("Nombre: ")
    tamaño = int(input("Tamaño: "))
    especie = input("Especie: ")
    color = input("Color: ")
    lombriz = self.lombriz_factory(nombre, tamaño, especie, color)
    return lombriz

  def lombriz_factory(self, nombre, tamaño, especie, color) -> Lombriz:
    lombriz = Lombriz.Lombriz(nombre, tamaño, especie, color)
    return lombriz

  def almacenar_cienpies(self, cienpies: Cienpies):
    # Aquí puedes agregar el código para agregar un cienpies a la base de datos
    pass

  def ver_animales(self):
    print("Ver animales")
    print("1. Cienpies")
    print("2. Lombriz")
    print("3. Regresar al menú principal")
    opcion = input("Ingresa una opción: ")
    self.ver_animales_opcion_handler(opcion)
  
  def ver_animales_opcion_handler(self, opcion):
    if opcion == "1":
      self.ver_cienpies()
    elif opcion == "2":
      self.ver_lombriz()
    elif opcion == "3":
      self.menu_principal()
    else:
      print("Opción inválida. Por favor, inténtelo de nuevo.")
      self.ver_animales()

  def ver_cienpies(self):
    print("Ver cienpies\n")
    print(self.animal.str_cienpies())
    self.ver_animales()

  def ver_lombriz(self):
    print("Ver lombriz\n")
    print(self.animal.str_lombriz())
    self.ver_animales()

  def editar_animal(self):
    print("Editar animal")
    print("1. Cienpies")
    print("2. Lombriz")
    print("3. Regresar al menú principal")
    opcion = input("Ingresa una opción: ")
    self.editar_animal_opcion_handler(opcion)

  def editar_animal_opcion_handler(self, opcion):
    if opcion == "1":
      self.editar_cienpies()
    elif opcion == "2":
      self.editar_lombriz()
    elif opcion == "3":
      self.menu_principal()
    else:
      print("Opción inválida. Por favor, inténtelo de nuevo.")
      self.editar_animal()

  def editar_cienpies(self):
    print("Editar cienpies")
    print(self.animal.str_cienpies())
    cienpies = self.get_input_cienpies()
    self.animal.editar_cienpies(cienpies)
    print("Cienpies editado exitosamente.")
    self.editar_animal()

  def editar_lombriz(self):
    print("Editar lombriz")
    print(self.animal.str_lombriz())
    lombriz = self.get_input_lombriz()
    self.animal.editar_lombriz(lombriz)
    print("Lombriz editada exitosamente.")
    self.editar_animal()

  def eliminar_animal(self):
    print("Eliminar animal")
    print("1. Cienpies")
    print("2. Lombriz")
    print("3. Regresar al menú principal")
    opcion = input("Ingresa una opción: ")
    self.eliminar_animal_opcion_handler(opcion)

  def eliminar_animal_opcion_handler(self, opcion):
    if opcion == "1":
      self.eliminar_cienpies()
    elif opcion == "2":
      self.eliminar_lombriz()
    elif opcion == "3":
      self.menu_principal()
    else:
      print("Opción inválida. Por favor, inténtelo de nuevo.")
      self.eliminar_animal()

  def eliminar_cienpies(self):
    print("Eliminar cienpies")
    print(self.animal.str_cienpies())
    seleccion = input("Indique el cienpies que desea eliminar: ")
    cienpies = self.animal.get_cienpies_by_name(seleccion)
    self.animal.eliminar_cienpies(cienpies)
    print("Cienpies eliminado exitosamente.")
    self.eliminar_animal()

  def eliminar_lombriz(self):
    print("Eliminar lombriz")
    print(self.animal.str_lombriz())
    seleccion = input("Indique la lombriz que desea eliminar: ")
    lombriz = self.animal.get_lombriz_by_name(seleccion)
    self.animal.eliminar_lombriz(lombriz)
    print("Lombriz eliminada exitosamente.")
    self.eliminar_animal()

  def json(self):
    print("JSON")
    print("1. Guardar JSON en archivo")
    print("2. Cargar JSON desde archivo e imprimirlo")
    print("3. Regresar al menú principal")
    opcion = input("Ingresa una opción: ")
    self.json_opcion_handler(opcion)

  def json_opcion_handler(self, opcion):
    if opcion == "1":
      self.guardar_json()
    elif opcion == "2":
      self.cargar_json()
    elif opcion == "3":
      self.menu_principal()
    else:
      print("Opción inválida. Por favor, inténtelo de nuevo.")
      self.json()

  def guardar_json(self):
    print("Guardar JSON en archivo")
    self.animal.guardar_json()
    print("JSON guardado exitosamente.")
    self.json()

  def cargar_json(self):
    print("JSON cargado exitosamente.")
    print(self.animal.cargar_json())
    self.json()

  def salir(self):
    print("Saliendo...")
    sys.exit()

M = Menu()