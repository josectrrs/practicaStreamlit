import streamlit as st
import pandas as pd
import plotly.express as px
import calendar
from datetime import datetime

st.title("Dashboard afluencia de clientes - Café internet")
st.subheader("Alumno: José Carlos Piña Torres")

#Vamos a leer los datos
dfCafe = pd.read_excel("datos/resultadoLimpieza.xlsx")

anios = list(set(dfCafe["fechaEntrada"].dt.year))

# Obtengo los nombres de los meses y lo guardo en la variable "meses"
meses = list(set(dfCafe["fechaEntrada"].dt.month_name()))

# Ordeno los meses utilizando el índice del nombre del mes y lo guardo en la variable "meses_ordenados".
meses_ordenados = sorted(meses, key=lambda x: list(calendar.month_name).index(x))

#Vamos a usar el sidebar para mostrar los controles que nos sirven para aplicar los filtros
########################################################
#Los filtros van a ser:
#1. Año
#2. Mes


anioSeleccionado = st.sidebar.selectbox('Seleccionar año', anios)
mesSeleccionado = st.sidebar.selectbox('Seleccionar mes', meses_ordenados)

########################################################
# Antes de las gráficas mostramos también el df ya filtrado

# Obtengo el número del mes seleccionado
numero_mes_seleccionado = datetime.strptime(mesSeleccionado, "%B").month

dfFiltradoMesanio = dfCafe[(dfCafe['fechaEntrada'].dt.month == numero_mes_seleccionado) & (dfCafe['fechaEntrada'].dt.year == anioSeleccionado) ]
dfMes = dfFiltradoMesanio.groupby(pd.Grouper(key="fechaEntrada",freq="1D")).count().reset_index()
dfMes["fechaStr"] = dfMes["fechaEntrada"].astype(str) + " - "
dfMes["Día"] = dfMes["fechaEntrada"].dt.day_name() + " - " + dfMes["fechaStr"]

# En la parte central vamos a mostrar la gráfica comparativa por mes de los dos años y,


# La gráfica de días por mes seleccionado.
fig13112023 = px.bar(dfMes, x='Día', y='horaEntrada', labels={'horaEntrada': 'Número de Clientes'}, title='Número de Clientes por Semana')
st.plotly_chart(fig13112023, use_container_width=True)
