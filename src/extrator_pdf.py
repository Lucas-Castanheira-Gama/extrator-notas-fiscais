from pathlib import Path
from dataclasses import dataclass
import re
import pdfplumber

# =====================================================================
# BLOCO 2 — A DATACLASS NotaFiscal
# =====================================================================
@dataclass
class NotaFiscal:
    numero: str
    data_emissao: str
    cnpj_emitente: str
    razao_social: str
    valor_total: float
    arquivo_origem: str

# =====================================================================
# BLOCO 3 — LER O PDF  ->  TEXTO 
# =====================================================================
def ler_texto(caminho_pdf):
    with pdfplumber.open(caminho_pdf) as pdf:
        texto = ""
        for pagina in pdf.pages:
            texto_pagina = (pagina.extract_text() or "") + "\n"
            texto += texto_pagina
    return texto
# =====================================================================
# BLOCO 4 — EXTRAIR OS CAMPOS COM REGEX  
# =====================================================================
def buscar(padrao, texto):
    achado = re.search(padrao, texto, re.IGNORECASE)
    return achado.group(1)
# =====================================================================
# BLOCO 5 — CONVERTER O VALOR (BR -> float)  
# =====================================================================
def valor_para_float(texto_valor):
    valor_float = float(texto_valor.replace(".", "").replace(",", "."))
    return valor_float
# =====================================================================
# BLOCO 6 — JUNTAR TUDO  
# =====================================================================
def extrair_nota(caminho_pdf):
    texto = ler_texto(caminho_pdf)
    return NotaFiscal(
        numero=buscar(r"numero\s*da\s*nf:\s*(\d+)", texto),
        data_emissao=buscar(r"data\s*de\s*emissao:\s*(\d{2}/\d{2}/\d{4})", texto),
        cnpj_emitente=buscar(r"cnpj\s*emitente:\s*([\d./-]+)", texto),
        razao_social=buscar(r"razao\s*social:\s*(.+)", texto),
        valor_total=valor_para_float(buscar(r"valor\s*total:\s*r\$\s*([\d.,]+)", texto)),
        arquivo_origem=Path(caminho_pdf).name
    )

def extrair_pasta(pasta):
    notas = []
    for pdf in sorted(Path(pasta).glob("*.pdf")):
        try:
            notas.append(extrair_nota(pdf))
        except Exception as erro:
            print(f"    [aviso] falha em {pdf.name}: {erro}")
    
    return notas

if __name__ == "__main__":
    for nota in extrair_pasta("data/notas_exemplo"):
        print(nota)