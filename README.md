# Actividad M7 L6 — CRUD con Django

Proyecto Django que implementa operaciones CRUD completas sobre un modelo `Libro`,
utilizando el ORM de Django, ModelForm, protección CSRF y herencia de templates.

---

## Requisitos

- Python 3.14+
- Django 5.x

---

## Pasos para ejecutar

```bash
# 1. Clonar el repositorio
git clone https://github.com/hanssoto-cyber/actividad_m7_l6.git
cd actividad_m7_l6

# 2. Crear y activar entorno virtual
python -m venv venv
source venv/Scripts/activate  # Git Bash
# o en PowerShell:
venv\Scripts\Activate.ps1

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Aplicar migraciones
python manage.py makemigrations
python manage.py migrate

# 5. Ejecutar servidor
python manage.py runserver
```

Abrir en el navegador: http://127.0.0.1:8000/libros/

---

## Rutas del proyecto

| Ruta | Descripción |
|------|-------------|
| `/libros/` | Listado de todos los libros |
| `/libros/crear/` | Formulario para crear un nuevo libro |
| `/libros/editar/<id>/` | Formulario para editar un libro existente |
| `/libros/eliminar/<id>/` | Confirmación para eliminar un libro |

---

## Estructura del proyecto
actividad_m7_l6/

├── config/

│   ├── settings.py

│   ├── urls.py

│   └── wsgi.py

├── libros/

│   ├── migrations/

│   ├── models.py

│   ├── forms.py

│   ├── views.py

│   └── urls.py

├── templates/

│   ├── base.html

│   ├── partials/

│   │   ├── navbar.html

│   │   └── footer.html

│   └── libros/

│       ├── listar_libros.html

│       ├── formulario_libro.html

│       └── confirmar_eliminacion.html

├── static/

│   └── css/

│       └── style.css

├── manage.py

└── requirements.txt

---

## ¿Cómo funciona el flujo completo de una operación CRUD?

El flujo sigue el patrón **MTV (Model - Template - View)** de Django:

1. **Create:** El usuario accede a `/libros/crear/`. La vista `crear` recibe un GET
   y renderiza el formulario vacío. Al enviar (POST), `LibroForm` valida los datos
   y si son correctos llama a `form.save()` que ejecuta un `INSERT` en la base de datos
   via el ORM. Luego redirige al listado.

2. **Read:** La vista `listar` ejecuta `Libro.objects.all()` que el ORM traduce a
   `SELECT * FROM libros_libro`. Los objetos se pasan al template y se renderizan
   con `{{ libro.titulo }}`, `{{ libro.autor }}`, etc.

3. **Update:** La vista `editar` recibe el `id` por URL, obtiene el objeto con
   `get_object_or_404(Libro, id=id)` y carga el formulario con `instance=libro`.
   Al hacer POST con cambios, el ORM ejecuta un `UPDATE` sobre el registro existente.

4. **Delete:** La vista `eliminar` muestra una pantalla de confirmación con los datos
   del libro. Solo al confirmar con POST se ejecuta `libro.delete()`, que el ORM
   traduce a `DELETE FROM libros_libro WHERE id=X`.

---

## ¿Qué aprendí sobre enrutamiento y parámetros dinámicos en URLs?

Django define rutas en `urls.py` usando `path()`. Los parámetros dinámicos se declaran
con la sintaxis `<tipo:nombre>`, por ejemplo `<int:id>`, lo que le indica a Django que
capture ese segmento de la URL como un entero y lo pase como argumento a la vista.

Ejemplo:
- URL: `/libros/editar/3/`
- Patrón: `path('editar/<int:id>/', views.editar, name='editar')`
- Django extrae `id=3` y llama a `views.editar(request, id=3)`

El uso de `namespace='libros'` en el `include()` del `urls.py` principal permite
referenciar las rutas con `{% url 'libros:editar' libro.id %}` en los templates,
evitando rutas hardcodeadas y facilitando el mantenimiento.