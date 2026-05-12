#Mi primer repositorio
Nombre : Alex

# 🚀 ParkGrid
## Gestión inteligente de parqueaderos

Sistema web para la gestión de múltiples parqueaderos en tiempo real, permitiendo visualizar espacios disponibles, registrar vehículos y automatizar el proceso de cobro.

---

## 📌 Descripción
ParkGrid es una plataforma que optimiza la administración de parqueaderos mediante una interfaz visual intuitiva. Permite a los usuarios encontrar espacios disponibles fácilmente y a los administradores tener control total del sistema.

---

## 🎯 Objetivo
Desarrollar un sistema web interactivo que permita gestionar múltiples parqueaderos en tiempo real, optimizando el control de espacios, el registro de vehículos y el cálculo automático del servicio.

---

## 👥 Equipo
- Alex Molina  
- Sebas Restrepo
- Juan Tirado

---

## ⚙️ Tecnologías

- **Frontend:** HTML, CSS, JavaScript, Bootstrap  
- **Backend:** Node.js  
- **Base de datos:** MySQL  

---

## 🧩 Funcionalidades

- Visualización de espacios disponibles en tiempo real  
- Registro de entrada y salida de vehículos  
- Cálculo automático del tiempo y costo  
- Sistema de pagos (efectivo y digital)  
- Gestión de múltiples parqueaderos  
- Historial de movimientos  
- Sistema de reseñas y calificaciones  

---

## 👤 Roles del Sistema

- **Administrador:** Control total del sistema, reportes y gestión global  
- **Dueño del parqueadero:** Control de su parqueadero, ingresos y espacios  
- **Usuario/Cliente:** Búsqueda de espacios, uso del servicio y pagos  

---

## 🔄 Flujo del Sistema

Inicio → Buscar parqueadero → Ver espacios disponibles → Registrar vehículo → Salida → Pago  

---

## 💳 Pasarela de Pagos

- Métodos: efectivo, tarjeta y pagos digitales  
- Cálculo automático del costo según tiempo de uso  
- Liberación automática del espacio tras el pago  

---

## 🗄️ Base de Datos

Tablas principales:
- espacios  
- vehiculos  
- historial  
- pagos  
- reseñas  
- usuarios  

---

## 💰 Presupuesto

- **Desarrollo:** $10.650.000 – $20.380.000 COP  
- **Mantenimiento anual:** $1.850.000 – $4.900.000 COP  

---

## 🌐 Estado actual

🚧 En desarrollo (proyecto académico con enfoque real)  

---

## 📍 Futuro del proyecto

- Implementación en parqueaderos reales  
- Integración completa con pasarelas de pago  
- Aplicación móvil  
- Sistema de reservas anticipadas  

---
## Uso de ramas en GitHub

Las ramas (branches) en GitHub permiten trabajar en nuevas funciones, mejoras o correcciones sin afectar el código principal del proyecto.

### ¿Para qué sirven?

- Facilitan el trabajo en equipo.
- Evitan errores en la versión principal del sistema.
- Permiten desarrollar funciones por separado.
- Ayudan a organizar el trabajo del proyecto.

### ¿Cómo las utilizaremos en ParkGrid?

En el proyecto ParkGrid se utilizará una rama principal llamada:

- `main` → Contendrá la versión estable y final del proyecto.

Cada integrante del equipo trabajará en ramas diferentes según la tarea asignada. Ejemplos:

- `login`
- `interfaz`
- `base-datos`
- `reportes`

Cuando una funcionalidad esté terminada y probada, se realizará un **merge** hacia la rama `main`.

### Flujo de trabajo

1. Crear una nueva rama.
2. Realizar cambios y guardar avances.
3. Subir cambios a GitHub.
4. Revisar el funcionamiento.
5. Unir los cambios a `main`.

### Ejemplo de comandos

```bash
git checkout -b login
git add .
git commit -m "Se agregó módulo de inicio de sesión"
git push origin login