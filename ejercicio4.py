#jercicio 4:
# Desarrolla una clase Cancion con los siguientes atributos:
# titulo: una variable String que guarda el título de la canción.
# autor: una variable String que guarda el autor de la canción.
#con lossiguientes métodos:
#Cancion(String, String): constructor que recibe como parámetros el título y el autor de la canción (por este orden).
# get_titulo(): devuelve el título de la canción.
#get_autor(): devuelve el autor de la canción.
# set_titulo(String): establece el título de la canción.
# set_autor(String): establece el autor de la canción

class Cancion:
    def __init__(self, titulo:str, autor:str):
        self.titulo = titulo
        self.autor = autor
    def get_titulo(self):
        return self.titulo
    def get_autor(self):
        return self.autor
    def set_titulo(self, titulo:str):
        self.titulo = titulo
    def set_autor(self, autor:str):
        self.autor = autor

Cancion1 = Cancion("La Leyenda del Hada y el Mago", "Rata Blanca")
Cancion2 = Cancion("The Trooper", "Iron Maiden")

Cancion1.set_titulo("Mi gente")
Cancion1.set_autor("J Balvin")
print("Cancion 1: ", Cancion1.get_titulo(),"De",Cancion1.get_autor())
print("Cancion 2: ", Cancion2.get_titulo(), "De",Cancion2.get_autor())