""" Clase cliente """

class Cliente:

    def __init__(self,usuario,mail,edad,categorias):
        self.usuario = usuario
        self.mail = mail
        self.edad = edad
        self.categorias = categorias

    def __str__(self):
        return f"Los datos del cliente son: {self.usuario}, {self.mail}, {self.edad} y {self.categorias}"
pass