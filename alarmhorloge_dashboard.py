
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_title="Alarmhorloge Dashboard")

st.title("📊 Alarmhorloge Dashboard")

# Upload
uploaded_file = st.file_uploader("Upload de standaardexport (Excel)", type=["xlsx"])

if uploaded_file:
    # Data inlezen
    df_verkoop = pd.read_excel(uploaded_file, sheet_name="Verkoop laatste 14 dagen")
    df_abonnementen = pd.read_excel(uploaded_file, sheet_name="Lopende abonnementen")
    df_tellingen = pd.read_excel(uploaded_file, sheet_name="Actieve tellingen")

    st.header("📍 Actieve tellingen")
    st.dataframe(df_tellingen)

    st.header("📈 Verkochte horloges per dag (laatste 14 dagen)")
    fig1, ax1 = plt.subplots()
    ax1.plot(df_verkoop['Datum'], df_verkoop['Aantal horloges zonder einddatum'], marker='o')
    ax1.set_xlabel("Datum")
    ax1.set_ylabel("Aantal")
    ax1.set_title("Verkochte horloges per dag")
    ax1.grid(True)
    st.pyplot(fig1)

    st.header("📆 Lopende actieve abonnementen per maand")
    fig2, ax2 = plt.subplots()
    ax2.bar(df_abonnementen['Maand'], df_abonnementen['Aantal lopende abonnementen'])
    ax2.set_xlabel("Maand")
    ax2.set_ylabel("Aantal abonnementen")
    ax2.set_title("Actieve abonnementen per maand")
    st.pyplot(fig2)

    st.success("Dashboard bijgewerkt op basis van geüploade gegevens.")
else:
    st.info("⬆️ Upload een Excel-bestand met de drie standaard tabbladen om te beginnen.")
