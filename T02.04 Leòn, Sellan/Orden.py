
import Cliente
import Producto

class Orden:
    """Clase que representa una orden en el sistema."""

    def __init__(self, id_orden: int, cliente: Cliente):
        self.id_orden = id_orden      # ID único de la orden
        self.cliente = cliente        # Cliente que realizó la orden
        self.productos = []           # Lista de productos en la orden

    def agregar_producto(self, producto: Producto):
        """Agrega un producto a la orden."""
        self.productos.append(producto)

    def calcular_total(self) -> float:
        """Calcula el total de la orden."""
        return sum(producto.precio for producto in self.productos)

    def __str__(self) -> str:
        productos_str = ", ".join([producto.nombre for producto in self.productos])
        return f"Orden {self.id_orden} por {self.cliente.nombre}: {productos_str} - Total: ${self.calcular_total():.2f}"
