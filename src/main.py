"""
Orquestrador: amarra as três etapas em um pipeline só.

    PDFs  ->  extrair  ->  planilha  ->  preencher formulário

Uso (quando estiver pronto):
    python -m src.main
"""

from pathlib import Path

from src.extrator_pdf import extrair_pasta
from src.gerador_planilha import gerar_planilha
from src.preenchedor_form import preencher_formulario

RAIZ = Path(__file__).resolve().parent.parent
PASTA_PDFS = RAIZ / "data" / "notas_exemplo"
PLANILHA_SAIDA = RAIZ / "data" / "saida" / "notas.xlsx"
URL_FORMULARIO = "https://httpbin.org/forms/post"  # site de teste; trocaremos depois


def main() -> None:
    print("1/3  Extraindo notas dos PDFs...")
    notas = extrair_pasta(PASTA_PDFS)
    print(f"     {len(notas)} nota(s) lida(s).")

    print("2/3  Gerando planilha...")
    caminho = gerar_planilha(notas, PLANILHA_SAIDA)
    print(f"     Planilha salva em {caminho}")

    print("3/3  Preenchendo formulário web...")
    preencher_formulario(notas, URL_FORMULARIO)
    print("Concluído.")


if __name__ == "__main__":
    main()
