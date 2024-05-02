import streamlit as st
import pandas as pd
import ifcopenshell
import ifcopenshell.geom
import ifcopenshell.util.shape
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

    # Récupération de tous les produits dans le fichier IFC
    products = ifc_file.by_type('IfcElement')

    # Création d'un DataFrame pour les informations sur les produits
    product_info = []
    for product in products:
        product_name = product.Name
        product_guid = product.GlobalId
        product_id = product.id()

        # Recherche des entités géométriques associées à ce produit
        product_geom = ifcopenshell.geom.create_shape(settings, product)
        verts_count = 0
        grouped_verts = ifcopenshell.util.shape.get_vertices(product_geom.geometry)
        verts_count += len(grouped_verts)
        product_info.append((product_name, product_id.__str__(), product_guid, verts_count))

    df = pd.DataFrame(product_info, columns=["Nom","Id", "GUID", "Nombre de VERTEX"])

    # Affichage du DataFrame dans un tableau interactif
    st.write("### Informations sur les produits:")
    st.dataframe(df)

if __name__ == "__main__":
    main()
