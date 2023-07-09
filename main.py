from paquete.clase_cliente import Cliente
from paquete.funciones_entrega_1 import *

cliente1 = Cliente("Maxi","maxi@gmail",30)
cliente2= Cliente("Carlos","carlos@gmail.com",27,"")

print(cliente1)
print(cliente1.compra("computacion", "notebook"))
print(cliente1.compra("computacion","headset"))
cliente1.historial_de_transacciones()
print(cliente2.compra("computacion","teclado"))
print(cliente2.compra("electrodomesticos","heladera"))
cliente2.historial_de_transacciones()