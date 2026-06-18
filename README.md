# Extrator de Notas Fiscais → Planilha → Cadastro Automático

Automação em Python que **lê PDFs de notas fiscais, extrai os dados, monta uma planilha e preenche um formulário web automaticamente** com Selenium. Um trabalho que feito à mão levaria horas roda em minutos.

> Projeto de portfólio baseado em uma automação que desenvolvi e usei em produção (em um órgão público federal), reconstruído aqui com dados **100% fictícios** para ser público com segurança.

---

## O problema

Cadastrar nota fiscal na mão é lento e propenso a erro: abrir cada PDF, copiar número, data, CNPJ e valor, jogar numa planilha e depois redigitar tudo num sistema web. Em volume, isso consome horas e cansa.

## O que esta ferramenta faz

```
   PDFs das notas  ──►  [1] Extrai os campos  ──►  [2] Monta planilha .xlsx
                                                          │
                                                          ▼
                                          [3] Preenche o formulário web (Selenium)
```

1. **Extração** — lê cada PDF com `pdfplumber` e captura número, data, CNPJ, razão social e valor.
2. **Planilha** — consolida tudo num `.xlsx` formatado com `openpyxl`.
3. **Cadastro** — abre o navegador com `Selenium` e preenche o formulário, uma nota por vez, com tratamento de erro.

## Resultado

No uso real, uma tarefa que levava cerca de **3 horas manuais passou a rodar em ~10 minutos**, sem erro de digitação, e podia ser usada por mais de uma pessoa.

## Stack

- **Python 3.11+**
- `pdfplumber` — leitura de PDF
- `openpyxl` — geração de planilha
- `selenium` — automação do navegador
- `reportlab` — geração dos PDFs fictícios de teste

## Como rodar

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Gerar notas fiscais fictícias para teste
python scripts/gerar_pdfs_exemplo.py 5

# 3. Rodar o pipeline completo
python -m src.main
```

A planilha sai em `data/saida/notas.xlsx`.

## Estrutura

```
extrator-notas-fiscais/
├── src/
│   ├── extrator_pdf.py       # [1] lê PDF e extrai os campos
│   ├── gerador_planilha.py   # [2] monta o .xlsx
│   ├── preenchedor_form.py   # [3] preenche o formulário com Selenium
│   └── main.py               # orquestra o pipeline
├── scripts/
│   └── gerar_pdfs_exemplo.py # gera dados fictícios de teste
├── data/
│   ├── notas_exemplo/        # PDFs de entrada
│   └── saida/                # planilha gerada
├── requirements.txt
└── README.md
```

## Decisões de projeto

- **Dados fictícios:** nenhum dado real é usado. Os PDFs de teste são gerados por script.
- **Modular:** cada etapa (extrair / planilha / formulário) é um módulo isolado e testável.
- **Tolerante a falha:** uma nota com problema não derruba o lote inteiro.

---

_Construído por Lucas. Desenvolvo apoiado por ferramentas de IA como parte do meu fluxo — escrevo, reviso e entendo cada parte do código._
