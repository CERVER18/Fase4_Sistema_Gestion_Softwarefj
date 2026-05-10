# Software FJ — Sistema Integral de Gestión de Clientes, Servicios y Reservas

Sistema orientado a objetos desarrollado en Python para la gestión de clientes, servicios y reservas de la empresa Software FJ. Proyecto académico del curso **Programación Orientada a Objetos (Código 213023)** — Universidad Nacional Abierta y a Distancia (UNAD).

---

## 📋 Descripción general
El sistema permite registrar clientes, gestionar un catálogo de servicios (salas, equipos y asesorías) y administrar reservas con un ciclo de vida completo. Toda la información se mantiene en memoria mediante objetos y listas, sin uso de base de datos. Los errores y eventos se registran automáticamente en un archivo de logs.

---

## 🧠 Principios de Programación Orientada a Objetos aplicados
* **Abstracción:** Implementación de clases abstractas `EntidadSistema` y `Servicio` que definen la estructura base.
* **Herencia:** Clases `Cliente`, `ReservaSala`, `AlquilerEquipo` y `AsesoriaEspecializada` heredan de las clases base.
* **Polimorfismo y Sobrecarga:** Cada servicio calcula su costo de forma diferente usando el mismo método `calcular_costo()`. La sobrecarga se logró implementando `**kwargs`.
* **Encapsulación:** Atributos protegidos y privados (`__nombre`, `__email`) con validación a través de *Getters* y *Setters*.
* **Manejo avanzado de excepciones:** Excepciones personalizadas, bloques `try/except/else/finally`, y encadenamiento de excepciones (`raise ... from`) para garantizar la estabilidad operativa.

---

## 📂 Estructura Modular del Proyecto
El código se desarrolló en una arquitectura de 8 módulos:
```text
sistema-gestion-softwarefj/
│
├── excepciones.py    # Módulo 1 - Excepciones jerárquicas del sistema
├── logger.py         # Módulo 2 - Sistema de registro de eventos (Logs)
├── entidad_base.py   # Módulo 3 - Clase abstracta base
├── cliente.py        # Módulo 4 - Cliente con encapsulación estricta
├── servicios.py      # Módulo 5 - Servicios con herencia y polimorfismo
├── reserva.py        # Módulo 6 - Ciclo de vida y try/except/else/finally
├── gestor.py         # Módulo 7 - Manejo de listas internas
├── main.py           # Módulo 8 - Simulación de 10 operaciones secuenciales
├── interfaz.py       # Módulo 9 - Interfaz gráfica interactiva (Tkinter)
└── logs/
    └── sistema_fj.log # Archivo generado automáticamente con los errores
