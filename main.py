import streamlit as st
import time
from pages.page_manager import page_manager
from hash.hash_index import HashIndex
from search.table_scan import TableScan

st.title("Interface gráfica da AV1 de Projeto de banco de dados")

st.subheader("Alunos:")
st.write("João Guilherme Braga Nascimento / 2210285")
st.write("Levy Gomes Porfirio Brito / 2223882")
st.write("Lucas Diniz Frota / 2310302")

st.divider()

st.subheader("Instanciando dados:")

archive = st.file_uploader("Importe o arquivo:", type=["txt","csv"])

if archive is not None:

    st.success("Arquivo enviado com sucesso!")

    content = archive.read().decode("utf-8").splitlines()

    st.write("Quantidade de dados carregados:", len(content))

    st.divider()

    st.subheader("Configurações")

    page_size = st.number_input(
        "Informe o tamanho da página:",
        min_value=1,
        value=200,
        step=1
    )

    bucket_size = st.number_input(
        "Informe o tamanho do bucket:",
        min_value=1,
        value=5,
        step=1
    )

    st.divider()

    if st.button("Criar páginas"):

        manager = page_manager()
        manager.create_page(content, page_size)

        st.session_state.manager = manager

        st.success("Páginas criadas com sucesso!")

    if "manager" in st.session_state:

        manager = st.session_state.manager

        st.subheader("Consulta de páginas")

        st.write("Total de páginas:", manager.total_pages)

        page_choice = st.number_input(
            "Escolha a página que deseja consultar:",
            min_value=1,
            max_value=manager.total_pages,
            value=1,
            step=1
        )

        current = manager.first

        for _ in range(page_choice - 1):
            current = current.next

        st.subheader(f"Página {current.get_character()}")

        for r in current.get_register():
            st.write(r)

        st.divider()

        st.subheader("Construir índice hash")

        if st.button("Construir índice hash"):

            nb = max(1, len(content) // bucket_size)

            hash_index = HashIndex(nb, bucket_size)

            start_time = time.time()
            hash_index.build_index(manager)
            end_time = time.time()

            build_time = end_time - start_time

            st.session_state.hash_index = hash_index
            st.session_state.build_time = build_time

            st.success("Índice hash construído com sucesso!")

    if "manager" in st.session_state:

        st.divider()
        st.subheader("Busca de registros")

        key = st.text_input("Digite a palavra para buscar:")

        col1, col2 = st.columns(2)

        if col1.button("Busca Sequencial (Table Scan)"):

            manager = st.session_state.manager
            scanner = TableScan(manager)

            start_time = time.time()
            result = scanner.execute(key)
            end_time = time.time()

            search_time = end_time - start_time

            if result is None:
                st.error("Palavra não encontrada.")
            else:
                st.success(f"Encontrado na página {result}")

            st.metric("Tempo da busca sequencial (s)", f"{search_time:.6f}")

        if col2.button("Busca com Hash"):

            if "hash_index" not in st.session_state:
                st.warning("Construa o índice hash primeiro.")
            else:

                hash_index = st.session_state.hash_index

                start_time = time.time()
                result = hash_index.search(key)
                end_time = time.time()

                search_time = end_time - start_time

                if result is None:
                    st.error("Palavra não encontrada.")
                else:
                    st.success(f"Encontrado na página {result}")

                st.metric("Tempo da busca com hash (s)", f"{search_time:.6f}")

    if "hash_index" in st.session_state:

        hash_index = st.session_state.hash_index

        st.divider()
        st.subheader("Estatísticas do índice")

        col1, col2, col3 = st.columns(3)

        col1.metric("Colisões", hash_index.collisions)
        col2.metric("Buckets overflow", hash_index.overflow_count)
        col3.metric(
            "Tempo construção índice (s)",
            f"{st.session_state.build_time:.6f}"
        )

        st.write(
            "Taxa de colisão:",
            f"{hash_index.collision_rate(len(content)):.2f}%"
        )

        st.write(
            "Taxa de overflow:",
            f"{hash_index.overflow_rate():.2f}%"
        )

        st.divider()
        st.subheader("Estrutura do índice hash")

        st.write("Quantidade de buckets:", hash_index.nb)

        bucket_choice = st.number_input(
            "Escolha o bucket para visualizar:",
            min_value=1,
            max_value=hash_index.nb - 1,
            value=1,
            step=1
        )

        bucket = hash_index.buckets[bucket_choice]

        level = 0

        while bucket is not None:

            st.subheader(f"Bucket {bucket_choice} (nível {level})")

            if len(bucket.entries) == 0:
                st.write("Bucket vazio")
            else:
                for entry in bucket.entries:
                    st.write(f"Chave: {entry[0]} | Página: {entry[1]}")

            bucket = bucket.overflow
            level += 1





# import streamlit as st
# from pages.page_manager import page_manager
#
# st.title("Interface gráfica da AV1 de Projeto de banco de dados")
#
# st.subheader("Alunos: ")
# st.write("João Guilherme Braga Nascimento / 2210285")
# st.write("Levy Gomes Porfirio Brito / 2223882")
# st.write("Lucas Diniz Frota / 2310302")
#
# st.divider()
#
# st.subheader("Instanciando dados: ")
#
# archive = st.file_uploader("Importe o arquivo:", type=["txt","csv"])
#
# if archive is not None:
#     st.success("Arquivo enviado com sucesso!")
#
#     content = archive.read().decode("utf-8").splitlines()
#
#     # quantidade de dados carregados
#     st.write("Quantidade de dados carregados:", len(content))
#
#     st.divider()
#
#     st.subheader("Configurando páginas ")
#
#     page_size = st.number_input(
#         "Informe o tamanho da página:",
#         min_value=1,
#         value=100,
#         step=1
#     )
#
#     bucket_size = st.number_input(
#         "Informe o tamanho da bucket:",
#         min_value=1,
#         value=5,
#         step=1
#     )
#
#     create_pages = st.button("Criar páginas")
#
#     if create_pages:
#
#         manager = page_manager()
#         manager.create_page(content, page_size)
#
#         st.session_state.manager = manager
#
#     if "manager" in st.session_state:
#
#         manager = st.session_state.manager
#
#         st.write("Total de páginas:", manager.total_pages)
#
#         page_choice = st.number_input(
#             "Escolha a página que deseja consultar:",
#             min_value=1,
#             max_value=manager.total_pages,
#             value=1,
#             step=1
#         )
#
#         current = manager.first
#
#         for _ in range(page_choice - 1):
#             current = current.next
#
#         st.subheader(f"Página {current.get_character()}")
#
#         for r in current.get_register():
#             st.write(r)