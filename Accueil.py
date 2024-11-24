import pandas as pd
import streamlit as st
from datetime import datetime
from streamlit_player import st_player



# Interface Streamlit
st.set_page_config(page_title="Accueil", page_icon=":house:")

st.title("Convertisseur CSV pour Listmonk")
st.markdown("""
    ## Bienvenue dans l'outil de conversion CSV
    Cette application vous permet de convertir un fichier CSV contenant des informations telles que l'email, le prénom et le nom, en un format compatible avec l'importation dans Listmonk. Elle a été conçue à l'origine pour fonctionner avec le logiciel Heiz System.

    ### Instructions
    - Créez un export CSV depuis Heitz System.
    - Assurez-vous d'inclure les informations suivantes : email, prénom et nom.
    - L'ordre des colonnes n'a d'importance que pour l'email, qui doit impérativement être placé en première position afin de respecter la structure requise par Listmonk. Vous pouvez ajuster cet ordre dans les paramètres d'exportation de Heiz System.
    - Une fois l'export terminé, téléchargez votre fichier dans le convertisseur.
    - Le convertisseur générera un fichier CSV prêt à être importé directement dans Listmonk.
    - Pour plus de détails sur le fonctionnement précis de l'outil, consultez la section ci-dessous.
""")

st.page_link("pages/Convertisseur_CSV.py", label="Accéder au convertisseur", icon="📁")

with open("./config/Exemple.csv", "rb") as file:
    btn = st.download_button(
        label="Télécharger un fichier d'exemple",
        data=file,
        file_name="Exemple.csv",
        mime="csv/text",
    )
video_file = open("./config/Utilisation-CSV-Converter.webm", "rb")
video_bytes = video_file.read()

st.video(video_bytes)

st.markdown("""
    ### Fonctionnement
    - L'outil vérifiera la présence des colonnes `email`, `prénom` et `nom` dans votre fichier CSV.
    - ATTENTION : la première colonne doit impérativement être `email` pour que l'outil fonctionne correctement.
    - Le fichier sera ajusté pour répondre aux exigences de Listmonk en matière d'importation. L'outil ajoutera également l'en-tête `email,name`.
    - Enfin, pour automatiser le processus au maximum, le fichier sera automatiquement encodé en UTF-8, le rendant directement importable dans Listmonk.

    ## Contact
    En cas de problème, de question ou de demande de fonctionnalité, vous pouvez [me contacter ici](https://github.com/Char1esD/Heitz-System-CSV-Converter/issues/new/choose).
""", unsafe_allow_html=True)
