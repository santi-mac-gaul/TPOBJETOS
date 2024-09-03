class Restaurante_Importado():
    def __init__(self,nombre,tipo, estado):
        self.nombre = nombre
        self.tipo = tipo
        self.estado = estado
    def DescribirRestaurante(self):
        print(f""" 
              NOMBRE DEL RESTAURANTE: {self.nombre}
              TIPOS DE COMIDA: {self.tipo}
              ESTADO: {self.estado}  """)
    def Abrir(self):
        if self.estado.lower() == "cerrado":    
            print(f'el {self.nombre} esta abierto ahora')
            self.estado = "abierto".lower()

class Heladeria(Restaurante_Importado):
    def __init__ (self,nombre,tipo, estado, sabores):
        super().__init__(nombre,tipo, estado)
        self.sabores = sabores
    def MostrarSabores(self):
        print(f"""LOS SABORES SON: {self.sabores}""")
