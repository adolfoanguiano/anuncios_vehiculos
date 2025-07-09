import pandas as pd
import plotly.express as px
import streamlit as st

#Encabezado
st.header('Análisis de anuncios de vehículos de EE.UU.')

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

display_button = st.button('Mostrar datos') # crear un botón para mostrar los datos

if display_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Conjunto de datos de anuncios de venta de coches (10 primeros)')
    
    # mostrar los primeros 10 registros del conjunto de datos
    st.dataframe(car_data.head(10))

hist_button = st.button('Construir histograma') # crear un botón para histograma
     
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir gráfico de dispersión') # crear botón para gráfico dispersión

if disp_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
