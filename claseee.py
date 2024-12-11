class paquete():
    __peso = 0
    __tarifaBase = 200
    __tarifaAdicionalPorKg = 40
    __tarifaEspecial = 300
    __costoTotal = 0  
    
    def calcularCosto(self, peso):
        if peso <= 0:
            raise ValueError("Ingresa números reales.")
        elif peso <= 5:
            self.__costoTotal = self.__tarifaBase
        elif peso <= 20:
            self.__costoTotal = self.__tarifaBase + (peso - 5) * self.__tarifaAdicionalPorKg
        else:
            self.__costoTotal = self.__tarifaBase + (20 - 5) * self.__tarifaAdicionalPorKg + self.__tarifaEspecial
        return self.__costoTotal
            
    def TarifaAdicional(self):
         return self.__costoTotal
