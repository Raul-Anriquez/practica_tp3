#Ejercicio 5:
# Crea una clase Libro que modele la información que se mantiene en una biblioteca sobre cada libro: título, autor (usa la clase Persona), ISBN, páginas, edición, editorial , lugar
#(ciudad y país) y fecha de edición (como texto). La clase debe proporcionar los siguientes servicios: getters y setters, método para leer la información y método para mostrar la
#información.
# Este último método mostrará la información del libro con este formato:

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    def get_nombre(self):
        return self.nombre
    def get_apellido(self):
        return self.apellido
class Libro:
    def __init__(self, titulo, autor, ISBN, paginas, edicion, editorial, lugar, fecha):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.paginas = paginas
        self.edicion = edicion
        self.editorial = editorial
        self.lugar = lugar
        self.fecha = fecha
    def get_titulo(self):
        return self.titulo
    def set_titulo(self, titulo):
        self.titulo = titulo
    def get_autor(self):
        return self.autor
    def set_autor(self, autor):
        self.autor = autor
    def get_ISBN(self):
        return self.ISBN
    def set_ISBN(self, ISBN):
        self.ISBN = ISBN
    def get_paginas(self):
        return self.paginas
    def set_paginas(self, paginas):
        self.paginas = paginas
    def get_edicion(self):
        return self.edicion
    def set_edicion(self, edicion):
        self.edicion = edicion
    def get_editorial(self):
        return self.editorial
    def set_editorial(self, editorial):
        self.editorial = editorial
    def get_lugar(self):
        return self.lugar
    def set_lugar(self, lugar):
        self.lugar = lugar
    def get_fecha(self):
        return self.fecha
    def set_fecha(self, fecha):
        self.fecha = fecha

    def leer_informacion(self):
      return "titulo:" + self.titulo + " autor:" + self.autor.get_nombre() + " " + self.autor.get_apellido() + " ISBN:" + self.ISBN + " paginas:" +str(self.paginas) + " edicion:" + str(self.edicion) + " editorial:" + self.editorial + " lugar:" + self.lugar + " fecha:" + self.fecha
    
    def mostrar_informacion(self):
        print("Titulo: " + self.titulo)
        print("Autor: " + self.autor.get_nombre() + " " + self.autor.get_apellido())
        print("ISBN: " + self.ISBN)
        print("Paginas: " + str(self.paginas))
        print("Edicion: " + str(self.edicion))
        print("Editorial: " + self.editorial)
        print("Lugar: " + self.lugar)
        print("Fecha: " + self.fecha)

Libro1 = Libro("Harry Potter y la piedra filosofal", Persona("J.K.", "Rowling"), "978-0747532699", 223, "1", "Bloomsbury", "Londres, Reino Unido", "26 de junio de 1997")        
Libro1.set_titulo("Harry Potter y la cámara secreta")
Libro1.set_ISBN("978-0747538493")
Libro1.set_paginas(251)
Libro1.set_fecha("2 de julio de 1998")
Libro1.mostrar_informacion()
