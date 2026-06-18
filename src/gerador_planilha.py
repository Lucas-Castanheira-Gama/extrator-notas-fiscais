from openpyxl import Workbook
from pathlib import Path

def gerar_planilha(notas, caminho_saida):
    # BLOCO 2: crie o workbook, pegue a planilha ativa, escreva o cabeçalho
    wb = Workbook()
    ws = wb.active
    ws.title = "Notas"
    ws.append(["Número", "Data", "CNPJ", "Razão Social", "Valor", "Arquivo"])
    # BLOCO 3: percorra as notas e escreva uma linha pra cada
    for nota in notas:
      ws.append([
        nota.numero,
        nota.data_emissao,
        nota.cnpj_emitente,
        nota.razao_social,
        nota.valor_total,
        nota.arquivo_origem
      ])
    # BLOCO 4: salve e devolva o caminho
    Path(caminho_saida).parent.mkdir(parents=True, exist_ok=True)
    wb.save(caminho_saida)
    return caminho_saida
  
if __name__ == "__main__":
    from extrator_pdf import extrair_pasta
    notas = extrair_pasta("data/notas_exemplo")
    caminho = gerar_planilha(notas, "data/saida/notas.xlsx")
    print("Planilha gerada em:", caminho)
