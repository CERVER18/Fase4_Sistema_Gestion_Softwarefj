from entidad_base import EntidadSistema
from abc import abstractmethod

class Servicio(EntidadSistema):
    def __init__(self, id_servicio, nombre, tarifa_base):
        super().__init__(id_servicio)
        self.nombre = nombre
        self.tarifa_base = tarifa_base

    @abstractmethod
    def calcular_costo(self, cantidad, **kwargs):
        """Método polimórfico a sobrescribir."""
        pass

class ReservaSala(Servicio):
    def calcular_costo(self, horas, limpieza=False):
        if type(horas) not in [int, float] or horas <= 0:
            raise ValueError("Las horas deben ser un número positivo.")
        total = self.tarifa_base * horas
        return total + 50000 if limpieza else total

class AlquilerEquipo(Servicio):
    def calcular_costo(self, dias, seguro=True):
        if type(dias) not in [int, float] or dias <= 0:
            raise ValueError("Los días deben ser un número positivo.")
        total = self.tarifa_base * dias
        return total * 1.15 if seguro else total

class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, sesiones, descuento=0):
        total = (self.tarifa_base * sesiones) - descuento
        if total < 0:
            raise ValueError("El descuento no puede ser mayor al costo total.")
        return total
