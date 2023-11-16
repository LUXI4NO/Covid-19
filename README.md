# Análisis de Evolución de Casos de COVID-19 por Región y País
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://covidanalyst.streamlit.app/)
[![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

## Descripción

Este proyecto se centra en el análisis de datos relativos a casos y defunciones vinculados al COVID-19. Proporciona información visual a través de gráficos y datos estadísticos que detallan la situación en diferentes países y continentes, ilustrando la evolución de casos y fallecimientos a lo largo del tiempo.

## Tabla de Contenidos

- [Datos Utilizados](#datos-utilizados)
- [Funcionalidades](#funcionalidades)
- [Ejemplos de Gráficos Generados](#ejemplos-de-gráficos-generados)
- [Uso](#uso)
- [Estructura del Repositorio](#estructura-del-repositorio)
- [Dependencias](#dependencias)
- [Autor](#autor)
- [Casos de Uso y Aplicaciones Futuras](#casos-de-uso-y-aplicaciones-futuras)
- [Enlaces](#enlaces)

### Datos Utilizados

Este análisis se basa en datos confiables, como los proporcionados por el Centro de Ciencia e Ingeniería de Sistemas (CSSE) de la Universidad Johns Hopkins y otras instituciones de salud reconocidas. Estos datos se actualizan periódicamente y se presentan en formatos accesibles, como CSV y JSON, para su disponibilidad y manejo.

## Funcionalidades

- **Filtrado de Datos:** Preparación y segmentación de datos sobre la pandemia por región y país.
- **Visualización Interactiva:** Utilización de gráficos interactivos a través de las librerías Streamlit y Altair para mostrar la evolución de casos confirmados y fallecimientos.
- **Comparación de Tendencias:** Análisis comparativo de la propagación del virus en distintas áreas del mundo, facilitando la comprensión de las variaciones y tendencias.

### Ejemplos de Gráficos Generados

A continuación, te comparto ejemplos de gráficos generados mediante el análisis. Estos gráficos ilustran la evolución de casos confirmados y defunciones en un formato interactivo. Además, en el segundo gráfico, se proporciona una perspectiva de la evolución de casos por continentes.

![image](https://github.com/LUXI4NO/Covid-19/assets/140111840/937787d7-b441-4378-bc6c-f24064a94e54)

![image](https://github.com/LUXI4NO/Covid-19/assets/140111840/d508fdf6-8011-416a-a330-1ba4bf5ac2d5)


## Uso

1. Clona el repositorio.
2. Crea y activa un entorno virtual de Python usando el siguiente comando:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/Mac
    .\venv\Scripts\activate   # Para Windows
    ```

3. Instala las dependencias requeridas con:

    ```bash
    pip install -r requirements.txt
    ```

4. Ejecuta el código principal `main.py`.
5. Accede al servidor local para interactuar con los gráficos generados.

### Estructura del Repositorio

- `main.py`: Archivo principal con el código para analizar y visualizar los datos.
- `data/`: Carpeta con los conjuntos de datos empleados en el análisis.
- `requirements.txt`: Listado de las dependencias necesarias para ejecutar el código.

### Dependencias

- Python 3.7 o superior
- Streamlit
- Altair
- Pandas

## Autor

# Luciano Ezequiel Alvarez

### Casos de Uso y Aplicaciones Futuras

Este análisis puede ser útil para profesionales de la salud, investigadores y responsables de la toma de decisiones. También puede extenderse para incluir más datos demográficos, análisis predictivos y comparativos entre políticas de diferentes países para abordar la pandemia.

### Enlaces

- [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:alvarezlucianoezequiel@gmail.com)
- [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/luciano-alvarez-332843285/)
