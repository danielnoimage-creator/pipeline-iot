
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql+psycopg2://iot_user:iot_password@localhost:5432/iot_database"

st.set_page_config(page_title="Dashboard IoT", page_icon="🌡️", layout="wide")

st.title("🌡️ Dashboard de Temperaturas IoT")
st.write("Análise dos registros de temperatura armazenados no PostgreSQL.")


@st.cache_resource
def conectar_banco():
    return create_engine(DATABASE_URL)


@st.cache_data(ttl=60)
def carregar_dados():
    engine = conectar_banco()

    with engine.connect() as conexao:
        resumo = pd.read_sql_query(
            text("SELECT * FROM vw_resumo_temperaturas"), conexao
        )
        categorias = pd.read_sql_query(
            text("SELECT * FROM vw_temperaturas_por_categoria"), conexao
        )
        diario = pd.read_sql_query(
            text("SELECT * FROM vw_temperaturas_por_dia ORDER BY dia"), conexao
        )

    diario["dia"] = pd.to_datetime(diario["dia"])
    return resumo, categorias, diario


try:
    resumo, categorias, diario = carregar_dados()
    r = resumo.iloc[0]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total de registros", f"{int(r['total_registros']):,}".replace(",", "."))
    col2.metric("Temperatura mínima", f"{r['temperatura_minima']:.2f}")
    col3.metric("Temperatura máxima", f"{r['temperatura_maxima']:.2f}")
    col4.metric("Temperatura média", f"{r['temperatura_media']:.2f}")

    st.subheader("Registros por categoria")
    st.bar_chart(categorias.set_index("categoria")[["total_registros"]])
    st.dataframe(categorias, use_container_width=True, hide_index=True)

    st.subheader("Temperatura média ao longo dos dias")
    diario_grafico = diario.set_index("dia")[["temperatura_media"]]
    st.line_chart(diario_grafico)

    st.subheader("Resumo diário")
    st.dataframe(diario, use_container_width=True, hide_index=True)

    st.caption("Fonte: dataset IoT carregado no PostgreSQL.")

except Exception as erro:
    st.error("Não foi possível carregar os dados do PostgreSQL.")
    st.code(str(erro))
    st.info(
        "Confira se o Docker está rodando e se as três views SQL "
        "foram criadas no projeto."
    )