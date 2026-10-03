# Control de gastos personales

Aplicación educativa con Python y Streamlit para registrar gastos,
consultar el presupuesto y exportar registros en CSV.

## Instalación

Desde la carpeta del proyecto:

```text
python -m pip install -r requirements.txt
```

## Ejecución

```text
python -m streamlit run app.py
```

## Pruebas

```text
python -m pip install pytest
python -m pytest test_logica_web.py -q
```

## Funcionalidades

- Validación de categorías y montos.
- Registro de varios gastos durante la sesión.
- Total gastado y saldo disponible.
- Mensajes según el estado del presupuesto.
- Limpieza de registros.
- Descarga de gastos en CSV.

## Almacenamiento

Los gastos se mantienen durante la sesión de la aplicación.
Para conservarlos, descarga el archivo CSV antes de cerrar
o recargar la pestaña.

## Colaboración

1. Actualiza tu copia de main.
2. Crea una rama para una mejora concreta.
3. Realiza y prueba el cambio.
4. Publica la rama.
5. Abre un pull request hacia main.
6. Solicita una revisión y atiende los comentarios.

## Contexto académico

Este proyecto practica fundamentos de Python y trabajo colaborativo.
Sirve como preparación para continuar con CS50P; no sustituye
el curso oficial ni otorga su certificación.
