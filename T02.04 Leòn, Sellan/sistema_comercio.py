# archivo: sistema_comercio.py

class Cliente:
    """Clase que representa a un cliente en el sistema."""

    def __init__(self, id_cliente: int, nombre: str, telefono: str):
        self.id_cliente = id_cliente  # ID único del cliente
        self.nombre = nombre          # Nombre del cliente
        self.telefono = telefono      # Teléfono del cliente

    def actualizar_telefono(self, nuevo_telefono: str):
        """Actualiza el número de teléfono del cliente."""
        self.telefono = nuevo_telefono

    def __str__(self) -> str:
        return f"{self.nombre} ({self.telefono})"

class Producto:
    """Clase que representa un producto en el sistema."""

    def __init__(self, id_producto: int, nombre: str, precio: float):
        self.id_producto = id_producto  # ID único del producto
        self.nombre = nombre            # Nombre del producto
        self.precio = precio            # Precio del producto

    def aplicar_descuento(self, porcentaje: float):
        """Aplica un descuento al producto."""
        self.precio *= (1 - porcentaje / 100)

    def __str__(self) -> str:
        return f"{self.nombre} - ${self.precio:.2f}"

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

class Factura:
    """Clase que representa una factura en el sistema."""

    def __init__(self, id_factura: int, orden: Orden):
        self.id_factura = id_factura  # ID único de la factura
        self.orden = orden            # Orden asociada a la factura

    def generar_factura(self) -> str:
        """Genera la representación textual de la factura."""
        return f"Factura {self.id_factura}\n{str(self.orden)}"
    
    def __str__(self) -> str:
        return self.generar_factura()
