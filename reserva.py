from excepciones import ErrorOperativo
from logger import registrar

class Reserva:
    def __init__(self, id_res, cliente, servicio, duracion):
        self.id_res = id_res
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "PENDIENTE"

    def confirmar(self, **opciones):
        print(f"\n--- Procesando Reserva #{self.id_res} ---")
        try:
            # 1. Validación de datos faltantes
            if not self.servicio or not self.cliente:
                raise ErrorOperativo("Datos incompletos: Cliente o Servicio nulo.")
            
            # 2. Llamada polimórfica
            costo = self.servicio.calcular_costo(self.duracion, **opciones)
            
        except Exception as e:
            # 3. Manejo de error y encadenamiento (raise from)
            self.estado = "FALLIDA"
            registrar(f"Error procesando la reserva {self.id_res}: {e}", "error")
            print(f"❌ ERROR: {e}")
            raise ErrorOperativo(f"Fallo crítico en reserva {self.id_res}") from e
            
        else:
            # 4. Bloque ELSE: Solo se ejecuta si NO hubo errores
            self.estado = "CONFIRMADA"
            registrar(f"Reserva {self.id_res} confirmada. Monto: ${costo}")
            print(f"✅ ÉXITO: Reserva confirmada. Total a facturar: ${costo}")
            return costo
            
        finally:
            # 5. Bloque FINALLY: Siempre se ejecuta, haya error o no
            print(f"📌 Estado actual de la transacción #{self.id_res}: {self.estado}")

    def cancelar(self):
        """Implementa la cancelación con manejo estricto de excepciones."""
        print(f"\n--- Solicitud de Cancelación: Reserva #{self.id_res} ---")
        try:
            if self.estado == "CONFIRMADA":
                self.estado = "CANCELADA"
                registrar(f"Reserva {self.id_res} cancelada exitosamente.", "warning")
                print(f"⚠️ RESERVA {self.id_res} CANCELADA.")
            else:
                raise ErrorOperativo(f"No se puede cancelar. Estado actual: {self.estado}")
                
        except ErrorOperativo as e:
            registrar(f"Intento fallido de cancelación en Reserva {self.id_res}: {e}", "error")
            print(f"❌ ERROR AL CANCELAR: {e}")
            raise
