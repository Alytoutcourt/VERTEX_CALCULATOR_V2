import streamlit as st
import ifcopenshell
import ifcopenshell.geom
import multiprocessing

def main():
    st.title("Informations géométriques dans un fichier IFC")

    # Chargement du fichier IFC
    uploaded_file = st.file_uploader("Uploader le fichier IFC", type=['ifc'])
    if not uploaded_file:
        st.warning("Veuillez uploader un fichier IFC.")
        return

    # Convertit le contenu du fichier en objet IFC à l'aide de ifcopenshell
    ifc_file = ifcopenshell.file.from_string(uploaded_file.getvalue().decode("utf-8"))

    # Configuration des paramètres pour la géométrie
    settings = ifcopenshell.geom.settings()

    # Création d'un itérateur pour extraire la géométrie
    Element = ifc_file.by_type('IfcProduct')
    iterator = ifcopenshell.geom.iterator(settings, ifc_file, multiprocessing.cpu_count(), include=Element)
    # Initialisation de l'itérateur
    if iterator.initialize():
        verts_list = []

        # Parcours de la géométrie
        while True:
            shape = iterator.get()
            if shape is None:
                break
            
            # Récupération des sommets
            verts = shape.geometry.verts

            # Ajout des informations à la liste respective
            verts_list.extend(verts)

            if not iterator.next():
                break

        # Affichage des informations dans un tableau
        st.write("### Sommets")
        st.write(len(verts_list))

if __name__ == "__main__":
    main()
