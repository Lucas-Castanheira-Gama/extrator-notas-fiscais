"""
Gera notas fiscais FICTÍCIAS em PDF para servir de dado de teste.

Todos os dados (CNPJ, razão social, valores) são gerados aleatoriamente e
não correspondem a empresas ou notas reais. Serve só para o bot ter o que ler.

Uso:
    python scripts/gerar_pdfs_exemplo.py            # gera 5 notas
    python scripts/gerar_pdfs_exemplo.py 12         # gera 12 notas
"""

import random
import sys
from datetime import date, timedelta
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas

PASTA_SAIDA = Path(__file__).resolve().parent.parent / "data" / "notas_exemplo"

EMPRESAS = [
    "Comercial Aurora Ltda",
    "Tech Nordeste Solucoes ME",
    "Distribuidora Vale Verde SA",
    "Papelaria Horizonte Ltda",
    "Servicos Integrados Atlas ME",
    "Mercado Bom Preco Eireli",
]


def cnpj_aleatorio() -> str:
    n = [random.randint(0, 9) for _ in range(8)]
    return f"{n[0]}{n[1]}.{n[2]}{n[3]}{n[4]}.{n[5]}{n[6]}{n[7]}/0001-{random.randint(10, 99)}"


def gerar_uma_nota(numero: int, caminho: Path) -> None:
    """Desenha uma nota fiscal fictícia simples em um PDF de uma página."""
    emissao = date.today() - timedelta(days=random.randint(0, 120))
    valor = round(random.uniform(150, 9800), 2)

    c = canvas.Canvas(str(caminho), pagesize=A4)
    largura, altura = A4
    y = altura - 3 * cm

    c.setFont("Helvetica-Bold", 16)
    c.drawString(2 * cm, y, "NOTA FISCAL ELETRONICA")
    y -= 1.2 * cm

    c.setFont("Helvetica", 11)
    linhas = [
        f"Numero da NF: {numero:06d}",
        f"Data de emissao: {emissao.strftime('%d/%m/%Y')}",
        f"CNPJ emitente: {cnpj_aleatorio()}",
        f"Razao social: {random.choice(EMPRESAS)}",
        f"Valor total: R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
    ]
    for linha in linhas:
        c.drawString(2 * cm, y, linha)
        y -= 0.8 * cm

    c.setFont("Helvetica-Oblique", 8)
    c.drawString(2 * cm, 2 * cm, "Documento ficticio gerado para testes de automacao.")
    c.showPage()
    c.save()


def main() -> None:
    quantidade = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    PASTA_SAIDA.mkdir(parents=True, exist_ok=True)

    for i in range(1, quantidade + 1):
        numero = random.randint(1000, 99999)
        caminho = PASTA_SAIDA / f"nota_{i:02d}.pdf"
        gerar_uma_nota(numero, caminho)
        print(f"Gerado: {caminho.name}  (NF {numero:06d})")

    print(f"\n{quantidade} nota(s) ficticia(s) em: {PASTA_SAIDA}")


if __name__ == "__main__":
    main()
