import streamlit as st

inicio = st.Page("inicio.py", title="Inicio", icon="🏚️")
sistema = st.Page("sistema_de_calculo.py", title="Sistema de Calculo de cachê", icon="🧮")

pg = st.navigation([inicio, sistema])
st.set_page_config(page_title="Sistema MRSYSTEM", page_icon="💻")
pg.run()