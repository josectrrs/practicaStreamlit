# This is a sample Python script.
import streamlit as st
import pandas as pd
import plotly.express as px
# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    st.title('José Piña')
    st.title('_Streamlit_ is :blue[cool] :sunglasses:')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Jose')
    #Leer datos
    datosVuelos = pd.read_csv("datos/lax_to_jfk.csv")
    st.dataframe(datosVuelos)

    st.title("Gráficas")
    #Agrupar por mes los retrasos de llegadas (ArrDelay)
    retrasos = datosVuelos.groupby("Month")["ArrDelay"].mean().reset_index()
    st.dataframe(retrasos)

    #Primero creamos la fig
    fig = px.line(retrasos, "Month", "ArrDelay")
    fig.update_layout(title="Gráfica Mes Vs. Retrasos promedio")

    #Motramos la gráfica
    st.plotly_chart(fig, use_container_width=True)

    st.title("Gráfica de dispersión")
    fig = px.scatter(datosVuelos, x="ArrTime", y="DepTime")
    st.plotly_chart(fig, use_container_width=True)

    st.title("Gráfica de barras")

    vuelos_x_mes = datosVuelos.groupby("Month")["FlightDate"].count().reset_index()
    vuelos_x_mes = vuelos_x_mes.rename(columns={"FlightDate": "Number of Flights"})

    fig = px.bar(vuelos_x_mes, x="Month", y="Number of Flights")
    fig.update_layout(title="Número de Vuelos por Mes",
                      xaxis_title="Mes",
                      yaxis_title="Número de Vuelos")

    st.plotly_chart(fig, use_container_width=True)

    st.title("Gráfica de pie")
    st.subheader("Distribución de vuelos por aerolínea")

    dfAerolineas = datosVuelos.groupby("Reporting_Airline")["Origin"].count().reset_index()
    st.dataframe(dfAerolineas)
    st.write(dfAerolineas.columns)

    dfValue = datosVuelos["Reporting_Airline"].value_counts()
    st.dataframe(dfValue)
    
    fig = px.pie(dfAerolineas, values="Origin", names="Reporting_Airline", title="Porcentaje vuelos por aerolínea")
    st.plotly_chart(fig, use_container_width=True)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
