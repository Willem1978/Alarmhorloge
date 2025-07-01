
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_title="Alarmhorloge Dashboard")

st.markdown("<h1 style='color:magenta;'>📊 Alarmhorloge Dashboard</h1>", unsafe_allow_html=True)

# Upload
uploaded_file = st.file_uploader("⬆️ Upload hier de standaardexport (Excel)", type=["xlsx"])

if uploaded_file:
    # Data inlezen
    df_verkoop = pd.read_excel(uploaded_file, sheet_name="Verkoop laatste 14 dagen")
    df_abonnementen = pd.read_excel(uploaded_file, sheet_name="Lopende abonnementen")
    df_tellingen = pd.read_excel(uploaded_file, sheet_name="Actieve tellingen")

    # Lay-out in kolommen
    st.markdown("### 📍 Actieve tellingen")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Actieve abonnementen", value=int(df_tellingen.iloc[0, 1]))
    with col2:
        st.metric(label="Uitleen binnen periode", value=int(df_tellingen.iloc[1, 1]))
    with col3:
        st.metric(label="Uitleen buiten periode", value=int(df_tellingen.iloc[2, 1]))

    st.markdown("---")

    # Verkoopgrafiek
    st.markdown("### 📈 Verkochte horloges per dag (laatste 14 dagen)")
    fig1, ax1 = plt.subplots(figsize=(10, 4))
    ax1.plot(df_verkoop['Datum'], df_verkoop['Aantal horloges zonder einddatum'], marker='o', color='magenta', linewidth=2)
    for i, v in enumerate(df_verkoop['Aantal horloges zonder einddatum']):
        ax1.text(df_verkoop['Datum'][i], v + 0.1, str(v), ha='center', fontsize=8, color='black')
    ax1.set_xlabel("Datum")
    ax1.set_ylabel("Aantal")
    ax1.set_title("Verkochte horloges per dag", fontsize=14, color='magenta')
    ax1.grid(True, linestyle='--', alpha=0.5)
    st.pyplot(fig1)

    # Abonnementen per maand
    st.markdown("### 📆 Lopende actieve abonnementen per maand")
    fig2, ax2 = plt.subplots(figsize=(10, 4))
    bars = ax2.bar(df_abonnementen['Maand'], df_abonnementen['Aantal lopende abonnementen'], color='magenta')
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2.0, height + 0.5, f'{int(height)}', ha='center', fontsize=8)
    ax2.set_xlabel("Maand")
    ax2.set_ylabel("Aantal abonnementen")
    ax2.set_title("Actieve abonnementen per maand", fontsize=14, color='magenta')
    ax2.tick_params(axis='x', rotation=45)
    st.pyplot(fig2)

    st.success("✅ Dashboard bijgewerkt op basis van je gegevens.")
else:
    st.info("📄 Upload een Excel-bestand met de drie standaard tabbladen om te beginnen.")
