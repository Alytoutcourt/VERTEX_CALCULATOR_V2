import os
import streamlit as st

st.title("File Uploader")

# Charger le fichier
uploaded_file = st.file_uploader("Uploader un fichier", type=["txt", "csv", "pdf"])

# Vérifier si un fichier a été téléchargé
if uploaded_file is not None:
    # Enregistrer le fichier dans un répertoire temporaire
    with open(os.path.join("temp_files", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    # Obtenir le chemin absolu du fichier sur le serveur
    file_path = os.path.abspath(os.path.join("temp_files", uploaded_file.name))
    st.write(f"Le fichier a été téléchargé avec succès. Chemin du fichier sur le serveur : {file_path}")
