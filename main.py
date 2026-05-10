from cliente import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from gestor import GestorSistema
from excepciones import ErrorValidacion

def ejecutar_simulacion():
    print("=== INICIANDO SISTEMA SOFTWARE FJ ===")
    gestor = GestorSistema()

    # Catálogo de servicios
    sala = ReservaSala("SRV-1", "Sala de Juntas", 80000)
    equipo = AlquilerEquipo("SRV-2", "Laptop Pro", 45000)
    asesoria = AsesoriaEspecializada("SRV-3", "Asesoría Python", 150000)

    gestor.servicios.extend([sala, equipo, asesoria])

    # 10 OPERACIONES (Múltiples escenarios de éxito y error)
    operaciones = [
        # 1. OK (Con limpieza)
        {"id": 101, "c_id": 1, "nom": "Juan Perez", "mail": "juan@mail.com", "srv": sala, "dur": 3, "opts": {"limpieza": True}},
        # 2. ERROR: Email inválido (Falla validación Cliente)
        {"id": 102, "c_id": 2, "nom": "Maria Lopez", "mail": "maria.com", "srv": equipo, "dur": 5, "opts": {}},
        # 3. OK (Descuento válido)
        {"id": 103, "c_id": 3, "nom": "Carlos Ruiz", "mail": "carlos@mail.com", "srv": asesoria, "dur": 2, "opts": {"descuento": 50000}},
        # 4. ERROR: Descuento mayor al costo (Falla cálculo)
        {"id": 104, "c_id": 4, "nom": "Ana Gil", "mail": "ana@mail.com", "srv": asesoria, "dur": 1, "opts": {"descuento": 200000}},
        # 5. ERROR: Duración es un string en vez de número (TypeError)
        {"id": 105, "c_id": 5, "nom": "Luis Paz", "mail": "luis@mail.com", "srv": sala, "dur": "dos", "opts": {}},
        # 6. OK (Sin seguro)
        {"id": 106, "c_id": 6, "nom": "Dora M", "mail": "dora@mail.com", "srv": equipo, "dur": 4, "opts": {"seguro": False}},
        # 7. ERROR: Servicio Nulo
        {"id": 107, "c_id": 7, "nom": "Pedro X", "mail": "pedro@mail.com", "srv": None, "dur": 2, "opts": {}},
        # 8. ERROR: Nombre muy corto
        {"id": 108, "c_id": 8, "nom": "A", "mail": "a@mail.com", "srv": sala, "dur": 1, "opts": {}},
        # 9. OK
        {"id": 109, "c_id": 9, "nom": "Sofia L", "mail": "sofia@mail.com", "srv": sala, "dur": 5, "opts": {"limpieza": False}},
        # 10. OK
        {"id": 110, "c_id": 10, "nom": "Raul G", "mail": "rg@mail.com", "srv": equipo, "dur": 10, "opts": {"seguro": True}}
    ]

    # Ejecución secuencial
    for op in operaciones:
        try:
            # 1. Intentamos crear el cliente
            cliente_obj = Cliente(op["c_id"], op["nom"], op["mail"])
            gestor.agregar_cliente(cliente_obj)
            
            # 2. Intentamos crear y procesar la reserva
            reserva_obj = Reserva(op["id"], cliente_obj, op["srv"], op["dur"])
            reserva_obj.confirmar(**op["opts"])
            
            # 3. Guardamos en listas
            gestor.registrar_operacion(reserva_obj)

        except ErrorValidacion as ev:
            print(f"\n--- Procesando Reserva #{op['id']} ---")
            print(f"❌ FALLO DE VALIDACIÓN AL CREAR CLIENTE: {ev}")
        except Exception as e:
            # Este bloque captura el error encadenado (raise from) para no detener el ciclo
            print(f"⚠️ El sistema ha contenido un error operativo: {e.__class__.__name__}")

    print("\n=== SIMULACIÓN FINALIZADA CORRECTAMENTE ===")
    print(f"Total clientes registrados: {len(gestor.clientes)}")
    print(f"Total reservas procesadas: {len(gestor.reservas_historial)}")

if __name__ == "__main__":
    ejecutar_simulacion()
