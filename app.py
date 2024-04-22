import streamlit as st
import ifcopenshell

st.title("IFC File Operations")

# Champ de saisie pour le chemin du fichier IFC
ifc_filepath = st.text_input("Entrez le chemin du fichier IFC")

# Vérifier si un chemin de fichier a été saisi
if ifc_filepath:
    try:
        # Ouvrir le fichier IFC
        model = ifcopenshell.open(ifc_filepath)

        # Exemple : Obtenir tous les types de murs
        st.subheader("Exemple : Obtenir tous les types de murs")
        for wall_type in model.by_type("IfcWallType"):
            st.write(f"Type de mur : {wall_type.Name}")

        # Exemple : Obtenir tous les product
        st.subheader("Exemple : Obtenir tous les ifcproduct)
        for p in model.by_type("IfcProduct"):
            st.write(f"Instance : {p.Name}")

        # Exemple : Obtenir toutes les occurrences de portes d'un type
        st.subheader("Exemple : Obtenir toutes les occurrences de portes d'un type")
        for door_type in model.by_type("IfcDoorType"):
            st.write(f"Type de porte : {door_type.Name}")
            doors = ifcopenshell.util.element.get_types(door_type)
            st.write(f"Il y a {len(doors)} portes de ce type.")
            for door in doors:
                st.write(f"Nom de la porte : {door.Name}")

        # Exemple : Obtenir le type d'un mur
        st.subheader("Exemple : Obtenir le type d'un mur")
        wall = model.by_type("IfcWall")[0]
        wall_type = ifcopenshell.util.element.get_type(wall)
        st.write(f"Le type de mur de {wall.Name} est {wall_type.Name}")

        # Exemple : Obtenir les propriétés d'un type de mur
        st.subheader("Exemple : Obtenir les propriétés d'un type de mur")
        psets = ifcopenshell.util.element.get_psets(wall_type)
        st.write(psets)
        
    except FileNotFoundError:
        st.error("Fichier IFC introuvable. Veuillez vérifier le chemin du fichier.")
