#Ejercicio 3:
#Define una clase Línea con dos atributos: _punto_a y _punto_b. Son dos puntos por los que pasa la línea en un espacio de dos dimensiones.
#La clase dispondrá de los siguientes métodos:
#Linea(Punto, Punto) Constructor que recibe como parámetros dos objetos de la clasePunto, que son utilizados para inicializar los atributos.
# mueve_derecha(float) Desplaza la línea a la derecha la distancia que se indique.
# mueve_izquierda(float) Desplaza la línea a la izquierda la distancia que se indique.
# mueve_arriba(float) Desplaza la línea hacia arriba la distancia que se indique.
# mueve_abajo(float) Desplaza la línea hacia abajo la distancia que se indique.

class Punto:
    def __init__(self,eje_x, eje_y):
        self.eje_x = eje_x
        self.eje_y = eje_y
    def impresion(self):
        return f"esta en el punto ({self.eje_x}, {self.eje_y})"
    def opuesto(self):
        return f"el punto opuesto es ({-self.eje_x, -self.eje_y})"

class Linea:
    def __init__(self, _punto_a, _punto_b):
        self.punto_a = _punto_a
        self.punto_b = _punto_b

    def mueve_derecha(self, distancia:float):
        self.punto_a.eje_x += distancia
        self.punto_b.eje_x += distancia

    def mueve_izquierda(self, distancia:float):
        self.punto_a.eje_x -= distancia
        self.punto_b.eje_x -= distancia

    def mueve_arriba(self, distancia:float):
        self.punto_a.eje_y += distancia
        self.punto_b.eje_y += distancia

    def mueve_abajo(self, distancia:float):
        self.punto_a.eje_y -= distancia
        self.punto_b.eje_y -= distancia

Punto1= Punto(7, 3) 
Punto2 = Punto(4, 1)
Linea1 = Linea(Punto1,Punto2)

Linea1.mueve_derecha(5.5)
Linea1.mueve_arriba(1.5)
Linea1.mueve_izquierda(3.5)
Linea1.mueve_abajo(2.5)