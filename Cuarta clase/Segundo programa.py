import streamlit as st

st.title("Calculadora de presupuesto")
st.write("Calcula el saldo después de un gasto.")

nombre = st.text_input("Nombre")

presupuesto = st.number_input(
    "Presupuesto",
    min_value=0.0,
    value=500.0,
    step=10.0,
    format="%.2f",
)

gasto = st.number_input(
    "Gasto",
    min_value=0.0,
    value=0.0,
    step=1.0,
    format="%.2f",
)

if st.button("Calcular"):
    if not nombre.strip():
        st.warning("Escribe tu nombre.")
    else:
        saldo = presupuesto - gasto

        st.write(f"Resumen de {nombre.strip()}")
        st.metric("Saldo disponible", f"${saldo:.2f}")

        if saldo > 0:
            st.success("Todavía tienes presupuesto.")
        elif saldo == 0:
            st.warning("Usaste todo el presupuesto.")
        else:
            st.error("Excediste el presupuesto.")