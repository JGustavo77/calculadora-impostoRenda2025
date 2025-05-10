# === calculadora.py ===
from decimal import Decimal

def calculo_impostopf(renda, dependentes=0, gsaude=Decimal("0.00")):
    renda = Decimal(renda)
    if renda <= Decimal("2259.20"):
        return Decimal("0.00")
    elif renda <= Decimal("2826.65"):
        imposto = renda * Decimal("0.075") - Decimal("169.44")
    elif renda <= Decimal("3751.05"):
        imposto = renda * Decimal("0.15") - Decimal("381.44")
    elif renda <= Decimal("4664.68"):
        imposto = renda * Decimal("0.225") - Decimal("662.77")
    else:
        imposto = renda * Decimal("0.275") - Decimal("896.00")

    deducao = Decimal(dependentes) * Decimal("189.59") + gsaude
    return max(imposto - deducao, Decimal("0.00"))

def calculo_impostopj(renda):
    renda = Decimal(renda)
    lucro_presumido = renda * Decimal("0.08")
    imposto = lucro_presumido * Decimal("0.15")
    if lucro_presumido > Decimal("20000"):
        imposto += (lucro_presumido - Decimal("20000")) * Decimal("0.10")
    return imposto