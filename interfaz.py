import tkinter as tk
from tkinter import ttk, messagebox
from cliente import Cliente
from servicios import ReservaSala, AlquilerEquipo
from reserva import Reserva
from gestor import Gestor
from excepciones import ErrorValidacion, ErrorOperativo
from logger import registrar

class InterfazSoftwareFJ:
    def __init__(self, root):
        self.root = root
        self.root.title("Software FJ - Gestión de Reservas")
        self.root.geometry("450x500")
        self.root.config(padx=20, pady=20)
        
        # Inicializamos el gestor y un catálogo base de servicios
        self.gestor = Gestor()
        self.sala = ReservaSala("SRV-001", "Sala de Juntas VIP", 80000)
        self.equipo = AlquilerEquipo("SRV-002", "Laptop Dell Pro", 45000)
        
        self.crear_interfaz()

    def crear_interfaz(self):
        # --- SECCIÓN CLIENTE ---
        frame_cliente = tk.LabelFrame(self.root, text=" Datos del Cliente ", padx=10, pady=10)
        frame_cliente.pack(fill="x", pady=5)

        tk.Label(frame_cliente, text="Documento:").grid(row=0, column=0, sticky="w")
        self.ent_id = tk.Entry(frame_cliente, width=30)
        self.ent_id.grid(row=0, column=1, pady=2)

        tk.Label(frame_cliente, text="Nombre:").grid(row=1, column=0, sticky="w")
        self.ent_nombre = tk.Entry(frame_cliente, width=30)
        self.ent_nombre.grid(row=1, column=1, pady=2)

        tk.Label(frame_cliente, text="Email:").grid(row=2, column=0, sticky="w")
        self.ent_email = tk.Entry(frame_cliente, width=30)
        self.ent_email.grid(row=2, column=1, pady=2)

        # --- SECCIÓN SERVICIO ---
        frame_servicio = tk.LabelFrame(self.root, text=" Detalles del Servicio ", padx=10, pady=10)
        frame_servicio.pack(fill="x", pady=5)

        tk.Label(frame_servicio, text="Servicio:").grid(row=0, column=0, sticky="w")
        self.combo_srv = ttk.Combobox(frame_servicio, values=["Sala de Juntas", "Alquiler de Equipo"], state="readonly", width=27)
        self.combo_srv.current(0)
        self.combo_srv.grid(row=0, column=1, pady=2)

        tk.Label(frame_servicio, text="Cantidad/Horas:").grid(row=1, column=0, sticky="w")
        self.ent_cantidad = tk.Entry(frame_servicio, width=30)
        self.ent_cantidad.grid(row=1, column=1, pady=2)

        # --- BOTÓN DE PROCESAR ---
        btn_procesar = tk.Button(self.root, text="Confirmar Reserva", bg="#0052cc", fg="white", font=("Arial", 10, "bold"), command=self.procesar_reserva)
        btn_procesar.pack(pady=15, fill="x")

        # --- CONSOLA DE SALIDA ---
        tk.Label(self.root, text="Registro de Operaciones:").pack(anchor="w")
        self.txt_log = tk.Text(self.root, height=8, state="disabled", bg="#f4f4f4")
        self.txt_log.pack(fill="both", expand=True)

    def log_interfaz(self, mensaje):
        """Escribe mensajes en el cuadro de texto de la interfaz."""
        self.txt_log.config(state="normal")
        self.txt_log.insert(tk.END, mensaje + "\n")
        self.txt_log.see(tk.END)
        self.txt_log.config(state="disabled")

    def procesar_reserva(self):
        try:
            # Captura de datos
            doc = self.ent_id.get()
            nom = self.ent_nombre.get()
            mail = self.ent_email.get()
            
            # Validación de cantidad numérica en la interfaz
            if not self.ent_cantidad.get().isdigit():
                raise ValueError("La cantidad o duración debe ser un número entero.")
            cant = int(self.ent_cantidad.get())

            # 1. Creación del Cliente (Puede lanzar ErrorValidacion)
            cliente = Cliente(doc, nom, mail)
            
            # 2. Selección del Servicio
            seleccion = self.combo_srv.get()
            servicio = self.sala if seleccion == "Sala de Juntas" else self.equipo
            opciones = {"limpieza": True} if seleccion == "Sala de Juntas" else {"seguro": True}

            # 3. Creación y Confirmación de la Reserva
            reserva = Reserva(f"RES-{doc[-3:]}", cliente, servicio, cant)
            costo_total = reserva.confirmar(**opciones)
            
            # 4. Guardar en el Gestor
            self.gestor.guardar(reserva)

            # Notificar éxito
            self.log_interfaz(f"✅ ÉXITO: {servicio.nombre} para {cliente.nombre}. Total: ${costo_total}")
            messagebox.showinfo("Reserva Exitosa", f"La reserva se ha procesado con un costo de ${costo_total}")

        except ErrorValidacion as e:
            self.log_interfaz(f"❌ ERROR DATOS: {e}")
            messagebox.showerror("Error de Validación", str(e))
        except ErrorOperativo as e:
            self.log_interfaz(f"❌ ERROR OPERATIVO: {e}")
            messagebox.showerror("Error Operativo", str(e))
        except Exception as e:
            self.log_interfaz(f"⚠️ ERROR CRÍTICO: {e}")
            messagebox.showerror("Error del Sistema", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazSoftwareFJ(root)
    root.mainloop()
