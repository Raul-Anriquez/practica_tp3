#Crear la clase Punto con dos atributos x e y (ambos numéricos), con el correspondiente constructor que recibe ambos valores.
# Definir métodos tales como:
# eje_x
# eje_y
# impresion (método que devuelve en representación de string ambos valores)
# opuesto (método que devuelve el punto opuesto -es decir con los atributos negativos-)
# Cualquier otro método que considere importante

class Punto:
    def __init__(self,eje_x, eje_y):
        self.eje_x = eje_x
        self.eje_y = eje_y
    def impresion(self):
        return f"esta en el punto ({self.eje_x}, {self.eje_y})"
    def opuesto(self):
        return f"el punto opuesto es ({-self.eje_x, -self.eje_y})"

Punto1 = Punto(7, 3)
print(Punto1.impresion())
print(Punto1.opuesto())