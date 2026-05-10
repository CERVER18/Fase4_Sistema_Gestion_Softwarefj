# 🚀 Software FJ — Sistema Integral de Gestión de Clientes, Servicios y Reservas

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![POO](https://img.shields.io/badge/Programación-Orientada%20a%20Objetos-success?style=for-the-badge)
![UNAD](https://img.shields.io/badge/UNAD-213023-orange?style=for-the-badge)
![Estado](https://img.shields.io/badge/Estado-Funcional-brightgreen?style=for-the-badge)

### Sistema desarrollado en Python aplicando Programación Orientada a Objetos  
### Gestión de clientes, servicios y reservas para Software FJ

</div>

---

# 📋 Descripción General

Este proyecto implementa un sistema integral orientado a objetos para la gestión de:

- 👤 Clientes
- 🛠️ Servicios especializados
- 📅 Reservas
- ⚠️ Manejo avanzado de excepciones
- 📝 Registro automático de logs

El sistema fue desarrollado sin utilizar bases de datos, empleando exclusivamente:

- Objetos
- Listas
- Archivos de texto para auditoría y logs

El proyecto corresponde al curso:

> **Programación Orientada a Objetos (Código 213023)**  
> Universidad Nacional Abierta y a Distancia — UNAD

---

# 🎯 Objetivo del Proyecto

Desarrollar una aplicación modular, estable y extensible capaz de continuar funcionando incluso cuando ocurren errores durante la ejecución.

El sistema implementa rigurosamente:

- Abstracción
- Herencia
- Polimorfismo
- Encapsulación
- Manejo avanzado de excepciones

---

# 🧠 Principios de Programación Orientada a Objetos Aplicados

| Principio | Aplicación en el sistema |
|---|---|
| 🔹 Abstracción | Clases abstractas `EntidadBase` y `Servicio` |
| 🔹 Herencia | `Cliente`, `ReservaSala`, `AlquilerEquipo` y `AsesoriaEspecializada` heredan de clases base |
| 🔹 Polimorfismo | Cada servicio redefine `calcular_costo()` |
| 🔹 Encapsulación | Uso de atributos privados y validaciones mediante getters/setters |
| 🔹 Sobrescritura | Métodos redefinidos en clases derivadas |
| 🔹 Sobrecarga | Parámetros opcionales mediante `*args` y `**kwargs` |
| 🔹 Manejo de excepciones | Uso de `try/except/else/finally` y excepciones personalizadas |

---

# 🏗️ Arquitectura del Sistema

```text
EntidadBase (Clase Abstracta)
│
├── Cliente
│
└── Servicio (Clase Abstracta)
    │
    ├── ReservaSala
    ├── AlquilerEquipo
    └── AsesoriaEspecializada

Gestión:
│
├── Reserva
└── Gestor

Jerarquía de Excepciones:
│
Exception
└── SoftwareFJError
    ├── ErrorValidacion
    └── ErrorOperativo
```

---

# 📂 Estructura Modular del Proyecto

```text
sistema-gestion-softwarefj/
│
├── excepciones.py
├── logger.py
├── entidad_base.py
├── cliente.py
├── servicios.py
├── reserva.py
├── gestor.py
├── main.py
├── interfaz.py
│
├── logs/
│   └── sistema_fj.log
│
└── README.md
```

---

# ⚙️ Funcionalidades Principales

✅ Registro de clientes  
✅ Validación de datos personales  
✅ Gestión de múltiples servicios  
✅ Creación y cancelación de reservas  
✅ Cálculo dinámico de costos  
✅ Manejo robusto de errores  
✅ Registro automático de eventos y excepciones  
✅ Interfaz gráfica con Tkinter  
✅ Simulación de operaciones exitosas y fallidas

---

# 🛠️ Servicios Implementados

| Servicio | Descripción |
|---|---|
| 🏢 ReservaSala | Reserva de espacios y salas empresariales |
| 💻 AlquilerEquipo | Préstamo y alquiler de equipos tecnológicos |
| 🎓 AsesoriaEspecializada | Servicios profesionales personalizados |

---

# 🔄 Ciclo de Vida de una Reserva

```text
        PENDIENTE
        /       \
       /         \
CONFIRMADA     FALLIDA
      |
      |
 CANCELADA
```

---

# ⚠️ Manejo Avanzado de Excepciones

El sistema implementa:

- Excepciones personalizadas
- Validaciones estrictas
- Encadenamiento de excepciones
- Recuperación controlada de errores
- Continuidad operativa

## Tipos de errores controlados

- Datos inválidos
- Emails incorrectos
- Servicios inexistentes
- Parámetros faltantes
- Reservas inválidas
- Cálculos inconsistentes
- Operaciones no permitidas

---

# 📝 Sistema de Logs

Todas las operaciones y errores se registran automáticamente en:

```text
logs/sistema_fj.log
```

## Ejemplo real

```text
2026-05-10 10:15:01 | INFO  | Cliente añadido: Juan Perez
2026-05-10 10:15:02 | INFO  | Reserva confirmada correctamente
2026-05-10 10:15:03 | ERROR | Error procesando reserva: Datos incompletos
```

---

# 💻 Requisitos

```bash
Python 3.8 o superior
```

### Librerías utilizadas

- Tkinter
- Logging
- ABC (Abstract Base Classes)
- Enum
- Datetime

✅ No requiere instalación de paquetes externos

---

# ▶️ Ejecución del Proyecto

## 🔹 Ejecución en terminal

```bash
python main.py
```

El programa ejecuta múltiples operaciones automáticas incluyendo:

- Casos exitosos
- Errores controlados
- Validaciones
- Manejo de excepciones
- Registro de logs

---

## 🔹 Ejecución de la interfaz gráfica

```bash
python interfaz.py
```

La GUI permite:

- Registrar clientes
- Crear reservas
- Validar servicios
- Generar excepciones controladas
- Visualizar mensajes emergentes

---

# 📊 Datos de Prueba

## 👤 Clientes

| Documento | Nombre | Email | Resultado |
|---|---|---|---|
| 102030 | Juan Perez | juan@gmail.com | ✅ Correcto |
| 203040 | Ana | ana.com | ❌ Email inválido |
| 304050 | M | mario@mail.com | ❌ Nombre inválido |

---

## 🛠️ Servicios

| Servicio | Tipo | Tarifa Base |
|---|---|---|
| Sala VIP | ReservaSala | $80.000/hora |
| Laptop Dell | AlquilerEquipo | $45.000/día |
| Consultoría TI | AsesoriaEspecializada | $120.000/sesión |

---

# 🧪 Simulación de Operaciones

El sistema ejecuta más de 10 operaciones completas incluyendo:

- ✔️ Registros válidos
- ❌ Registros inválidos
- ✔️ Reservas exitosas
- ❌ Reservas fallidas
- ✔️ Cálculos correctos
- ❌ Excepciones controladas

Demostrando que la aplicación permanece estable incluso ante errores críticos.

---

# 📸 Vista del Proyecto

Puedes agregar capturas aquí:

```markdown
![Interfaz](imagenes/interfaz.png)
```

---

# 👨‍💻 Integrantes

| Nombre | Rol |
|---|---|
| Cesar Enciso | Desarrollo y documentación |
| Integrante 2 | Desarrollo |
| Integrante 3 | Desarrollo |
| Integrante 4 | Desarrollo |
| Integrante 5 | Desarrollo |

---

# 🎓 Información Académica

| Campo | Información |
|---|---|
| Universidad | Universidad Nacional Abierta y a Distancia — UNAD |
| Programa | Ingeniería de Sistemas |
| Curso | Programación Orientada a Objetos |
| Código | 213023 |
| Actividad | Fase 4 — Trabajo colaborativo |

---

# ⭐ Conclusión

Este proyecto demuestra la correcta aplicación de los principios fundamentales de la Programación Orientada a Objetos mediante el desarrollo de un sistema robusto, modular y extensible.

La solución integra arquitectura orientada a objetos, manejo avanzado de excepciones, validaciones estrictas y persistencia mediante archivos de logs, garantizando estabilidad y continuidad operativa aun cuando ocurren errores durante la ejecución.

---

<div align="center">

# ⭐ Software FJ ⭐

### Proyecto académico desarrollado con Python y Programación Orientada a Objetos

</div>
