
# ==========================================
# FRONTEND
# ==========================================

import streamlit as st
import matplotlib.pyplot as plt

st.title("Análise Estatística de Dados")

st.write("Envie um arquivo contendo os dados para análise.")

# Orientações para o usuário

st.info("""
📄 Orientações para o arquivo de dados

\\>>> Utilize um arquivo no formato `.txt`.  
\\>>> Insira apenas valores numéricos.  
\\>>> Coloque um único valor em cada linha.  
\\>>> Não utilize títulos, nomes de variáveis ou outros textos.  
\\>>> Linhas vazias serão ignoradas.

Exemplo:

    7
    5
    10
""")

arquivo = st.file_uploader(
    "Selecione o arquivo de dados",
    type=["txt"]
)


# ==========================================
# LEITURA DOS DADOS
# ==========================================

if arquivo is not None:

    conteudo = arquivo.getvalue().decode("utf-8")
    linhas = conteudo.splitlines()

    dados = []

    for linha in linhas:
        dados.append(float(linha))


    # ==========================================
    # CÁLCULO DA MÉDIA
    # ==========================================

    N = len(dados)

    S = sum(dados)

    MAS = S/N


    # ==========================================
    # CÁLCULO DA VARIÂNCIA
    # ==========================================

    soma = 0

    for x in dados:
        soma = soma + (x-MAS)**2

    Variancia = soma/N


    # ==========================================
    # CÁLCULO DO DESVIO PADRÃO
    # ==========================================

    Desvpadp = Variancia**0.5


    # ==========================================
    # CÁLCULO DA MEDIANA
    # ==========================================

    dados_ordenados = sorted(dados)

    if N % 2 == 0:
        Mediana = (dados_ordenados[N//2 - 1] +
                   dados_ordenados[N//2]) / 2

    else:
        Mediana = dados_ordenados[N//2]


    # ==========================================
    # CÁLCULO DA MODA
    # ==========================================

    maior_frequencia = 0
    Moda = 0

    for nota in range(11):

        frequencia = dados.count(nota)

        if frequencia > maior_frequencia:
            maior_frequencia = frequencia
            Moda = nota


    # ==========================================
    # RESULTADOS
    # ==========================================

    st.subheader("Resultados")

    st.write(f"Número de dados = {N}")
    st.write(f"Média Aritmética Simples = {MAS:.2f}")
    st.write(f"Mediana = {Mediana:.2f}")
    st.write(f"Moda = {Moda}")
    st.write(f"Variância = {Variancia:.2f}")
    st.write(f"Desvio padrão populacional = {Desvpadp:.2f}")


    # ==========================================
    # HISTOGRAMA
    # ==========================================

    st.subheader("Histograma")

    fig, ax = plt.subplots()

    ax.hist(
        dados,
        bins=[
            -0.5, 0.5, 1.5, 2.5, 3.5,
            4.5, 5.5, 6.5, 7.5, 8.5,
            9.5, 10.5
        ],
        rwidth=0.8
    )

    ax.set_xlabel("Nota")
    ax.set_ylabel("Frequência")
    ax.set_xticks(range(11))
    ax.set_title("Distribuição das notas")

    st.pyplot(fig)
