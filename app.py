import streamlit as st
import pandas as pd
import plotly.express as px

player_data = pd.read_csv('euro2024_players.csv')
')

# Limpiar un poco los datos

player_data.columns = player_data.columns.str.lower()
player_data = player_data.rename(columns={'marketvalue': 'market_value'})


st.header("Jugadores de la Eurocopa 2024")

# Hacer un botón que abra un histograma
hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    fig = px.histogram(player_data, x="market_value", color="position",
                       title="Histograma de valor de mercado por posición",
                       labels={"market_value": "Valor de mercado",
                               "position": "Posición"},
                       color_discrete_sequence=px.colors.qualitative.Plotly)

    st.plotly_chart(fig, use_container_width=True)

    scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write(
        'Creación de un gráfico de dispersión para el conjunto de datos')

    scatter_fig = px.scatter(player_data, x="age", y="market_value", color="position",
                             title="Gráfico de dispersión: Edad vs Valor de mercado",
                             labels={"age": "Edad", "market_value": "Valor de mercado",
                                     "position": "Posición"},
                             color_discrete_sequence=px.colors.qualitative.Plotly)

    st.plotly_chart(scatter_fig, use_container_width=True)
