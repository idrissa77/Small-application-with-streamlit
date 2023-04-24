import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Application de distribution")
st.subheader("Auteur : Idrissa")
st.write(
    "Cette application permet d'afficher l'histogramme d'une distribution normale."
     " L'utilisateur a la possiblite de faire varier le nombre de bins de l'histogramme"
     " et de donner un titre au graphique."

)

data = np.random.normal(size=1000)
data = pd.DataFrame(data, columns=["Dist_norm"])
st.write(data.head())
#st.dataframe(data.head())

fig, ax = plt.subplots()
n_bins = st.number_input(
    label = "Choisis le nombre de bins",
    min_value = 10,
    value = 20
)

graph_title = st.text_input( 
    label ="Ecrire le titre du graphe"
)
plt.title(graph_title)
ax.hist(data.Dist_norm, bins=n_bins)
st.pyplot(fig)