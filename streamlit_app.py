import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Exemple d'application avec Streamlit")

x = np.linspace(0, 10, 100)
a = st.slider("Choisissez un coefficient", 0.0, 5.0, 1.0)
y = a * np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)