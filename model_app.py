import streamlit as st
import joblib

# Charger le modèle pré-entraîné
model = joblib.load("regression.joblib")

st.title("Estimation Immobilière")

# Formulaire avec st.number_input pour chaque caractéristique
size = st.number_input("Taille de la maison (m²)", min_value=10.0, value=75.0, step=1.0)
rooms = st.number_input("Nombre de chambres", min_value=1, value=3, step=1)
garden = st.number_input("Présence d'un jardin (1 pour Oui, 0 pour Non)", min_value=0, max_value=1, value=0, step=1)

# Prédiction et affichage du résultat
if st.button("Estimer le prix"):
    # Le modèle attend une liste 2D : [[taille, chambres, jardin]]
    features = [[size, rooms, garden]]
    prediction = model.predict(features)
    
    st.write(f"Prix estimé : **{prediction[0]:,.2f} €**")