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
