# sprint7_project
Proyecto del sprint 7 del Bootcamp TripleTen

# Euro 2024 Players Dashboard

Este proyecto forma parte del Sprint 7 del bootcamp de ciencia de datos. Consiste en una aplicación web interactiva construida con **Streamlit**, que permite explorar datos de jugadores convocados a la Eurocopa 2024.

## 📌 Objetivo

Visualizar y analizar la información de los jugadores mediante gráficos interactivos, con el fin de detectar patrones interesantes relacionados con sus características y valor de mercado.

## ⚙️ Funcionalidades

- **Visualización de datos en tiempo real** con gráficos generados a partir de un conjunto de datos en formato CSV (`player_data.csv`).
- **Botón para construir un histograma** que muestra la distribución del valor de mercado por posición.
- **Botón para construir un gráfico de dispersión**, que muestra la relación entre edad y valor de mercado, también diferenciando por posición.

## 🧪 Tecnologías utilizadas

- `Streamlit`: para la creación de la interfaz web.
- `Pandas`: para la manipulación del conjunto de datos.
- `Plotly Express`: para generar visualizaciones interactivas.

## 📊 Gráficos generados

1. **Histograma de valor de mercado por posición**  
   Permite observar qué posiciones tienden a tener mayor o menor valor de mercado.

2. **Gráfico de dispersión: Edad vs Valor de mercado**  
   Ayuda a analizar si existe alguna correlación entre la edad de los jugadores y su valor actual.

## 🗂 Estructura del proyecto
sprint7_project/ │ ├── data/ │ └── player_data.csv │ ├── notebooks/ │ └── EDA.ipynb │ ├── app.py ← Código principal de Streamlit ├── requirement.txt ← Dependencias del entorno ├── .gitignore └── README.md ← Este archivo


## 📝 Cómo ejecutar la app

1. Asegúrate de tener un entorno virtual activado y con las dependencias instaladas:

```bash
pip install -r requirement.txt
```

2. Para ejecutar la aplicación puedes usar:
```bash
streamlit run app.py
```

## ✨ Autor

Proyecto desarrollado por **Diego Barocio** como parte del Sprint 7 del bootcamp **TripleTen**.
