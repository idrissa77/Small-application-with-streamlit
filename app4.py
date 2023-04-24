import pandas as pd 
import streamlit as st 
import numpy as np 

st.title("Initialisation a la Data Viz des donnees.")
st.subheader("Auteur : Idrissa")
st.markdown("***Cette application affiche differents types de graphiques***")

#Trace lic=neaire
random_data = np.random.normal(size = 1000)
st.line_chart(random_data)

# Diagramme a barre 
bar_data = pd.DataFrame(
    [100, 19, 88, 54],
    ["A", "b", "C", "D"]
)
st.bar_chart(bar_data)

# 