from logger import registrar_log
from excepciones import ErrorOperativo

class Reserva:
    def __init__(self, id_reserva, cliente, servicio, duracion):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "PENDIENTE"

    def confirmar(self, **parametros_extra):
        print(f"\n--- Procesando Reserva #{self.id_reserva} ---")
        try:
            if self.servicio is None or self.cliente is None:
                raise ErrorOperativo("Faltan datos (Cliente o Servicio nulo).")
            
            # Llamada polimórfica
            costo = self.servicio.calcular_costo(self.duracion, **parametros_extra)
            
        except (ValueError, TypeError, ErrorOperativo) as error_interno:
            self.estado = "FALLIDA"
            mensaje_error = f"Fallo operativo en la reserva {self.id_reserva}: {error_interno}"
            registrar_log(mensaje_error, "error")
            print(f"❌ ERROR: {error_interno}")
            # ENCADENAMIENTO DE EXCEPCIONES
            raise ErrorOperativo("La reserva fue abortada por datos inválidos.") from error_interno
            
        except Exception as error_critico:
            self.estado = "ERROR_SISTEMA"
            registrar_log(f"Error crítico inesperado: {error_critico}", "critical")
            print("❌ ERROR CRÍTICO.")
            
        else:
            self.estado = "CONFIRMADA"
            registrar_log(f"Reserva {self.id_reserva} exitosa. Monto: ${costo}")
            print(f"✅ ÉXITO: {self.servicio.nombre} para {self.cliente.nombre}.")
            print(f"💰 Total a facturar: ${costo}")
            return costo
            
        finally:
            print(f"📌 Estado final de transacción #{self.id_reserva}: {self.estado}")
