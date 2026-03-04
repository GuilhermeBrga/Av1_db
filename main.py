import streamlit as st # rodar o comando no terminal "streamlit run main.py" para rodar o código

st.title("Interface gráfica da AV1 de Projeto de banco de dados")

st.header("Alunos: ")
st.subheader("João Guilherme Braga Nascimento / 2210285")
st.subheader("Levy Gomes Porfirio Brito / 2223882")
st.subheader("Lucas Diniz Frota / 2310302")

st.divider()

st.header("Informe o arquivo a ser lido: ")

archive = st.file_uploader("Escolha um arquivo", type=["txt", "csv"])

if archive is not None:
    st.success("Arquivo enviado com sucesso!")

    content = archive.read().decode("utf-8").splitlines()
    st.text(content)