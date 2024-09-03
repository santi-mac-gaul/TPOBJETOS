"""Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área 
del rectángulo."""

# class Rectangulo():
#     def __init__ (self,base,altura):
#         self.base = base
#         self.altura = altura

#     def Area(self):
#         return f'el area del rectangulo es de = {self.base * self.altura}'

# rectangulo = Rectangulo(10,20)
# print(rectangulo.Area())

"""Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina. La clase debe contener 
como miembros:
o Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
o Un atributo para el estado (lleno o vacío).
o Un atributo n, que indica la cantidad máxima de cebadas.
o Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una 
excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste!
o Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, se 
debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!
o Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. En ese caso la cantidad 
de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso: 
“Advertencia: el mate está lavado.” pero no se debe lanzar una excepción.
"""
# class Mate():
#     def __init__(self,CantidadCebadas,estado,maxcebadas):
#         self.CantidadCebadas = CantidadCebadas
#         self.estado = estado
#         self.maxcebada = maxcebadas
#         self.CantidadCebadas = self.maxcebada
    
#     def Cebar(self):
#         try:
#             if self.estado == "vacio":
#                 self.estado = "lleno"
#                 print("mate cebado, ahora el mate esta lleno")
#                 if self.CantidadCebadas <= 0:
#                     print(' el mate esta lavado')
#                 else:
#                     self.CantidadCebadas -= 1
#         except:
#             print("¡cuidado, el mate rebalzo! te quemaste")
    
#     def Beber(self):
#         if self.estado == "vacio":
#             print("El mate esta vacio")
#         else:
#             print('*Ruidito de tomando Mate*')
#             self.estado = 'vacio'


# matesito = Mate(0,"vacio",4)

# matesito.Cebar()
# print(matesito.CantidadCebadas)
# print(matesito.estado)

# matesito.Beber()
# print(matesito.estado)

# matesito.Cebar()
# print(matesito.estado)
# print(matesito.CantidadCebadas)

# matesito.Beber()

"""3) Botella y Sacacorchos
 Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
 Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, o None si está 
destapada.
 Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque el corcho y se guarde 
una referencia al corcho sacado. Debe lanzar una excepción en el caso en que la botella ya esté destapada, o si el 
sacacorchos ya contiene un corcho.
 Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el caso en el que no haya 
un corcho.
"""
# class Corcho:
#     def __init__(self,bodega):
#         self.bodega = bodega

# class Botella:
#     def __init__(self,corcho=None):
#         self.corcho = corcho

# class SacaCorchos:
#     def __init__(self):
#         self.corcho = None
    
#     def destapar(self,botella):
#         if botella.corcho is None:
#             print ('La botella esta destapada')
#         if self.corcho is not None:
#             return 'La Botella aun esta tapada'
#         self.corcho = botella.corcho
#         botella.corcho = None
    
#     def Limpiar(self):
#         try:
#             if self.corcho is not None:
#                 self.corcho = None
#                 print('haz limpiado el SacaCorchos')
#         except:
#             print ('no hay ningun corcho en el sacacorchos')
        
        
# corcho = Corcho("Bodega S")
# botella = Botella(corcho)
# sacacorcho = SacaCorchos()


# sacacorcho.destapar(botella)
# print(f'corcho de la botella de la {sacacorcho.corcho.bodega} sacado')
# sacacorcho.destapar(botella)
# sacacorcho.Limpiar()
# sacacorcho.Limpiar()


"""4) Una heladería es un tipo especial de restaurante. Cree una clase Restaurante, cuyo método __init__() guarde dos atributos: 
restaurante_nombre y tipo_comida. Cree un método describir_restaurante() que muestre estas piezas de información, y un 
método abrir_restaurante() que muestre un mensaje indicando que el restaurante ahora está abierto. Luego cree una clase 
Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado sabores que almacene una lista de los 
sabores de helado disponibles. Escriba también un método que muestre estos valores, cree una instancia de la clase y llame 
al método."""

# class Restaurante:
#     def __init__(self,nombre,tipo, estado):
#         self.nombre = nombre
#         self.tipo = tipo
#         self.estado = estado
#     def DescribirRestaurante(self):
#         print(f""" 
#               NOMBRE DEL RESTAURANTE: {self.nombre}
#               TIPOS DE COMIDA: {self.tipo}
#               ESTADO: {self.estado}  """)
#     def Abrir(self):
#         if self.estado.lower() == "cerrado":    
#             print(f'el {self.nombre} esta abierto ahora')
#             self.estado = "abierto".lower()

# class Heladeria(Restaurante):
#     def __init__ (self,nombre,tipo, estado, sabores):
#         super().__init__(nombre,tipo, estado)
#         self.sabores = sabores
#     def MostrarSabores(self):
#         print(f"""LOS SABORES SON: {self.sabores}""")


# italy_pizzeria = Restaurante("ItalyPizzeri","Restauran","abierto")
# grido = Heladeria("Grido", "Helados", "cerrado", ["menta granizada","chocolate","frutilla"])

# grido.DescribirRestaurante()
# grido.Abrir()
# grido.DescribirRestaurante()

"""5) Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, y los métodos recibir_ataque, que 
reduzca la vida según una cantidad recibida y lance una excepción si la vida pasa a ser menor o igual que cero, y mover 
que reciba una dirección y se mueva en esa dirección la cantidad indicada por velocidad.
 Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método atacar, que reciba otro 
personaje, al que le debe hacer el daño indicado por el atributo ataque.
 Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método cosechar, que 
devuelva la cantidad cosechad"""

# class Personaje():
#     def __init__(self,vida,posicion,velocidad):
#         self.vida = vida
#         self.posicion = posicion
#         self.velocidad = velocidad
#     def RecibirAtaque(self, daño):
#         try:
#             daño_recibido = self.vida - daño
#             if self.vida >= 1:
#                 print(f'has recibido daño, vida actual: {daño_recibido}')
#                 self.vida -= daño_recibido
#         except:
#             if self.vida <= 0:
#                 return 'te quedaste sin vida, has muerto'
    
#     def Mover(self,direccion,distancia):
#         print (f' te has movido {distancia} hacia {direccion} a una velocidad de {self.velocidad}')

# class Soldado(Personaje):
#     def __init__(self, vida,posicion,velocidad, ataque):
#         super().__init__(vida,posicion,velocidad)
#         self.ataque = ataque
#     def Atacar(self,otro):
#         otro.RecibirAtaque(self.ataque)
#         return (f'has acertado -{self.ataque}')
# class Campesino(Personaje):
#     def __init__(self,vida,posicion,velocidad,cosecha):
#         super().__init__(vida,posicion,velocidad)
#         self.cosecha = cosecha
#     def Cosechar(self):
#         print (f'has cosechado +10 trigo')
#         self.cosecha += 10

# vegeta = Soldado(100,"soldado","50m/s",20)
# granjero = Campesino(75,"campesino", "20m/s",30)
# bulma = Personaje(50,"personaje","50m/s")

# print(bulma.vida)
# vegeta.Atacar(bulma)
# granjero.Cosechar()
# print(granjero.cosecha)

"""6) Usuarios: Cree una clase Usuario. Cree también dos atributos nombre y apellido, así como otros atributos que típicamente 
se guardan en un perfil de usuario. Escriba un método describir_usuario() que muestre un resumen de la información del 
usuario. Escriba otro método saludar_usuario() que muestre un saludo personalizado al usuario.
Cree varias instancias que representen distintos usuarios y llame ambos métodos para cada uno.
"""
# class Usuario:
#     def __init__(self,nombre,apellido,nombre_usuario,edad):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.nombre_usuario = nombre_usuario
#         self.edad = edad
#     def DescribirUsuario(self):
#         print(f"""
#                   Nombre: {self.nombre}
#                   Apellido: {self.apellido}
#                   Nombre de usuario: {self.nombre_usuario}
#                   Edad: {self.edad}          """)
#     def SaludarUsuario(self,saludo_personalizado):
#         print(saludo_personalizado)

# martin = Usuario("Martin","Figueroa","chicho24",18)
# santiago = Usuario("santiago",'Mac Gaul','magolsitosan',21)
# pedro = Usuario('Pedro','Gomez','pedritroclavito',50)

# Saludo = input('ingrese un saludo personalizado: ')
# martin.DescribirUsuario()
# martin.SaludarUsuario(Saludo)

# Saludo = input('ingrese un saludo personalizado: ')
# santiago.DescribirUsuario()
# santiago.SaludarUsuario(Saludo)

# Saludo = input('ingrese un saludo personalizado: ')
# pedro.DescribirUsuario()
# pedro.SaludarUsuario(Saludo)

"""7) Admin: Un administrador es un tipo de usuario con privilegios especiales. Cree una clase Admin que herede de la clase 
Usuario del ejercicio anterior y agréguele un atributo privilegios que almacene una lista de strings tales como “puede 
postear en el foro”, “puede borrar un post”, “puede banear usuario”, etc. Escriba un método mostrar_privilegios() que 
muestre el conjunto de privilegios del administrador, cree una instancia de la clase y llame al método.
"""
# class Admin(Usuario):
#     def __init__(self,nombre,apellido,nombre_usuario,edad,privilegios):
#         super().__init__(nombre,apellido,nombre_usuario,edad)
#         self.privilegios = privilegios

    # def MostrarPrivilegios(self):
    #     print(f""" 
    #             Privilegios del Admin:
    #             1-{self.privilegios[0]}
    #             2-{self.privilegios[1]}
    #             3-{self.privilegios[2]} """)
# administrador = Admin('juan','perez','juanpere',100,["puede postear en el foro", "puede borrar un post", "puede banear usuario"])
# administrador.MostrarPrivilegios()

"""8) Privilegios: Escriba una clase Privilegios. La clase debería tener un atributo, privilegios, que almacene una lista de strings 
con los privilegios de manera similar a la del ejercicio 7. Mueva el método mostrar_privilegios() de ese ejercicio a esta 
clase, y haga que una instancia de esta clase sea un atributo de la clase Admin. Cree una nueva instancia de Admin y use 
el método para mostrar privilegios.
"""
# class Privilegios(Admin):
#     def __init__(self,privilegio):
#         self.privilegio = privilegio
#     def MostrarPrivilegios(self):
#         print(f""" 
#             Privilegios del Admin:
#             1-{self.privilegio[0]}
#             2-{self.privilegio[1]}
#             3-{self.privilegio[2]} """)
        
# clase_privilegios = Privilegios(["puede postear en el foro", "puede borrar un post", "puede banear usuario"])
# administrador = Admin('juan','perez','juanpere',100,clase_privilegios)

# administrador.privilegios.MostrarPrivilegios()
"""9) Restaurante importado: Escriba un programa que esté en otro archivo que la clase Restaurante del ejercicio 4, e impórtela 
al módulo actual. Cree una instancia de Restaurante y llame a alguno de sus métodos para asegurarse que la importación 
funcionó."""
# from Restaurante import Restaurante_Importado,Heladeria

# RestauranteImportado = Restaurante_Importado("Rapi","comida rapida","cerrado")


# RestauranteImportado.Abrir()
# RestauranteImportado.DescribirRestaurante()

"""10) (Opcional): Repita el ejercicio anterior pero esta vez importando la clase Heladeria. ¿Qué se necesita para que funcione la 
importación"""

# HeladeriaImportada = Heladeria("grido","Helados","cerrado",['menta granizada', 'chocolate', 'crema americana'])
# HeladeriaImportada.DescribirRestaurante()
# HeladeriaImportada.Abrir
# HeladeriaImportada.MostrarSabores()