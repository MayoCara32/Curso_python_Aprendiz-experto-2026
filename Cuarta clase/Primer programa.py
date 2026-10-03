import streamlit as st

if "gastos" not in st.session_state:
    st.session_state["gastos"] = []

st.title("Mi historial")

if st.button("Agregar gasto de ejemplo"):
    st.session_state["gastos"].append(
        {"categoria": "Transporte", "monto": 35.0}
    )

st.write(st.session_state["gastos"])