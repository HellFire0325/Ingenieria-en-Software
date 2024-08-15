import Orden
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
