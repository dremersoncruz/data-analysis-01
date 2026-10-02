# ==========================================
# FRONTEND
# ==========================================

import streamlit as st
import matplotlib.pyplot as plt

st.title("Análise Estatística de Dados")

st.write("Envie um arquivo contendo os dados para análise.")

# Orientações para o usuário

st.info("""
📄 Orientações para a formatação correta do arquivo de dados

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

        linha = linha.strip()

        if linha != "":
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

    Desvpadp100 = 100*Desvpadp/MAS


    # ==========================================
    # CÁLCULO DA MEDIANA
    # ==========================================

    dados_ordenados = sorted(dados)

    if N % 2 == 0:

        Mediana = (
            dados_ordenados[N//2 - 1]
            + dados_ordenados[N//2]
        ) / 2

    else:

        Mediana = dados_ordenados[N//2]


    # ==========================================
    # CÁLCULO DA MODA
    # ==========================================

    maior_frequencia = 0

    for x in dados:

        frequencia = dados.count(x)

        if frequencia > maior_frequencia:
            maior_frequencia = frequencia


    Modas = []

    for x in dados:

        if dados.count(x) == maior_frequencia:

            if x not in Modas:
                Modas.append(x)


    # ==========================================
    # RESULTADOS
    # ==========================================

    st.subheader("Resultados")

    st.write(f"Número de dados = {N}")
    st.write(f"Média Aritmética Simples = {MAS:.2f}")
    st.write(f"Mediana = {Mediana:.2f}")
    st.write(f"Moda = {Modas}")
    st.write(f"Variância = {Variancia:.2f}")
    st.write(f"Desvio padrão populacional = {Desvpadp:.2f}")
    st.write(
        f"Desvio padrão populacional percentual = {Desvpadp100:.2f}%"
    )


    # ==========================================
    # HISTOGRAMA
    # ==========================================

    st.subheader("Distribuição de frequências")

    fig, ax = plt.subplots()

    ax.hist(
        dados,
        bins="auto",
        rwidth=0.9
    )

    ax.set_xlabel("Valor")
    ax.set_ylabel("Frequência")
    ax.set_title("Distribuição de frequências")

    st.pyplot(fig)
