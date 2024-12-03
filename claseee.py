class Paquete:
    def __init__(self):
        self.__peso = 0
        self.__tarifaBase = 200
        self.__tarifaAdicionalPorKg = 40
        self.__tarifaEspecial = 300
        self.__costoTotal = 0 

    def calcularCostoTotal(self, peso):
        if peso <= 0:
            raise ValueError("Ingresa números reales.")

        self.__peso = peso 
        
 
        if peso <= 5:
            self.__costoTotal = self.__tarifaBase
        elif peso <= 20:
            self.__costoTotal = self.__tarifaBase + (peso - 5) * self.__tarifaAdicionalPorKg
        else:
            self.__costoTotal = (
                self.__tarifaBase + 
                (20 - 5) * self.__tarifaAdicionalPorKg + 
                self.__tarifaEspecial
            )

        return self.__costoTotal

    def obtenerCostoTotal(self):
        
        return self.__costoTotal
