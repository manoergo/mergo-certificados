import streamlit as st
import pandas as pd
import os

# ---------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA
# ---------------------------------------------------

st.set_page_config(
    page_title="Validación de Certificados MERGO",
    page_icon="✅",
    layout="centered"
)

# ---------------------------------------------------
# TÍTULO
# ---------------------------------------------------

st.title("Validación de Certificados")
st.subheader("MERGO ACADEMY")

st.write(
    "Ingrese el código de validación que figura en el certificado."
)

# ---------------------------------------------------
# RUTA DEL EXCEL
# ---------------------------------------------------

ruta_excel = "CERTIFICADOS.xlsx"

# ---------------------------------------------------
# VERIFICAR SI EXISTE EL ARCHIVO
# ---------------------------------------------------

if os.path.exists(ruta_excel):

    # CARGAR EXCEL
    df = pd.read_excel(
        ruta_excel,
        engine="openpyxl"
    )

    # LIMPIAR NOMBRES DE COLUMNAS
    df.columns = df.columns.str.strip()

    # ---------------------------------------------------
    # INPUT DEL CÓDIGO
    # ---------------------------------------------------

    codigo = st.text_input(
        "Código de validación"
    ).strip().upper()

    # ---------------------------------------------------
    # VALIDACIÓN
    # ---------------------------------------------------

    if codigo:

        resultado = df[
            df["codigo"]
            .astype(str)
            .str.strip()
            .str.upper() == codigo
        ]

        if not resultado.empty:

            cert = resultado.iloc[0]

            st.success("✅ CERTIFICADO VÁLIDO")

            st.markdown("---")

            st.markdown(f"""
            ### Datos del certificado

            **Participante:**  
            {cert['Participante']}

            **Curso:**  
            {cert['Curso']}

            **Duración:**  
            {cert['Horas']}

            **Fecha de emisión:**  
            {cert['Fecha']}

            **Código de validación:**  
            {cert['codigo']}

            **Estado:**  
            {cert['Estado']}
            """)

            st.markdown("---")

            st.info(
                "Certificado emitido oficialmente por MERGO ACADEMY "
                "con respaldo de la Sociedad Peruana de Ergonomía (SOPERGO)."
            )

        else:

            st.error(
                "❌ El código ingresado no corresponde "
                "a un certificado registrado."
            )

else:

    st.error("❌ No se encontró el archivo Excel.")

    st.write("Ruta buscada:")
    st.code(ruta_excel)
