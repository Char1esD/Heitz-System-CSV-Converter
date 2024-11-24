import streamlit as st
from datetime import datetime
import pandas as pd
import unicodedata

def normalize_column_names(columns):
    normalized_columns = []
    for col in columns:
        col_normalized = ''.join(
            c for c in unicodedata.normalize('NFD', col) if unicodedata.category(c) != 'Mn'
        ).lower()
        normalized_columns.append(col_normalized)
    return normalized_columns

def formater_csv(file_csv, output_csv):
    try:
        df = pd.read_csv(file_csv, sep=None, engine='python')
    except Exception as e:
        st.error(f"Erreur lors de la lecture du fichier : {e}")
        return None

    df.columns = normalize_column_names(df.columns)

    required_columns = {'email', 'prenom', 'nom'}
    if not required_columns.issubset(df.columns):
        st.error("Erreur : Les colonnes 'email', 'prenom' et 'nom' sont absentes dans le fichier CSV.")
        return None
    
    df['email_name'] = df.apply(lambda row: f"{row['email']}, {row['nom'].upper()} {row['prenom']}", axis=1)

    df_final = df[['email_name']]

    df_final.columns = ['email,name']

    lines = [','.join(df_final.columns)] + df_final['email,name'].tolist()

    with open(output_csv, 'w', encoding='utf-8') as final_file:
        final_file.write('\n'.join(lines))

    return output_csv

st.set_page_config(page_title="Convertisseur CSV", page_icon=":file_folder:")

st.title("Convertisseur CSV pour Listmonk")

st.markdown("## Déposez votre fichier CSV ici")

uploaded_file = st.file_uploader("Veillez à ce que le fichier soit au format CSV", type=["csv"], accept_multiple_files=False)

if uploaded_file is not None:
    original_filename = uploaded_file.name.split('.')[0]

    now = datetime.now()
    date = now.strftime("%d.%m.%Y")
    output_filename = f"{original_filename}.formaté.{date}.csv"

    input_path = f"/tmp/{uploaded_file.name}"
    output_path = f"/tmp/{output_filename}"

    with open(input_path, 'wb') as temp_file:
        temp_file.write(uploaded_file.getbuffer())

    result = formater_csv(input_path, output_path)

    if result:
        st.success(f"Fichier formaté avec succès : {output_filename}")
        with open(output_path, 'rb') as file:
            st.download_button(
                label="Télécharger le fichier formaté",
                data=file,
                file_name=output_filename,
                mime="text/csv"
            )
