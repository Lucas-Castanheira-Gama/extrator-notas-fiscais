"""
Etapa 3 do pipeline: usar Selenium para preencher um formulário web com os dados
de cada nota. (No projeto original era o sistema interno; aqui usamos um site de
teste público, ex.: https://httpbin.org/forms/post ou um HTML local de demonstração.)

>>> Vamos preencher este módulo JUNTOS por último, é a parte mais visual. <<<
"""

from src.extrator_pdf import NotaFiscal


def preencher_formulario(notas: list[NotaFiscal], url: str, headless: bool = True) -> None:
    """
    Abre o navegador, vai até `url` e preenche o formulário uma vez por nota.

    TODO (juntos):
      1. Configurar o webdriver (Chrome/Firefox), opção headless.
      2. Para cada nota: navegar, localizar campos por name/id, preencher, enviar.
      3. Tratar esperas (WebDriverWait) e erros sem derrubar o lote inteiro.
      4. Logar sucesso/falha de cada nota.
    """
    raise NotImplementedError("Vamos escrever isto juntos.")
