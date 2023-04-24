import pandas as pd 
import streamlit as st 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
import plotly.express as px

##################  PLOTLY ##################
st.header("Plotly")
   # DataFrames de temperatures hebdomadaires
temps = pd.DataFrame(

    { 'day' : ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
      'temperature' : [28, 27, 25, 31, 32, 35, 36]
    
    }
)
# st.write(temps)
fig = px.bar(
    data_frame = temps, x = "day",
    y = "temperature", title = "Temperature moyennes journalieres"

)
st.plotly_chart(fig)

# nuage de points interactif
Salaries = pd.read_csv ("Salary_Data.csv")
st.dataframe(Salaries)

numeric_cols = Salaries.select_dtypes(exclude = "object").columns.to_list()
var_x = st.selectbox("Choisis la variable en abscisse", numeric_cols)
var_y = st.selectbox("Choisis de la variable en ordonnee", numeric_cols)

fig2 = px.scatter(
    data_frame = Salaries,
    x = var_x,
    y = var_y,
    title=str(var_y) + " VS " + str(var_x)
)
st.plotly_chart(fig2)