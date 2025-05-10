# 🧮 Calculadora de Imposto de Renda 2025

Uma aplicação interativa em Python com [Streamlit](https://streamlit.io) que calcula o imposto de renda de pessoa física ou jurídica, com base na tabela vigente. Gera recibos em **.txt** e **.pdf**, pronto para salvar ou imprimir.

---

## 🚀 Acesse online

👉 [Clique aqui para acessar o app online](https://YOUR-STREAMLIT-LINK.streamlit.app)

> *Substitua pelo link após o deploy!*

---

## 🧠 Funcionalidades

- 📊 Cálculo automático de IRPF e IRPJ
- 📄 Geração de recibo em PDF (usando `fpdf`)
- 📁 Recibo `.txt` com resumo da declaração
- ✅ Suporte a deduções por dependentes e saúde
- 📎 Compatível com **Streamlit Cloud** (sem uso de `open()`)

---

## 🧰 Tecnologias
Python 3.10+

Streamlit

fpdf

decimal

io.BytesIO

---

## 📸 Demonstração

![Calculadora de Imposto de Renda 2025](https://i.imgur.com/SeuPrint.png)

 ---

## 💻 Como rodar localmente

```bash
git clone https://github.com/SeuUsuario/seu-repo.git
cd seu-repo
pip install -r requirements.txt
streamlit run app.py
