import streamlit as st
import pandas as pd
import altair as alt

# Configuración de la página de la aplicación
st.set_page_config(page_title="Analisis covid 19", page_icon="🔎", layout="wide")

# Cargar datos desde el archivo CSV
df = pd.read_csv('Casos.CSV', encoding='utf-8')
df1 = pd.read_csv('Muertes.CSV', encoding='utf-8')

# Título y autor
st.title("Análisis de Casos y Mortalidad por COVID-19 📊")
st.caption("Autor: Luciano Alvarez")

#metodologia
st.subheader("Metodología:")
st.write("En este proyecto, se siguieron los siguientes pasos para obtener, limpiar y analizar los datos:")

st.markdown("1. **Obtención de Datos:** Los datos relacionados con el COVID-19 se obtuvieron de fuentes confiables, como el Centro de Ciencia e Ingeniería de Sistemas (CSSE) de la Universidad Johns Hopkins. Sin embargo, debido a la naturaleza cambiante de la información, es importante señalar que se podrían haber encontrado datos faltantes o inexactitudes debido a la constante actualización y variabilidad de la información en tiempo real.")
st.markdown("2. **Limpieza de Datos:** Una fase crucial del análisis de datos. Durante esta etapa, se eliminaron duplicados, valores nulos y se estandarizaron formatos para garantizar la calidad de los datos. Se aplicaron técnicas de manejo de datos faltantes, como la imputación de valores o el análisis cuidadoso de la omisión de los mismos.")
st.markdown("3. **Análisis de Datos:** Se utilizaron herramientas y software de análisis de datos como Python con bibliotecas como Pandas y Altair para explorar y visualizar los datos. Se consideró un análisis para manejar y presentar los datos de forma coherente, a pesar de los posibles datos faltantes.")

# Objetivos del Análisis
st.subheader("Objetivos del Análisis:")
st.write("El propósito principal es desarrollar habilidades analíticas y de interpretación de datos a través de un estudio profundo y la mejora de las técnicas de manipulación, análisis y visualización de información.")

# Lista de habilidades
st.write("""
1. Recopilar y limpiar datos de fuentes confiables, considerando la posibilidad de datos faltantes o inexactitudes.
2. Realizar análisis exploratorio de datos (EDA) utilizando Python y bibliotecas como Pandas y Altair, adaptando el análisis para afrontar datos faltantes.
3. Identificar tendencias, patrones y relaciones en los datos, incluso cuando la información no está completa.
4. Visualizar los resultados de manera efectiva, comunicando los datos de forma clara y considerando las posibles áreas de incertidumbre debido a datos faltantes.
""")

st.write("---")
st.title("Estado de Casos Actuales 🔎")
st.write("A continuación, se presenta el resumen de los casos que estamos investigando en este Proyecto.")
# CASOS
fechas = df.columns[4:]
suma_total = df[fechas].sum().sum()

# MUERTES
fechas1 = df1.columns[4:]
suma_total1 = df1[fechas1].sum().sum()

total1, total2 = st.columns(2, gap='large')

with total1:
    st.success('Casos Investigados', icon="🦠")
    st.metric(label="Infectados", value=f"{suma_total:,.0f}")

with total2:
    st.error('Muertes Investigadas', icon="💀")
    st.metric(label="Muertos", value=f"{suma_total1:,.0f}")

# Separador
st.write("---")

# Encabezado principal
st.title("COVID-19: Casos y Mortalidad 🌐")
st.write("Este análisis evalúa la densidad de casos confirmados y defunciones por millón de habitantes en varias naciones, ofreciendo una perspectiva comparativa del impacto del COVID-19. Examina la relación entre la incidencia de casos y la mortalidad, considerando la densidad poblacional para comprender el impacto en diferentes contextos geográficos. Basado en datos actualizados, destaca diferencias regionales y factores que influyen en la propagación y gravedad de la pandemia a escala global.")
st.caption("Última actualización de datos: 3 de septiembre de 2023.")

# División en columnas
columna_1, columna_2 = st.columns(2, gap='large')

# Columna 1: Naciones con el Mayor Número de Casos de COVID-19
with columna_1:
    st.markdown("<h4 style='text-align: center;'>Naciones con el Mayor Número de Casos de COVID-19</h4>", unsafe_allow_html=True)
    casos_filtrados = df[df['3/9/23'] > 6500000]

    casos_chart = alt.Chart(casos_filtrados).mark_bar().encode(
        y=alt.Y('Country/Region:N', sort='-x', title='Países'),
        x=alt.X('3/9/23:Q', title='Casos Confirmados', axis=alt.Axis(format='~s')),
        color=alt.Color('3/9/23:Q', scale=alt.Scale(scheme='greens'), title='Casos Confirmados'),
        tooltip=['Country/Region:N', alt.Tooltip('3/9/23:Q', title='Casos Confirmados', format=',')]
    )

    st.altair_chart(casos_chart, use_container_width=True)
    st.success("Principales países con casos confirmados de COVID-19, clasificados de forma descendente. Estados Unidos lidera con un porcentaje significativo, mientras que otros países presentan una distribución más equilibrada en el gráfico de los 20 con mayor incidencia.")

# Columna 2: Naciones con el Mayor Número de Muertes de COVID-19
with columna_2:
    st.markdown("<h4 style='text-align: center;'>Naciones con el Mayor Número de Muertes de COVID-19</h4>", unsafe_allow_html=True)
    muertes_filtradas = df1[df1['3/9/23'] > 100000]

    muertes_chart = alt.Chart(muertes_filtradas).mark_bar().encode(
        y=alt.Y('Country/Region:N', sort='-x', title='Países'),
        x=alt.X('3/9/23:Q', title='Muertes Confirmadas', axis=alt.Axis(format='~s')),
        color=alt.Color('3/9/23:Q', scale=alt.Scale(scheme='reds'), title='Muertes Confirmadas'),
        tooltip=['Country/Region:N', alt.Tooltip('3/9/23:Q', title='Muertes Confirmadas', format=',')]
    )

    st.altair_chart(muertes_chart, use_container_width=True)
    st.error("Principales países con tasas de mortalidad por COVID-19, ordenados de forma descendente. Estados Unidos encabeza la lista con un porcentaje notable, mientras que otros países exhiben una distribución más equilibrada entre los 20 con mayores tasas de fallecimientos.")

# Separador
st.write("---")

# Encabezado principal
st.title("Tasa de Mortalidad e Incidencia del COVID-19 📊")
st.write("Este análisis se enfoca en dos aspectos claves de la pandemia de COVID-19: la tasa de mortalidad y la incidencia. Los gráficos proporcionan una visión comparativa que permite comprender la gravedad de la enfermedad en distintas regiones. Estos indicadores son fundamentales para evaluar el impacto en la población y guiar decisiones estratégicas en la lucha contra la pandemia.")
st.caption("Datos actualizados hasta el 3 de septiembre de 2023.")

# Columnas para colocar gráficos
graf3, graf4 = st.columns(2, gap='large')

# Gráfico de Tasa de Incidencia
with graf3:
    st.subheader("Tasa de Incidencia del COVID-19 por País")

    # Calcular la tasa de incidencia y agregarla como una nueva columna
    df['Tasa de Incidencia'] = (df['3/9/23'] / 1_000_000) * 100_000

    # Filtrar los países/regiones con tasas de incidencia más altas
    tasas_altas = df[df['Tasa de Incidencia'] > 640_000]

    # Crear el gráfico de barras para la tasa de incidencia
    tasa_chart = (
        alt.Chart(tasas_altas)
        .mark_bar()
        .encode(
            y=alt.Y('Tasa de Incidencia:Q', title="Tasa de Incidencia"),
            x=alt.X('Country/Region:N', title="País/Región", sort='-y'),  
            color=alt.Color('Tasa de Incidencia:Q', scale=alt.Scale(scheme='greens'), title='Tasa de Incidencia'),
            tooltip=['Country/Region:N', alt.Tooltip('Tasa de Incidencia:Q', title='Tasa de Incidencia', format=',')]
        )

    )

    # Mostrar el gráfico de tasa de incidencia
    st.altair_chart(tasa_chart, use_container_width=True)
    st.success("Gráfico de barras: Tasa de incidencia del COVID-19 por país/región, ordenado de forma descendente por casos confirmados por millón de habitantes. Proporciona una evaluación de la gravedad de la propagación del virus en diversas regiones.")

# Gráfico de Tasa de Letalidad
with graf4:
    st.subheader("Tasa de Letalidad del COVID-19 por País")

    # Calcular el promedio de letalidad y agregarlo como una nueva columna
    columns_to_average = df1.columns[4:]
    df1['Average_Lethality'] = df1[columns_to_average].mean(axis=1)
    
    # Filtrar los países/regiones con tasas de letalidad promedio más altas
    tasas_letalidad_altas = df1[df1['Average_Lethality'] > 40_000]

    # Crear el gráfico de barras para la tasa de letalidad promedio
    promedio_chart = (
        alt.Chart(tasas_letalidad_altas)
        .mark_bar()
        .encode(
            y=alt.Y('Average_Lethality:Q', title='Promedio de Muertes'),  
            x=alt.X('Country/Region:N', title='País/Región', sort='-y'),  
            color=alt.Color('Average_Lethality:Q', scale=alt.Scale(scheme='reds'), title='Promedio de Muertes'),
            tooltip=['Country/Region:N', alt.Tooltip('Average_Lethality:Q', title='Tasa de Letalidad', format=',')]
        )
    )

    # Mostrar el gráfico de tasa de letalidad promedio
    st.altair_chart(promedio_chart, use_container_width=True)
    st.error("Gráfico de barras: Promedio de muertes por COVID-19 por país/región, ordenado de forma descendente por tasa de letalidad promedio. Se excluyen áreas con menos de 40,000 muertes para destacar las más afectadas. Ofrece datos sobre la enfermedad en diversas regiones.")

# Encabezado y descripción general
st.markdown("---")
st.title("Evolución de Casos Confirmados de COVID-19 Global 🌎")
st.write("El gráfico lineal que se presenta a continuación muestra la evolución de los casos confirmados de COVID-19 desde el 22 de enero de 2020 hasta el 9 de marzo de 2023. Esta representación gráfica se destaca como una herramienta fundamental para analizar la variación en el número de casos a lo largo de este extenso período temporal. Su utilidad radica en la identificación de patrones, momentos críticos y posibles cambios significativos en la propagación de la enfermedad a escala global.")
st.caption("Datos actualizados hasta el 3 de septiembre de 2023.")

# División en dos columnas para casos y muertes
casos, muertes = st.columns(2, gap='large')

# Gráfico de Evolución de Casos Confirmados de COVID-19
with casos:
    st.subheader("Evolución de Casos Confirmados de COVID-19")
    
    # Procesamiento de datos para el gráfico de casos confirmados
    fechas = df.columns[4:]
    global_chart = (
        alt.Chart(df.melt(id_vars=['Country/Region'], value_vars=fechas, var_name='Fecha', value_name='Casos Confirmados'))
        .mark_line(point=True, color='blue', size=2)
        .encode(
            y=alt.Y('sum(Casos Confirmados):Q', title='Casos Confirmados a Nivel Mundial'),
            x=alt.X('Fecha:T', title='Fecha', axis=alt.Axis(format='%b %Y')),
            color=alt.Color('sum(Casos Confirmados):Q', scale=alt.Scale(scheme='greens'), title='Casos Confirmados a Nivel Mundial'),
            tooltip=[
                alt.Tooltip('Fecha:T', title='Fecha'),
                alt.Tooltip('sum(Casos Confirmados):Q', title='Casos Confirmados', format=',')
            ]
        ).configure_legend(orient='top')
    )

    st.altair_chart(global_chart, use_container_width=True)
    
    # Información adicional sobre los casos confirmados
    st.success(
        "Se observa un aumento constante en los casos confirmados de COVID-19 en los primeros meses. A partir de enero de 2022 hasta abril, hay un incremento significativo que se mantiene constante. "
        "Aunque la tasa de crecimiento se estabiliza, los casos confirmados continúan aumentando. "
        "El gráfico representa los casos desde el 22 de enero de 2020 hasta el 9 de marzo de 2023."
    )

# Gráfico de Evolución de Muertes Confirmadas de COVID-19
with muertes:
    st.subheader("Evolución de Muertes Confirmadas de COVID-19")
    
    # Procesamiento de datos para el gráfico de muertes confirmadas
    fechas = df1.columns[4:]
    muertes_chart = (
        alt.Chart(df1.melt(id_vars=['Country/Region'], value_vars=fechas, var_name='Fecha', value_name='Muertes'))
        .mark_line(point=True, color='red', size=2)
        .encode(
            x=alt.X('Fecha:T', title='Fecha', axis=alt.Axis(format='%b %Y')),
            y=alt.Y('sum(Muertes):Q', title='Muertes a Nivel Mundial'),
            color=alt.Color('sum(Muertes):Q', scale=alt.Scale(scheme='reds'), title='Muertes a Nivel Mundial'),
            tooltip=[
                alt.Tooltip('Fecha:T', title='Fecha'),
                alt.Tooltip('sum(Muertes):Q', title='Muertes', format=',')
            ]
        ).configure_legend(orient='top')
    )

    st.altair_chart(muertes_chart, use_container_width=True)
    
    # Información adicional sobre las muertes confirmadas
    st.error(
        "Se evidencia un aumento inicial significativo en las muertes durante los primeros meses del brote de COVID-19. "
        "En abril de 2020, se registraron alrededor de 53,000 muertes, alcanzando los 6 millones para marzo de 2022. "
        "Desde entonces, la tasa de crecimiento disminuyó y, al 9 de marzo de 2023, se mantuvieron por debajo de los 6 millones. "
    )

# Sección de encabezado
st.write("---")
st.title("Evolución de Casos Confirmados de COVID-19 en Distintos Continentes 🌍")
st.write("El gráfico exhibe la evolución de los casos confirmados de COVID-19 en varias regiones del mundo, abarcando Sudamérica, Centroamérica, África, Europa, Asia y Oceanía. Esta visualización posibilita la comparación de la propagación de la enfermedad a lo largo del tiempo en estas áreas geográficas, ofreciendo una perspectiva detallada de la incidencia de la enfermedad en distintas partes del mundo.")

fechas = df.columns[4:]

# Definir listas de países por región
sudamerica_countries = ['Guyana', 'Trinidad and Tobago', 'Suriname', 'Argentina', 'Brazil', 'Bolivia', 'Chile', 'Colombia', 'Ecuador', 'Perú', 'Paraguay', 'Uruguay', 'Venezuela']
centroamerica_paises = ['Jamaica', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Haiti', 'Grenada', 'Dominica', 'Dominican Republic', 'Barbados', 'Bahamas', 'Mexico', 'US', 'Canada', 'Belize', 'Costa Rica', 'El Salvador', 'Guatemala', 'Honduras', 'Nicaragua', 'Panama', 'Antigua and Barbuda', 'Cuba']
africa_paises = ['Mauritania', 'Zambia', 'Zimbabwe', 'Uganda', 'Tunisia', 'Togo', 'Tanzania', 'Sudan', 'Somalia', 'Seychelles', 'Sierra Leone', 'Sao Tome and Principe', 'Rwanda', 'Niger', 'Nigeria', 'Namibia', 'Mozambique', 'Morocco', 'Mauritius', 'Mali', 'Madagascar', 'Malawi', 'Liberia', 'Libya', 'Lesotho', 'Guinea', 'Kenya', 'Guinea-Bissau', 'Ghana', 'Gabon', 'Gambia', 'Ethiopia', 'Eswatini', 'Eritrea', 'Djibouti', 'South Africa', 'South Sudan', 'Algeria', 'Cameroon', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Central African Republic', 'Chad', 'Comoros', 'Congo (Brazzaville)', 'Congo (Kinshasa)', "Cote d'Ivoire", 'egypt', 'Senegal', 'Equatorial Guinea']
europa_paises = ['Malta', 'Turkey', 'Ukraine', 'Switzerland', 'Sweden', 'Slovenia', 'Slovakia', 'Serbia', 'San Marino', 'Norway', 'North Macedonia', 'Montenegro', 'Kosovo', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Moldova', 'Monaco', 'Italy', 'Ireland', 'Iceland', 'Hungary', 'Holy See', 'Estonia', 'Georgia', 'Finland', 'Bulgaria', 'Cyprus', 'Czechia', 'Bosnia and Herzegovina', 'Belarus', 'Belgium', 'Austria', 'Denmark', 'Albania', 'France', 'Germany', 'Greece', 'Hungary', 'Netherlands', 'United Kingdom', 'Spain', 'Andorra', 'Croatia']
asia_paises = ['Mongolia', 'Yemen', 'West Bank and Gaza', 'Vietnam', 'United Arab Emirates', 'Timor-Leste', 'Thailand', 'Taiwan*', 'Uzbekistan', 'Tajikistan', 'Syria', 'Sri Lanka', 'Singapore', 'Saudi Arabia', 'Russia', 'Oman', 'Nepal', 'Maldives', 'Laos', 'Malaysia', 'Lebanon', 'Jordan', 'Kyrgyzstan', 'Kuwait', 'Korea, North', 'Korea, South', 'Japan', 'Israel', 'Afghanistan', 'Azerbaijan', 'Kazakhstan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei', 'Burma', 'Cambodia', 'China', 'India', 'Indonesia', 'Iran', 'Iraq']
oceania_paises = ['Australia', 'Fiji', 'Kiribati', 'Marshall Islands', 'Micronesia', 'Nauru', 'New Zealand', 'Samoa', 'Solomon Islands', 'Tonga', 'Tuvalu', 'Vanuatu']

# Filtrar datos por regiones
sudamerica_data = df[df['Country/Region'].isin(sudamerica_countries)]
centroamerica_data = df[df['Country/Region'].isin(centroamerica_paises)]
africa_data = df[df['Country/Region'].isin(africa_paises)]
europa_data = df[df['Country/Region'].isin(europa_paises)]
asia_data = df[df['Country/Region'].isin(asia_paises)]
oceania_data = df[df['Country/Region'].isin(oceania_paises)]

# Calcular la suma total de casos por región
suma_total_sudamerica = sudamerica_data[fechas].sum().sum()
suma_total_centroamerica = centroamerica_data[fechas].sum().sum()
suma_total_africa = africa_data[fechas].sum().sum()
suma_total_europa = europa_data[fechas].sum().sum()
suma_total_asia = asia_data[fechas].sum().sum()
suma_total_oceania = oceania_data[fechas].sum().sum()

# Convertir los datos en formato 'melted' para su visualización
melted_sudamerica_df = pd.melt(sudamerica_data, id_vars=['Province/State'], value_vars=fechas, var_name='Fecha', value_name='Casos')
melted_centroamerica_df = pd.melt(centroamerica_data, id_vars=['Province/State'], value_vars=fechas, var_name='Fecha', value_name='Casos')
melted_africa_df = pd.melt(africa_data, id_vars=['Province/State'], value_vars=fechas, var_name='Fecha', value_name='Casos')
melted_europa_df = pd.melt(europa_data, id_vars=['Province/State'], value_vars=fechas, var_name='Fecha', value_name='Casos')
melted_asia_df = pd.melt(asia_data, id_vars=['Province/State'], value_vars=fechas, var_name='Fecha', value_name='Casos')
melted_oceania_df = pd.melt(oceania_data, id_vars=['Province/State'], value_vars=fechas, var_name='Fecha', value_name='Casos')

# Creación de un gráfico combinado para múltiples regiones
combined_chart = (
    alt.layer(
        # Gráfico de evolución de casos para Sudamérica
        alt.Chart(melted_sudamerica_df).mark_line(point=True, color='Green', size=1).encode(
            y=alt.Y('sum(Casos):Q'),
            x=alt.X('Fecha:T', title='Fecha', axis=alt.Axis(format='%b %Y')),
            color=alt.ColorValue('Green'),  
            tooltip=[
                alt.Tooltip('Fecha:T', title='Fecha'),
                alt.Tooltip('sum(Casos):Q', title='Casos en Sudamérica', format=','),
            ]
        ),
        # Gráfico de evolución de casos para Centroamérica
        alt.Chart(melted_centroamerica_df).mark_line(point=True, color='#627229').encode(
            y=alt.Y('sum(Casos):Q'),
            x=alt.X('Fecha:T'),
            color=alt.ColorValue('#627229'), 
            tooltip=[
                alt.Tooltip('Fecha:T', title='Fecha'),
                alt.Tooltip('sum(Casos):Q', title='Casos en Norteamérica', format=',')
            ]
        ),
        # Gráfico de evolución de casos para África
        alt.Chart(melted_africa_df).mark_line(point=True, color='#5ABD61').encode(
            y=alt.Y('sum(Casos):Q'),
            x=alt.X('Fecha:T', title='Fecha'),
            color=alt.value('#5ABD61'), 
            tooltip=[
                alt.Tooltip('Fecha:T', title='Fecha'),
                alt.Tooltip('sum(Casos):Q', title='Casos en África', format=',')
            ]
        ),
        # Gráfico de evolución de casos para Europa
        alt.Chart(melted_europa_df).mark_line(point=True, color='#054135').encode(
            y=alt.Y('sum(Casos):Q'),
            x=alt.X('Fecha:T'),
            color=alt.value('#054135'), 
            tooltip=[
                alt.Tooltip('Fecha:T', title='Fecha'),
                alt.Tooltip('sum(Casos):Q', title='Casos en Europa', format=',')
            ]
        ),
        # Gráfico de evolución de casos para Asia
        alt.Chart(melted_asia_df).mark_line(point=True, color='#00D589').encode(
            y=alt.Y('sum(Casos):Q'),
            x=alt.X('Fecha:T'),
            color=alt.value('#00D589'), 
            tooltip=[
                alt.Tooltip('Fecha:T', title='Fecha'),
                alt.Tooltip('sum(Casos):Q', title='Casos en Asia', format=',')
            ]
        ),
        # Gráfico de evolución de casos para Oceanía
        alt.Chart(melted_oceania_df).mark_line(point=True, color='#72FF07').encode(
            y=alt.Y('sum(Casos):Q'),
            x=alt.X('Fecha:T'),
            color=alt.value('#72FF07'), 
            tooltip=[
                alt.Tooltip('Fecha:T', title='Fecha'),
                alt.Tooltip('sum(Casos):Q', title='Casos en Oceanía', format=',')
            ]
        ).interactive()  # Hacer el gráfico interactivo
    )
)

# Mostrar el gráfico combinado de evolución de casos confirmados para varias regiones
st.altair_chart(combined_chart, use_container_width=True)

# Mostrar una decripcion de que se trata el grafico
st.success("El gráfico lineal ilustra la evolución de casos de COVID-19 en distintos continentes. Europa se destaca por su alto número de casos, seguida por Asia y Centroamérica. En contraste, Sudamérica, África y Oceanía muestran una incidencia considerablemente menor de la enfermedad. Esta visualización ofrece una panorámica global de la distribución del virus, lo que resulta fundamental para comprender su propagación a nivel mundial. Presenta una suma total de casos para cada región, permitiendo una comparativa clara entre continentes y su evolución a lo largo del tiempo")

# Sección de encabezado
st.write("##")  # Línea divisoria
st.title("Evolución de Casos por País en Múltiples Continentes 🗺️")
st.write("Este segmento se enfoca en un análisis detallado de la variación de las cifras de muertes por país en diferentes continentes. Su propósito es ampliar la perspectiva brindada en gráficos previos al detallar la incidencia del virus en los diez países más significativos de cada continente. Ofrece una selección representativa de naciones relevantes por región, brindando una visión clara y concisa del impacto de la pandemia en diversas áreas del mundo.")
st.caption("Se muestran los 10 países más relevantes por continente.")

# Columnas para Europa y Asia
columna_Asia, columna_Europa = st.columns(2, gap='large')

# Gráfico de Europa
with columna_Europa:
    st.subheader("Evolución de Casos de COVID-19 en Países Europeos")
    europa_data = df[df['Country/Region'].isin(europa_paises)]
    fecha_columnas = df.columns[4:].tolist()

    # Procesamiento de datos para el gráfico de Europa
    europa_df = pd.melt(europa_data, id_vars=['Country/Region'], value_vars=fecha_columnas, var_name='Fecha', value_name='Casos')

    # Filtrar los 10 países con más casos
    top_10_europa = europa_df.groupby('Country/Region')['Casos'].max().nlargest(10).index
    europa_df_top_10 = europa_df[europa_df['Country/Region'].isin(top_10_europa)]

    # Creación del gráfico de barras para Europa
    chart_europa = (
        alt.Chart(europa_df_top_10).mark_bar().encode(
            x=alt.X('Casos:Q'),
            y=alt.Y('Country/Region:N', sort='-x'),
            color=alt.Color('Country/Region:N', scale=alt.Scale(scheme='greens')),
            tooltip=[
                alt.Tooltip('Country/Region:N', title='Pais'),
                alt.Tooltip('Casos:Q', title='Casos en Europa', format=',')
            ]
        ).properties(
            width=800,
            height=400
        )
    )

    st.altair_chart(chart_europa, use_container_width=True)

# Gráfico de Asia
with columna_Asia:
    st.subheader("Evolución de Casos de COVID-19 en Países Asiáticos")
    asia_data = df[df['Country/Region'].isin(asia_paises)]
    fecha_columnas = df.columns[4:].tolist()

    # Procesamiento de datos para el gráfico de Asia
    asia_df = pd.melt(asia_data, id_vars=['Country/Region'], value_vars=fecha_columnas, var_name='Fecha', value_name='Casos')

    # Filtrar los 10 países con más casos
    top_10_asia = asia_df.groupby('Country/Region')['Casos'].max().nlargest(10).index
    asia_df_top_10 = asia_df[asia_df['Country/Region'].isin(top_10_asia)]

    # Creación del gráfico de barras para Asia
    chart_asia = (alt.Chart(asia_df_top_10).mark_bar().encode(
            x=alt.X('Casos:Q'),
            y=alt.Y('Country/Region:N', sort='-x'),
            color=alt.Color('Country/Region:N', scale=alt.Scale(scheme='greens')),
            tooltip=[
                alt.Tooltip('Country/Region:N', title='Pais'),
                alt.Tooltip('Casos:Q', title='Casos en Asia', format=',')
            ]
        ).properties(
            width=800,
            height=400
        )
    )

    st.altair_chart(chart_asia, use_container_width=True)

# Columnas para Sudamérica y Centroamérica
columna_sur, columna_centro = st.columns(2, gap='large')

# Gráfico de Sudamérica
with columna_sur:
    st.subheader("Evolución de Casos de COVID-19 en Sudamerica")
    sudamerica_data = df[df['Country/Region'].isin(sudamerica_countries)]
    fecha_columnas = df.columns[4:].tolist()

    sur_df = pd.melt(sudamerica_data, id_vars=['Country/Region'], value_vars=fecha_columnas, var_name='Fecha', value_name='Casos')

    # Filtrar los 10 países con más casos
    top_10_sur = sur_df.groupby('Country/Region')['Casos'].max().nlargest(10).index
    sur_df_top_10 = sur_df[sur_df['Country/Region'].isin(top_10_sur)]

    # Crear el gráfico de barras con los 10 países
    chart_sur = (alt.Chart(sur_df_top_10).mark_bar().encode(
            x=alt.X('Casos:Q'),
            y=alt.Y('Country/Region:N', sort='-x'),
            color=alt.Color('Country/Region:N', scale=alt.Scale(scheme='greens')),
            tooltip=[
                alt.Tooltip('Country/Region:N', title='Pais'),
                alt.Tooltip('Casos:Q', title='Casos en Sudamerica', format=',')
            ]
        ).properties(
            width=800,
            height=400
        )
    )

    st.altair_chart(chart_sur, use_container_width=True)

# Gráfico de Centroamérica
with columna_centro:
    st.subheader("Evolución de Casos de COVID-19 en Norteamerica")
    
    # Filtrar los datos para países de Centroamérica
    centroamerica_data = df[df['Country/Region'].isin(centroamerica_paises)]
    fecha_columnas = df.columns[4:].tolist()

    # Procesamiento de datos para el gráfico de Centroamérica
    centro_df = pd.melt(centroamerica_data, id_vars=['Country/Region'], value_vars=fecha_columnas, var_name='Fecha', value_name='Casos')

    # Filtrar los 10 países con más casos de Centroamérica
    top_10_centro = centro_df.groupby('Country/Region')['Casos'].max().nlargest(10).index
    centro_df_top_10 = centro_df[centro_df['Country/Region'].isin(top_10_centro)]

    # Creación del gráfico de barras para Centroamérica
    chart_centro = (alt.Chart(centro_df_top_10).mark_bar().encode(
            x=alt.X('Casos:Q'),
            y=alt.Y('Country/Region:N', sort='-x'),
            color=alt.Color('Country/Region:N', scale=alt.Scale(scheme='greens')),
            tooltip=[
                alt.Tooltip('Country/Region:N', title='Pais'),
                alt.Tooltip('Casos:Q', title='Casos en Norteamerica', format=',')
            ]
        ).properties(
            width=800,
            height=400
        )
    )

    st.altair_chart(chart_centro, use_container_width=True)

# Sección de éxito con información adicional
st.success("Se destacan los casos prominentes de Brasil y Estados Unidos en sus respectivas regiones, mientras que Europa presenta una distribución más equitativa de casos entre sus países. Además, India sobresale como líder en incidencia en Asia. Estos gráficos ofrecen una visión general y comparativa de la pandemia en diferentes continentes, destacando las diferencias significativas en la propagación del virus en cada región.")


# Sección de encabezado
st.write("---")
st.title("Evolución de Muertes Confirmadas de COVID-19 Global 🌎")
st.write("El gráfico muestra la evolución de muertes confirmadas por COVID-19 en distintas regiones del mundo. Permite comparar la progresión de la enfermedad a lo largo del tiempo y ofrece una visión detallada de su incidencia en diversas áreas. Esta visualización es fundamental para comprender la propagación global de la enfermedad.")
st.write("##")

fechas = df1.columns[4:]

# Filtrar datos por regiones
sudamerica_data = df1[df1['Country/Region'].isin(sudamerica_countries)]
centroamerica_data = df1[df1['Country/Region'].isin(centroamerica_paises)]
africa_data = df1[df1['Country/Region'].isin(africa_paises)]
europa_data = df1[df1['Country/Region'].isin(europa_paises)]
asia_data = df1[df1['Country/Region'].isin(asia_paises)]
oceania_data = df1[df1['Country/Region'].isin(oceania_paises)]

# Calcular la suma total de casos por región
suma_total_sudamerica = sudamerica_data[fechas].sum().sum()
suma_total_centroamerica = centroamerica_data[fechas].sum().sum()
suma_total_africa = africa_data[fechas].sum().sum()
suma_total_europa = europa_data[fechas].sum().sum()
suma_total_asia = asia_data[fechas].sum().sum()
suma_total_oceania = oceania_data[fechas].sum().sum()

# Convertir los datos en formato 'melted' para su visualización
melted_sudamerica_df1 = pd.melt(sudamerica_data, id_vars=['Province/State'], value_vars=fechas, var_name='Fecha', value_name='Casos')
melted_centroamerica_df1 = pd.melt(centroamerica_data, id_vars=['Province/State'], value_vars=fechas, var_name='Fecha', value_name='Casos')
melted_africa_df1 = pd.melt(africa_data, id_vars=['Province/State'], value_vars=fechas, var_name='Fecha', value_name='Casos')
melted_europa_df1 = pd.melt(europa_data, id_vars=['Province/State'], value_vars=fechas, var_name='Fecha', value_name='Casos')
melted_asia_df1 = pd.melt(asia_data, id_vars=['Province/State'], value_vars=fechas, var_name='Fecha', value_name='Casos')
melted_oceania_df1 = pd.melt(oceania_data, id_vars=['Province/State'], value_vars=fechas, var_name='Fecha', value_name='Casos')

# Creación del gráfico combinado de evolución de casos confirmados por continente
combined_chart1 = (
    alt.layer(
        # Gráfico de Sudamérica
        alt.Chart(melted_sudamerica_df1).mark_line(point=True, color='#D90A00', size=1).encode(
            y=alt.Y('sum(Casos):Q'),
            x=alt.X('Fecha:T', title='Fecha', axis=alt.Axis(format='%b %Y')),
            color=alt.ColorValue('#D90A00'),  
            tooltip=[
                alt.Tooltip('Fecha:T', title='Fecha'),
                alt.Tooltip('sum(Casos):Q', title='Muertes en Sudamerica', format=','),
            ]
        ),
        # Gráfico de Centroamérica
        alt.Chart(melted_centroamerica_df1).mark_line(point=True, color='#FF6D04').encode(
            y=alt.Y('sum(Casos):Q'),
            x=alt.X('Fecha:T'),
            color=alt.ColorValue('#FF6D04'), 
            tooltip=[
                alt.Tooltip('Fecha:T', title='Fecha'),
                alt.Tooltip('sum(Casos):Q', title='Muertes en Norteamerica', format=',')
            ]
        ),
        # Gráfico de África
        alt.Chart(melted_africa_df1).mark_line(point=True, color='#FF2B2F').encode(
            y=alt.Y('sum(Casos):Q'),
            x=alt.X('Fecha:T', title='Fecha'),
            color=alt.value('#FF2B2F'), 
            tooltip=[
                alt.Tooltip('Fecha:T', title='Fecha'),
                alt.Tooltip('sum(Casos):Q', title='Muertes en Africa', format=',')
            ]
        ),
        # Gráfico de Europa
        alt.Chart(melted_europa_df1).mark_line(point=True, color='red').encode(
            y=alt.Y('sum(Casos):Q'),
            x=alt.X('Fecha:T'),
            color=alt.value('red'), 
            tooltip=[
                alt.Tooltip('Fecha:T', title='Fecha'),
                alt.Tooltip('sum(Casos):Q', title='Muertes en Europa', format=',')
            ]
        ),
        # Gráfico de Asia
        alt.Chart(melted_asia_df1).mark_line(point=True, color='#FF9A61').encode(
            y=alt.Y('sum(Casos):Q'),
            x=alt.X('Fecha:T'),
            color=alt.value('#FF9A61'), 
            tooltip=[
                alt.Tooltip('Fecha:T', title='Fecha'),
                alt.Tooltip('sum(Casos):Q', title='Muertes en Asia', format=',')
            ]
       ),
        # Gráfico de Oceanía
        alt.Chart(melted_oceania_df1).mark_line(point=True, color='#FF530E').encode(
            y=alt.Y('sum(Casos):Q'),
            x=alt.X('Fecha:T'),
            color=alt.value('#FF530E'), 
            tooltip=[
                alt.Tooltip('Fecha:T', title='Fecha'),
                alt.Tooltip('sum(Casos):Q', title='Muertes en Oceania', format=',')
            ]
       ).interactive()  # Hace que el gráfico sea interactivo
    )
)

# Mostrar el gráfico combinado de evolución de casos confirmados para varios continentes
st.altair_chart(combined_chart1, use_container_width=True)

# Sección de éxito con información adicional
st.error("El gráfico lineal representa la evolución de las muertes causadas por COVID-19 en diferentes continentes. Se destaca un aumento significativo en Asia después del 7 de agosto, alcanzando un pico de un millón de muertes. Se observa un incremento repentino de 100,000 muertes en un solo día entre el 14 y 15 de junio. Europa y Norteamérica muestran una tendencia constante con cifras similares. Sudamérica, al inicio, presenta números comparables a otras regiones, pero posteriormente experimenta una disminución considerable en muertes. África registra cifras más bajas, y Oceanía se mantiene por debajo de las 250,000 muertes.")


st.write("##")
st.title("Evolución de Muertes por País en Múltiples Continentes 🗺️")
st.write("Este segmento se enfoca en un análisis detallado de la evolución de los casos confirmados por país en diferentes continentes. Su objetivo principal es ampliar la perspectiva presentada en los gráficos anteriores, ofreciendo un detallado análisis de la incidencia del virus en los diez países más relevantes de cada continente.")
st.caption("Se muestran los 10 países más relevantes por continente.")
# Crear columnas para Asia y Europa
Asia, Europa = st.columns(2, gap='large')

# Gráfico de Europa
with Europa:
    st.subheader("Evolución de Casos de COVID-19 en Países Europeos")
    europa_data = df1[df1['Country/Region'].isin(europa_paises)]
    fecha_columnas = df1.columns[4:].tolist()

    europa_df1 = pd.melt(europa_data, id_vars=['Country/Region'], value_vars=fecha_columnas, var_name='Fecha', value_name='Casos')

    # Filtrar solo los 10 países con más casos
    top_10_europa = europa_df1.groupby('Country/Region')['Casos'].max().nlargest(10).index
    europa_df1_top_10 = europa_df1[europa_df1['Country/Region'].isin(top_10_europa)]

    chart_europa1 = (alt.Chart(europa_df1_top_10).mark_bar().encode(
            x=alt.X('Casos:Q'),
            y=alt.Y('Country/Region:N', sort='-x'),
            color=alt.Color('Country/Region:N', scale=alt.Scale(scheme='reds')),
            tooltip=[
                alt.Tooltip('Country/Region:N', title='Pais'),
                alt.Tooltip('Casos:Q', title='Muertes en Europa', format=',')
            ]
        ).properties(
            width=800,
            height=400
        )
    )

    st.altair_chart(chart_europa1, use_container_width=True)

# Gráfico de Asia
with Asia:
    # Título y encabezado del gráfico para países asiáticos
    st.subheader("Evolución de Casos de COVID-19 en Países Asiaticos")
    
    # Filtrar los datos para países de Asia
    asia_data = df1[df1['Country/Region'].isin(asia_paises)]
    fecha_columnas = df1.columns[4:].tolist()

    # Preparación de datos para el gráfico de Asia
    asia_df1 = pd.melt(asia_data, id_vars=['Country/Region'], value_vars=fecha_columnas, var_name='Fecha', value_name='Casos')

    # Seleccionar los 10 países con más casos en Asia
    top_10_asia = asia_df1.groupby('Country/Region')['Casos'].max().nlargest(10).index
    asia_df1_top_10 = asia_df1[asia_df1['Country/Region'].isin(top_10_asia)]

    # Creación del gráfico de barras para Asia
    chart_asia1 = (
        alt.Chart(asia_df1_top_10)
        .mark_bar()
        .encode(
            x=alt.X('Casos:Q'),
            y=alt.Y('Country/Region:N', sort='-x'),
            color=alt.Color('Country/Region:N', scale=alt.Scale(scheme='reds')),
            tooltip=[
                alt.Tooltip('Country/Region:N', title='Pais'),
                alt.Tooltip('Casos:Q', title='Muertes en Asia', format=',')
            ]
        ).properties(
            width=800,
            height=400
        )
    )

    st.altair_chart(chart_asia1, use_container_width=True)

# División de la pantalla en dos columnas
sur, centro = st.columns(2, gap='large')

# Gráfico de Sudamérica de muertes
with sur:
    st.subheader("Evolución de Casos de COVID-19 en Sudamérica")
    sudamerica_data = df1[df1['Country/Region'].isin(sudamerica_countries)]
    fecha_columnas = df1.columns[4:].tolist()

    # Procesamiento de datos para el gráfico de Sudamérica
    sur_df1 = pd.melt(sudamerica_data, id_vars=['Country/Region'], value_vars=fecha_columnas, var_name='Fecha', value_name='Casos')
    top_10_sur = sur_df1.groupby('Country/Region')['Casos'].max().nlargest(10).index
    sur_df1_top_10 = sur_df1[sur_df1['Country/Region'].isin(top_10_sur)]

    # Creación del gráfico de barras para Sudamérica
    chart_sur = (alt.Chart(sur_df1_top_10).mark_bar().encode(
            x=alt.X('Casos:Q'),
            y=alt.Y('Country/Region:N', sort='-x'),
            color=alt.Color('Country/Region:N', scale=alt.Scale(scheme='reds')),
            tooltip=[
                alt.Tooltip('Country/Region:N', title='País'),
                alt.Tooltip('Casos:Q', title='Muertes en Sudamérica', format=',')
            ]
        ).properties(
            width=800,
            height=400
        )
    )

    st.altair_chart(chart_sur, use_container_width=True)

# Gráfico de Centroamérica de muertes
with centro:
    st.subheader("Evolución de Casos de COVID-19 en Centroamérica")
    centroamerica_data = df1[df1['Country/Region'].isin(centroamerica_paises)]

    # Procesamiento de datos para el gráfico de Centroamérica
    centro_df1 = pd.melt(centroamerica_data, id_vars=['Country/Region'], value_vars=fecha_columnas, var_name='Fecha', value_name='Casos')
    top_10_centro = centro_df1.groupby('Country/Region')['Casos'].max().nlargest(10).index
    centro_df1_top_10 = centro_df1[centro_df1['Country/Region'].isin(top_10_centro)]

    # Creación del gráfico de barras para Centroamérica
    chart_centro = (
        alt.Chart(centro_df1_top_10).mark_bar().encode(
            x=alt.X('Casos:Q'),
            y=alt.Y('Country/Region:N', sort='-x'),
            color=alt.Color('Country/Region:N', scale=alt.Scale(scheme='reds')),
            tooltip=[
                alt.Tooltip('Country/Region:N', title='País'),
                alt.Tooltip('Casos:Q', title='Muertes en Centroamérica', format=',')
            ]
        ).properties(
            width=800,
            height=400
        )
    )

    st.altair_chart(chart_centro, use_container_width=True)

# Información adicional sobre los gráficos
st.error("Los gráficos muestran la distribución de fallecimientos por COVID-19 en distintos continentes. En sus respectivas regiones, Brasil y Estados Unidos lideran con cifras que superan medio millón y un millón de fallecimientos, respectivamente. En Asia, India se encuentra a la cabeza seguida por Rusia. En Europa, se observa una distribución más uniforme, aunque Gran Bretaña destaca con más de 200 mil fallecimientos, a diferencia de la mayoría de los países que registran entre 100 mil y 200 mil fallecidos.")



# Conclusiones del Proyecto
st.write("---")
st.title("Conclusiones del Proyecto")
conclusiones = """
Este análisis brinda una perspectiva global de la pandemia de COVID-19 y presenta hallazgos clave con implicaciones significativas:

1. **Tendencia de Crecimiento Sostenido:** A medida que la pandemia avanza, se observa un incremento constante en los casos confirmados y las defunciones, lo que subraya la necesidad de fortalecer las medidas de control y prevención para contener la propagación del virus.

2. **Disparidades Regionales Significativas:** Se revelan notables diferencias entre países y regiones en tasas de incidencia y letalidad. Destacando la importancia de adaptar estrategias de salud pública a las condiciones locales, considerando las variaciones regionales al asignar recursos y tomar decisiones.

3. **Relevancia de Medidas de Control y Prevención:** Los resultados subrayan la importancia crucial de implementar y mantener medidas efectivas, como el distanciamiento social, el uso de mascarillas y la vacunación, para reducir la propagación del virus y minimizar su impacto.

4. **Limitaciones de los Datos:** Reconocer las limitaciones en la calidad de las fuentes y la posibilidad de subregistro de casos es fundamental. Resalta la necesidad de mejorar la calidad y disponibilidad de los datos para una toma de decisiones más precisa.

5. **Datos para la Toma de Decisiones:** Este análisis proporciona información valiosa para autoridades sanitarias, investigadores y la comunidad en general, facilitando la comprensión del impacto de la pandemia y contribuyendo a decisiones informadas. Estos datos pueden guiar la asignación de recursos y la planificación de estrategias de respuesta a la pandemia.

En resumen, estos hallazgos ofrecen implicaciones significativas para la gestión de la pandemia de COVID-19. Las lecciones extraídas pueden ser vitales en la formulación de políticas, la toma de decisiones estratégicas y la implementación de medidas efectivas para combatir la propagación del virus y resguardar la salud pública.
"""


st.markdown(conclusiones)
# Información de Contacto
st.write("---")
st.header("¡Gracias por revisar este proyecto!")
st.subheader("Contacto: Alvarezlucianoezequiel@gmail.com")
