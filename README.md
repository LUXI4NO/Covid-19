# Análisis de Evolución de Casos de COVID-19 por Región y País
![image](https://github.com/LUXI4NO/Covid-19/assets/140111840/959b1207-5878-4fa0-9f6e-adffb08936a8)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://covidanalyst.streamlit.app/)

## Descripción

Este proyecto se centra en el análisis de datos relativos a casos y defunciones vinculados al COVID-19. Proporciona información visual a través de gráficos y datos estadísticos que detallan la situación en diferentes países y continentes, ilustrando la evolución de casos y fallecimientos a lo largo del tiempo.

## Tabla de Contenidos

- [Datos Utilizados](#datos-utilizados)
- [Funcionalidades](#funcionalidades)
- [Ejemplos de Gráficos Generados](#ejemplos-de-gráficos-generados)
- [Uso](#uso)
- [Estructura del Repositorio](#estructura-del-repositorio)
- [Dependencias](#dependencias)
- [Contribución](#contribución)
- [Autor](#autor)
- [Casos de Uso y Aplicaciones Futuras](#casos-de-uso-y-aplicaciones-futuras)
- [Enlaces](#enlaces)

### Datos Utilizados

Este análisis se basa en datos confiables, como los proporcionados por el Centro de Ciencia e Ingeniería de Sistemas (CSSE) de la Universidad Johns Hopkins y otras instituciones de salud reconocidas. Estos datos se actualizan periódicamente y se presentan en formatos accesibles, como CSV y JSON, para su disponibilidad y manejo.

## Funcionalidades

- **Filtrado de Datos:** Preparación y segmentación de datos sobre la pandemia por región y país.
- **Visualización Interactiva:** Utilización de gráficos interactivos a través de las librerías Streamlit y Altair para mostrar la evolución de casos confirmados y fallecimientos.
- **Comparación de Tendencias:** Análisis comparativo de la propagación del virus en distintas áreas del mundo, facilitando la comprensión de las variaciones y tendencias.

---

## Librerías Python Utilizadas
```python
import streamlit as st
import pandas as pd
import altair as alt
```

### Ejemplos de Gráficos Generados

Se incluyen ejemplos de gráficos generados por el análisis. Estos gráficos representan la evolución de casos confirmados y muertes en un formato interactivo, permitiendo explorar diferentes áreas y rangos de tiempo.
![image](https://github.com/LUXI4NO/Covid-19/assets/140111840/3722f26f-f642-47a5-9574-65b323f650c9)


## Uso

1. Clona el repositorio.
2. Asegúrate de tener los requisitos necesarios (listados en el archivo `requirements.txt`).
3. Ejecuta el código principal `main.py`.
4. Accede al servidor local para interactuar con los gráficos generados.

### Instrucciones más Detalladas de Uso

Para ejecutar el código, se recomienda crear un entorno virtual de Python y luego instalar las dependencias con:



## Estructura del Repositorio

- `main.py`: Archivo principal con el código para analizar y visualizar los datos.
- `data/`: Carpeta con los conjuntos de datos empleados en el análisis.
- `requirements.txt`: Listado de las dependencias necesarias para ejecutar el código.

## Dependencias

- Python 3.7 o superior
- Streamlit
- Altair
- Pandas

## Autor

Luciano Alvarez

## Casos de Uso y Aplicaciones Futuras

Este análisis puede ser útil para profesionales de la salud, investigadores y responsables de la toma de decisiones. También puede extenderse para incluir más datos demográficos, análisis predictivos y comparativos entre políticas de diferentes países para abordar la pandemia.

## Enlaces
- [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:alvarezlucianoezequiel@gmail.com)
- [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/luciano-alvarez-332843285/)
