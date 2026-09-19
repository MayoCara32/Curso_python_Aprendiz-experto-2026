# Control de gastos personales en Python

Proyecto didáctico de un gestor de gastos personales creado durante un curso introductorio de Python. El programa evoluciona de un cálculo simple en consola a una aplicación que registra varios gastos, valida datos, guarda información en CSV y cuenta con pruebas automatizadas.

## Objetivos de aprendizaje

Este repositorio permite practicar:

- Variables, tipos de datos, conversiones y f-strings.
- Condicionales y funciones con parámetros y `return`.
- Listas, diccionarios, tuplas y ciclos.
- Validación de entradas y manejo de excepciones.
- Lectura y escritura de archivos CSV.
- Separación entre lógica del programa e interacción de consola.
- Pruebas automatizadas con `pytest`.

## Estructura esperada

```text
.
├── 01_saludo.py
├── 02_gasto_basico.py
├── 03_presupuesto.py
├── 04_funciones_gastos.py
├── control_gastos_dia1.py
├── 01_colecciones.py
├── 02_recorrer_gastos.py
├── 03_validar_monto.py
├── gastos.py
├── app_gastos.py
├── test_gastos.py
├── gastos.csv              # Se crea al guardar registros desde la aplicación
└── README.md
```

Los archivos con prefijos numéricos son ejercicios y demostraciones progresivas. La versión principal del proyecto del Día 2 está compuesta por `app_gastos.py`, `gastos.py` y `test_gastos.py`.

## Requisitos

- Python 3.
- `pytest` para ejecutar las pruebas automatizadas.

Comprueba la versión de Python:

```text
python --version
```

Instala `pytest`:

```text
python -m pip install -U pytest
```

## Ejecución

Para ejecutar la versión inicial del proyecto:

```text
python control_gastos_dia1.py
```

Para ejecutar el gestor de gastos con menú y archivo CSV:

```text
python app_gastos.py
```

La aplicación permite:

1. Registrar un gasto.
2. Consultar los gastos registrados.
3. Ver el total gastado y el dinero disponible.
4. Guardar los gastos en `gastos.csv` y salir.

## Pruebas

Ejecuta las pruebas desde la carpeta raíz del proyecto:

```text
python -m pytest -q
```

El archivo `test_gastos.py` comprueba cálculos, limpieza de categorías y validación de montos. Un resultado correcto debe indicar que todas las pruebas terminaron con `passed`.

## Ejemplo de uso

```text
=== Control de gastos personales: Día 2 ===
Presupuesto disponible: $500

1. Registrar gasto
2. Ver gastos
3. Ver resumen
4. Guardar y salir
Elige una opción: 1

Categoría del gasto: Transporte
Monto del gasto: $35.50

Gasto registrado correctamente.
```

## Archivo CSV

Al guardar, el programa genera un archivo `gastos.csv` con una estructura similar a esta:

```text
categoria,monto
Transporte,35.5
Alimentos,82.0
```

No se deben guardar en el repositorio datos personales, contraseñas, tokens ni claves API.

## Cómo contribuir al proyecto

1. Crea una rama para tu cambio.
2. Realiza cambios pequeños y comprensibles.
3. Ejecuta el programa y las pruebas antes de subir tus cambios.
4. Describe claramente el cambio en el mensaje del commit.

Ejemplos de mejoras posibles:

- Añadir fecha a cada gasto.
- Filtrar gastos por categoría.
- Mostrar el porcentaje del presupuesto utilizado.
- Permitir eliminar un gasto.
- Crear una interfaz web con Streamlit en una siguiente etapa.

## Contexto académico

Este proyecto está pensado como práctica de fundamentos de Python y preparación para continuar con cursos de programación de mayor profundidad. No sustituye cursos oficiales ni incluye soluciones de ejercicios oficiales de terceros.

```
