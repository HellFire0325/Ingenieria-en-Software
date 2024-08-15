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
