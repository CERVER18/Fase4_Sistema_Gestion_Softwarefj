from cliente import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from gestor import GestorSistema
from excepciones import ErrorValidacion

def ejecutar_simulacion():
    print("=== INICIANDO SISTEMA SOFTWARE FJ ===\n")

    gestor = GestorSistema()

    # ==============================
    # CATÁLOGO DE SERVICIOS
    # ==============================

    sala = ReservaSala("SRV-1", "Sala de Juntas", 80000)
    equipo = AlquilerEquipo("SRV-2", "Laptop Pro", 45000)
    asesoria = AsesoriaEspecializada("SRV-3", "Asesoría Python", 150000)

    gestor.servicios.extend([sala, equipo, asesoria])

    # ==============================
    # 10 OPERACIONES DEL SISTEMA
    # ==============================

    operaciones = [

        # 1. CLIENTE VÁLIDO
        {
            "id": 101,
            "c_id": 102030,
            "nom": "Patricia Meneses",
            "mail": "pmeneses@gmail.com",
            "srv": sala,
            "dur": 3,
            "opts": {"limpieza": True}
        },

        # 2. EMAIL INVÁLIDO
        {
            "id": 102,
            "c_id": 203040,
            "nom": "Ricardo",
            "mail": "ricardo.com",
            "srv": equipo,
            "dur": 5,
            "opts": {}
        },

        # 3. NOMBRE INVÁLIDO
        {
            "id": 103,
            "c_id": 304050,
            "nom": "M",
            "mail": "mario@mail.com",
            "srv": asesoria,
            "dur": 2,
            "opts": {}
        },

        # 4. DESCUENTO VÁLIDO
        {
            "id": 104,
            "c_id": 405060,
            "nom": "Carlos Ruiz",
            "mail": "carlos@mail.com",
            "srv": asesoria,
            "dur": 2,
            "opts": {"descuento": 50000}
        },

        # 5. DESCUENTO INVÁLIDO
        {
            "id": 105,
            "c_id": 506070,
            "nom": "Ana Gil",
            "mail": "ana@mail.com",
            "srv": asesoria,
            "dur": 1,
            "opts": {"descuento": 200000}
        },

        # 6. DURACIÓN INVÁLIDA
        {
            "id": 106,
            "c_id": 607080,
            "nom": "Luis Paz",
            "mail": "luis@mail.com",
            "srv": sala,
            "dur": "dos",
            "opts": {}
        },

        # 7. RESERVA CORRECTA
        {
            "id": 107,
            "c_id": 708090,
            "nom": "Dora Martinez",
            "mail": "dora@mail.com",
            "srv": equipo,
            "dur": 4,
            "opts": {"seguro": False}
        },

        # 8. SERVICIO NULO
        {
            "id": 108,
            "c_id": 809100,
            "nom": "Pedro Gomez",
            "mail": "pedro@mail.com",
            "srv": None,
            "dur": 2,
            "opts": {}
        },

        # 9. RESERVA EXITOSA
        {
            "id": 109,
            "c_id": 901011,
            "nom": "Sofia Lopez",
            "mail": "sofia@mail.com",
            "srv": sala,
            "dur": 5,
            "opts": {"limpieza": False}
        },

        # 10. RESERVA EXITOSA CON SEGURO
        {
            "id": 110,
            "c_id": 100112,
            "nom": "Raul Garcia",
            "mail": "raul@mail.com",
            "srv": equipo,
            "dur": 10,
            "opts": {"seguro": True}
        }
    ]

    # ==============================
    # EJECUCIÓN DE OPERACIONES
    # ==============================

    for op in operaciones:

        print(f"\n========== OPERACIÓN #{op['id']} ==========")

        try:

            # ==============================
            # CREACIÓN DEL CLIENTE
            # ==============================

            cliente_obj = Cliente(
                op["c_id"],
                op["nom"],
                op["mail"]
            )

            gestor.agregar_cliente(cliente_obj)

            # ==============================
            # CREACIÓN DE LA RESERVA
            # ==============================

            reserva_obj = Reserva(
                op["id"],
                cliente_obj,
                op["srv"],
                op["dur"]
            )

            # ==============================
            # CONFIRMACIÓN DE RESERVA
            # ==============================

            reserva_obj.confirmar(**op["opts"])

            # ==============================
            # REGISTRO EN HISTORIAL
            # ==============================

            gestor.registrar_operacion(reserva_obj)

            print(f"✅ Reserva procesada correctamente para {cliente_obj.nombre}")

        except ErrorValidacion as ev:

            print("❌ ERROR DE VALIDACIÓN")
            print(f"Detalle: {ev}")

        except Exception as e:

            print("⚠️ ERROR OPERATIVO CONTROLADO")
            print(f"Tipo: {e.__class__.__name__}")
            print(f"Detalle: {e}")

    # ==============================
    # RESUMEN FINAL
    # ==============================

    print("\n===================================")
    print("✅ SIMULACIÓN FINALIZADA")
    print("===================================\n")

    print(f"👥 Clientes válidos registrados: {len(gestor.clientes)}")
    print(f"📅 Reservas exitosas: {len(gestor.reservas_historial)}")
    print("📝 Revisar logs/sistema_fj.log para auditoría completa.")

# ==================================
# PUNTO DE ENTRADA PRINCIPAL
# ==================================

if __name__ == "__main__":
    ejecutar_simulacion()
