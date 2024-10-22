class NoSePuedeCalcular(Exception):
    """Excepción lanzada cuando no se puede calcular un valor debido a datos inválidos."""
    pass


class ExcepcionDatos(Exception):
    """Excepción lanzada por datos no numéricos."""
    pass


class Conjunto:
    def __init__(self, elementos):
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
                raise ExcepcionDatos(f"El elemento {elem} no es numérico..")

        # 2.2 Caso con un solo elemento
        if len(self.elementos) == 1:
            return 0.0

        # Calcular la media
        promedio = sum(self.elementos) / len(self.elementos)

        # 2.4 Calcular la desviación estándar
        suma_cuadrados = sum((x - promedio) ** 2 for x in self.elementos)
        desviacion_estandar = (suma_cuadrados / len(self.elementos)) ** 0.5

        return desviacion_estandar
