# archivo: test_sistema_comercio.py

import unittest
from sistema_comercio import Cliente, Producto, Orden, Factura

class TestCliente(unittest.TestCase):
    
    def setUp(self):
        self.cliente = Cliente(1, "Juan Pérez", "123456789")
    
    def test_actualizar_telefono(self):
        self.cliente.actualizar_telefono("987654321")
        self.assertEqual(self.cliente.telefono, "987654321")
    
    def test_str(self):
        self.assertEqual(str(self.cliente), "Juan Pérez (987654321)")

class TestProducto(unittest.TestCase):
    
    def setUp(self):
        self.producto = Producto(1, "Laptop", 1000.00)
    
    def test_aplicar_descuento(self):
        self.producto.aplicar_descuento(10)
        self.assertEqual(self.producto.precio, 900.00)
    
    def test_str(self):
        self.assertEqual(str(self.producto), "Laptop - $900.00")

class TestOrden(unittest.TestCase):
    
    def setUp(self):
        self.cliente = Cliente(1, "Juan Pérez", "123456789")
        self.orden = Orden(1, self.cliente)
        self.producto1 = Producto(1, "Laptop", 1000.00)
        self.producto2 = Producto(2, "Ratón", 50.00)
    
    def test_agregar_producto(self):
        self.orden.agregar_producto(self.producto1)
        self.orden.agregar_producto(self.producto2)
        self.assertIn(self.producto1, self.orden.productos)
        self.assertIn(self.producto2, self.orden.productos)
    
    def test_calcular_total(self):
        self.orden.agregar_producto(self.producto1)
        self.orden.agregar_producto(self.producto2)
        self.assertEqual(self.orden.calcular_total(), 1050.00)
    
    def test_str(self):
        self.orden.agregar_producto(self.producto1)
        self.assertEqual(str(self.orden), "Orden 1 por Juan Pérez: Laptop - $1000.00 - Total: $1000.00")

class TestFactura(unittest.TestCase):
    
    def setUp(self):
        self.cliente = Cliente(1, "Juan Pérez", "123456789")
        self.orden = Orden(1, self.cliente)
        self.factura = Factura(1, self.orden)
    
    def test_generar_factura(self):
        self.orden.agregar_producto(Producto(1, "Laptop", 1000.00))
        self.orden.agregar_producto(Producto(2, "Ratón", 50.00))
        expected_factura = "Factura 1\nOrden 1 por Juan Pérez: Laptop, Ratón - Total: $1050.00"
        self.assertEqual(self.factura.generar_factura(), expected_factura)
    
    def test_str(self):
        self.orden.agregar_producto(Producto(1, "Laptop", 1000.00))
        self.assertEqual(str(self.factura), "Factura 1\nOrden 1 por Juan Pérez: Laptop - $1000.00 - Total: $1000.00")

if __name__ == "__main__":
    unittest.main()
