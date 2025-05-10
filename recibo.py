# === recibo.py ===
from fpdf import FPDF
from io import BytesIO
from datetime import datetime
from decimal import Decimal

def gerar_recibo_txt(dados):
    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    recibo = f"""
=== RECIBO DE IMPOSTO DE RENDA ===
Data: {data}
Nome: {dados['nome']}
{dados['id_tipo']}: {dados['id_fiscal']}
Tipo: {dados['tipo']}
Renda: R$ {dados['renda']:.2f}
"""
    if dados['tipo'] == "Pessoa Física":
        recibo += f"Dependentes: {dados['dependentes']}\nGastos com Saúde: R$ {dados['gsaude']:.2f}\n"
    else:
        recibo += f"Razão Social: {dados['razao_social']}\n"

    recibo += f"Imposto Devido: R$ {dados['imposto']:.2f}\n"
    return recibo

def gerar_recibo_pdf(dados):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, txt="Recibo de Imposto de Renda", ln=1, align="C")

    pdf.set_font("Arial", size=12)
    for chave, valor in dados.items():
        linha = f"{chave}: {valor}"
        pdf.cell(200, 10, txt=linha, ln=1, align="L")

    # Gera string binária e empacota em BytesIO
    pdf_bytes = pdf.output(dest='S').encode('latin1')
    return BytesIO(pdf_bytes)