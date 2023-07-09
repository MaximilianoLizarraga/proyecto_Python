""" Clase cliente """

class Cliente:

    def __init__(self,usuario,mail,edad,domicilio):
        self.usuario = usuario
        self.mail = mail
        self.edad = edad
        self.domicilio = domicilio
        self.productos = []
        

    def __str__(self):
        return f"Los datos del cliente son: \nUsuario:{self.usuario}, \nMail:{self.mail}, \nEdad:{self.edad}, \nDomicilio: {self.domicilio}"
    
    def compra(self,categoria,nombre):
        self.productos.append(Producto(categoria,nombre))
        return f"Acabas de comprar: {nombre} de la categoria {categoria}!!"
    
    def historial_de_transacciones(self):
        print(f"El historial de compras de {self.usuario} es: ")
        for producto in self.productos:
            print(f"{producto}")

pass

class Producto:

    def __init__(self,categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre

    def __str__(self):
        return f"Categoria:{self.categoria}, Producto:{self.nombre}"

pass