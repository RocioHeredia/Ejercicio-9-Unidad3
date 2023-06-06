from ClassLista import listaVehiculos
from ClassVehiculoNuevo import Vehiculo_Nuevo
from ClassVehiculoUsado import Vehiculo_usado
import unittest
class TestVehiculos(unittest.TestCase):

    def setUp(self):
        self.lista = listaVehiculos()
        self.vehiculo1 = Vehiculo_Nuevo("Modelo1", 4, "Rojo", 20000.0, "Marca1", "Base")
        self.vehiculo2 = Vehiculo_Nuevo("Modelo2", 4, "Azul", 25000.0, "Marca2", "Full")
        self.vehiculo4 = Vehiculo_usado('Modelo4', 4, 'verde', 25000, 'Marca4', 'PGCR1879', 2023, 1500)

    def test_agregar_vehiculo(self):
        self.lista.agregar_vehiculo(self.vehiculo1)
        self.lista.mostrar()

    def test_insertar_vehiculo_posicion_0(self):
        self.lista.agregar_vehiculo(self.vehiculo1)
        self.lista.agregar_vehiculo(self.vehiculo4)
        self.lista.insertar_vehiculo(self.vehiculo2, 0)

    def test_insertar_vehiculo_posicion_intermedia(self):
        self.lista.agregar_vehiculo(self.vehiculo1)
        self.lista.agregar_vehiculo(self.vehiculo2)
        self.lista.insertar_vehiculo(self.vehiculo4, 1)

    def test_insertar_vehiculo_ultima_posicion(self):
        self.lista.agregar_vehiculo(self.vehiculo4)
        self.lista.agregar_vehiculo(self.vehiculo2)
        self.lista.insertar_vehiculo(self.vehiculo1, 2)

    def test_obtener_vehiculo(self):
        self.lista.agregar_vehiculo(self.vehiculo4)
        self.lista.mostrar_tipo_vehiculo(0)

    def test_modificar_precio_base(self):
        self.lista.agregar_vehiculo(self.vehiculo1)
        nuevo_precio = 12000
        self.vehiculo1.set_precio_base(nuevo_precio)
        self.assertEqual(self.vehiculo1.get_precio_B(), nuevo_precio)

if __name__ == '__main__':
    unittest.main()

