import pandas as pd
import streamlit as st
from datetime import datetime
from streamlit_player import st_player



# Interface Streamlit
st.set_page_config(page_title="Accueil", page_icon=":house:")

st.title("Formatteur CSV pour Listmonk")
st.markdown("""
## Bienvenue dans l'outil de conversion CSV
Cette application vous permet de convertir un fichier CSV contenant des informations telles que l'email, le prénom et le nom en un format adapté pour l'importation dans Listmonk. Il a, à la base, été conçu pour fonctionner avec le logiciel Heiz System.

### Instructions
- Créer un export CSV via Heiz System.
- Assurez-vous d'exporter les informations suivantes : email, prénom et nom.
- L'ordre a de l'importance uniquement pour l'email, qui doit être placé en premier afin de respecter la structure de Listmonk. Tout cela est modifiable dans les paramètres d'exportation de Heitz System
- Une fois votre export terminé, uploader votre fichier dans le convertisseur
- Le convertisseur vous donnera un fichier CSV prêt à être importé directement dans Listmonk
- Pour avoir plus de détail sur le fonctionnement exact de l'outil, vous pouvez consulter la section plus bas""")

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
- L'outil vérifiera la présence des colonnes `email`, `prenom`, et `nom` dans votre fichier CSV.
- ATTENTION, il faut que la première colonne soit `email` pour que l'outil fonctionne correctement.
- Le fichier sera modifié afin de répondre au besoin de Listmonk pour l'importation. L'outil créera également l'entête `email,name`.
- Puis, afin d'automatiser le procéssus au maximum, le fichier sera automatiquement encodé en UTF-8 le rendant directement importable dans Listmonk.

## Contact
En cas de problème, de question ou de demande d'ajout de fonctionnalité, vous pouvez [me contacter ici](https://github.com/Char1esD/Heitz-System-CSV-Converter/issues/new/choose).
""", unsafe_allow_html=True)


