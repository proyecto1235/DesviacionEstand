import unittest

# Definición de Excepciones
class NoSePuedeCalcular(Exception):
    """Excepción lanzada cuando no se puede calcular un valor debido a datos inválidos."""
    pass

class ExcepcionDatos(Exception):
    """Excepción lanzada por datos no numéricoss."""
    pass

# Clase Conjunto
class Conjunto:
    def _init_(self, elementos):
        self.elementos = elementos

    def media(self):
        # 1.1 Caso sin elementos
        if len(self.elementos) == 0:
            raise NoSePuedeCalcular("No se puede calcular la media de un conjunto vacío.")

        # 1.7 Caso con elementos no numéricos
        for elem in self.elementos:
            if not isinstance(elem, (int, float)):
                raise ExcepcionDatos(f"El elemento {elem} no es numérico.")

        # 1.2 Caso con un solo elemento
        if len(self.elementos) == 1:
            return self.elementos[0]

        # 1.3 Caso con dos elementos
        return sum(self.elementos) / len(self.elementos)

    def desviacion_estandar(self):
        # 2.1 Caso sin elementos
        if len(self.elementos) == 0:
            raise NoSePuedeCalcular("No se puede calcular la desviación estándar de un conjunto vacío.")

        # 2.7 Caso con elementos no numéricos
        for elem in self.elementos:
            if not isinstance(elem, (int, float)):
                raise ExcepcionDatos(f"El elemento {elem} no es numérico.")

        # 2.2 Caso con un solo elemento
        if len(self.elementos) == 1:
            return 0.0

        # Calcular la media
        promedio = sum(self.elementos) / len(self.elementos)

        # 2.4 Calcular la desviación estándar
        suma_cuadrados = sum((x - promedio) ** 2 for x in self.elementos)
        desviacion_estandar = (suma_cuadrados / len(self.elementos)) ** 0.5

        return desviacion_estandar

# Clase de Test
class TestConjunto(unittest.TestCase):
    def test_media(self):
        # 1.1 Caso sin elementos
        conjunto = Conjunto([])
        with self.assertRaises(NoSePuedeCalcular):
            conjunto.media()

        # 1.2 Caso con un solo elemento
        conjunto = Conjunto([3.5])
        self.assertEqual(conjunto.media(), 3.5)

        # 1.3 Caso con dos elementos
        conjunto = Conjunto([4, 6])
        self.assertAlmostEqual(conjunto.media(), 5.0)

        # 1.4 Caso con n elementos positivos
        conjunto = Conjunto([4, 6, 8, 12.5])
        self.assertAlmostEqual(conjunto.media(), 7.625)

        # 1.5 Caso con n elementos donde todos son ceros
        conjunto = Conjunto([0, 0, 0, 0])
        self.assertEqual(conjunto.media(), 0.0)

        # 1.6 Caso con n elementos positivos y negativos
        conjunto = Conjunto([3.5, 8, -4.2])
        self.assertAlmostEqual(conjunto.media(), 2.433333333333333, places=6)

        # 1.7 Caso con n elementos no numéricos
        conjunto = Conjunto([5, "4.5"])
        with self.assertRaises(ExcepcionDatos):
            conjunto.media()

        conjunto = Conjunto([8, "a"])
        with self.assertRaises(ExcepcionDatos):
            conjunto.media()

    def test_desviacion_estandar(self):
        # 2.1 Caso sin elementos
        conjunto = Conjunto([])
        with self.assertRaises(NoSePuedeCalcular):
            conjunto.desviacion_estandar()

        # 2.2 Caso con un solo elemento
        conjunto = Conjunto([5])
        self.assertEqual(conjunto.desviacion_estandar(), 0.0)

        # 2.3 Caso con dos elementos
        conjunto = Conjunto([5, 7])
        self.assertAlmostEqual(conjunto.desviacion_estandar(), 1.0)

        # 2.4 Caso con n elementos positivos
        conjunto = Conjunto([4, 6, 8, 12.5])
        self.assertAlmostEqual(conjunto.desviacion_estandar(), 2.5000000000000004, places=6)

        # 2.5 Caso con n elementos donde todos son ceros
        conjunto = Conjunto([0, 0, 0, 0])
        self.assertEqual(conjunto.desviacion_estandar(), 0.0)

        # 2.6 Caso con n elementos positivos y negativos
        conjunto = Conjunto([3.5, 8, -4.2])
        self.assertAlmostEqual(conjunto.desviacion_estandar(), 4.537249881199995, places=6)

        # 2.7 Caso con n elementos no numéricos
        conjunto = Conjunto([5, "4.5"])
        with self.assertRaises(ExcepcionDatos):
            conjunto.desviacion_estandar()

        conjunto = Conjunto([8, "a"])
        with self.assertRaises(ExcepcionDatos):
            conjunto.desviacion_estandar()

# Ejecución de Pruebas
if _name_ == "_main_":
    unittest.main()