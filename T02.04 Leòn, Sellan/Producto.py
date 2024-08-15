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