# === app.py ===
import streamlit as st
from decimal import Decimal, getcontext
from calculadora import calculo_impostopf, calculo_impostopj
from recibo import gerar_recibo_txt, gerar_recibo_pdf

getcontext().prec = 10

st.title("Calculadora de Imposto de Renda 2025")

col1, col2 = st.columns(2)
tipo = col1.selectbox("Tipo de contribuinte:", ["Pessoa Física", "Pessoa Jurídica"])
nome = col2.text_input("Nome completo")
id_fiscal = col1.text_input("CPF" if tipo == "Pessoa Física" else "CNPJ")
r_social = col2.text_input("Razão Social") if tipo == "Pessoa Jurídica" else ""
renda = Decimal(str(st.number_input("Informe a renda (R$):", min_value=0.0, format="%.2f")))

dependentes = 0
gsaude = Decimal("0.00")
if tipo == "Pessoa Física":
    col3, col4 = st.columns(2)
    dependentes = col3.number_input("Dependentes:", min_value=0)
    gsaude = Decimal(str(col4.number_input("Gastos com saúde (R$):", min_value=0.0, format="%.2f")))

if st.button("Calcular Imposto"):
    if tipo == "Pessoa Física":
        imposto = calculo_impostopf(renda, dependentes, gsaude)
    else:
        imposto = calculo_impostopj(renda)

    dados = {
        "nome": nome,
        "id_fiscal": id_fiscal,
        "id_tipo": "CPF" if tipo == "Pessoa Física" else "CNPJ",
        "tipo": tipo,
        "renda": renda,
        "imposto": imposto,
        "dependentes": dependentes,
        "gsaude": gsaude,
        "razao_social": r_social
    }

    if imposto == Decimal("0.00"):
        st.info("Renda isenta de imposto!")
    else:
        st.success(f"Imposto calculado: R$ {imposto:.2f}")

    st.markdown("""
    #### Como o imposto é calculado:
    - Alíquotas e faixas progressivas são aplicadas conforme a renda.
    - Descontos por dependentes: R$ 189,59 por dependente.
    - Gastos com saúde são abatidos integralmente.
    """)

    st.subheader("Recibo Gerado")
    st.code(gerar_recibo_txt(dados))

    pdf_file = gerar_recibo_pdf(dados)
    st.download_button("Baixar Recibo em PDF", data=pdf_file, file_name="recibo.pdf", mime="application/pdf")
