## 🏨 Aplicación de Hotelería en Python

Aplicación de escritorio para la gestión de reservas, habitaciones y huéspedes en un hotel.

Tecnologías utilizadas:
- Python 3.10+
- Tkinter (interfaz gráfica)
- SQLite (base de datos local)

---

## 📚 Descripción
La aplicación permite al recepcionista:
- Registrar huéspedes.
- Registrar habitaciones.
- Crear, consultar y cerrar reservas.
- Registrar check-in y check-out.
- Ver disponibilidad por fecha.

---

## ⚖️ Roles en el Proyecto

### Uziel: Backend / Base de Datos
- Crear scripts de creación de tablas.
- Escribir funciones CRUD.
- Validaciones de negocio (fechas, estado de habitaciones).
- Archivos: `models/database.py`, `controllers/logic.py`

### Lucas: Interfaz Tkinter
- Crear formularios para todas las operaciones.
- Conectar GUI con backend.
- Validar campos en la interfaz.
- Archivos: `views/forms.py`, `views/main_window.py`, `main.py`

### Lautaro: Coordinación / Documentación
- Documentación en `README.md` y Word.
- Supervisión de merges, conflictos y estructura del repo.
- Archivos: `README.md`, `doc/`, estructura del proyecto.

---

## 📂 Estructura del Proyecto
hotel_app/
├── main.py                      ← inicia la app (Tkinter)
├── db/
│   └── hotel.db                 ← base de datos SQLite
├── models/
│   └── database.py              ← Python puro: conexión y consultas a SQLite
├── views/
│   ├── main_window.py           ← Tkinter: ventana principal y navegación
│   └── forms.py                 ← Tkinter: formularios (registro, reservas, etc.)
├── controllers/
│   └── logic.py                 ← Python puro: lógica de negocio
└── assets/
    └── icons/                   ← recursos visuales

---

## 🚀 Instalación Rápida
```bash
# Clonar el repositorio
git clone https://github.com/usuario/hotel_app.git
cd hotel_app

# Crear entorno virtual (opcional)
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la app
python main.py
```

---

## 📕 Historias de Usuario
- Registrar huésped
- Registrar habitaciones
- Crear una reserva
- Ver reservas activas
- Registrar check-in / check-out
- Consultar disponibilidad

(Ver archivo Word en /doc para más detalle)

---

## ✨ Mejoras Futuras
- Facturación con PDF.
- Reportes mensuales.
- Roles de usuario (admin, recepción).
- Backup en la nube.

---

## 📅 Estado del Proyecto
- MVP en desarrollo.
- División de tareas activa.

---

## ✉️ Equipo de Desarollo
Autores: Lucas Parejas, Uziel Gamarra, Lautaro Loyola 
>>>>>>> 62b266ca083516a452172ff66fa6f0274adac7b6
