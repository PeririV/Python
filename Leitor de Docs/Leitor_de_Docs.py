import PyPDF2
import re
import os
from pathlib import Path


def extrair_informacao_pdf(waytothedoc, palavra_chave):
    """
    Extrai informação específica após uma palavra-chave no PDF
    """
    try:
        with open(waytothedoc, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text_complete = ""

            print(f"🔍 Analisando PDF: {waytothedoc}")
            print(f"📄 Total de páginas: {len(reader.pages)}")

            for pag in range(len(reader.pages)):
                text_pag = reader.pages[pag].extract_text()
                text_complete += f" {text_pag}"  # Espaço para evitar junção de palavras

            # Padrão: palavra_chave seguida de qualquer coisa até quebra de linha ou ponto
            padrao = re.compile(
                f"{re.escape(palavra_chave)}\\s*[:]?\\s*(.+?)(?=\\n|\\.|$|;|,)",
                re.IGNORECASE
            )

            resultados = padrao.findall(text_complete)

            if resultados:
                print(f"✅ Palavra '{palavra_chave}' encontrada!")
                for i, resultado in enumerate(resultados, 1):
                    print(f"   Resultado {i}: {resultado.strip()}")
                return resultados
            else:
                print(f"❌ Palavra '{palavra_chave}' não encontrada")
                return None

    except Exception as e:
        print(f"❌ Erro ao processar {waytothedoc}: {e}")
        return None


def selecionar_pasta():
    """
    Permite ao usuário selecionar uma pasta com arquivos PDF
    """
    while True:
        caminho = input("\n📁 Digite o caminho da pasta com os arquivos PDF: ").strip()

        # Remove aspas se o usuário colar o caminho com aspas
        caminho = caminho.strip('"\'')

        if os.path.exists(caminho):
            return caminho
        else:
            print("❌ Pasta não encontrada! Tente novamente.")


def listar_pdfs_na_pasta(caminho_pasta):
    """
    Lista todos os arquivos PDF na pasta selecionada
    """
    pdfs = []
    for arquivo in os.listdir(caminho_pasta):
        if arquivo.lower().endswith('.pdf'):
            pdfs.append(os.path.join(caminho_pasta, arquivo))

    return pdfs


def obter_palavras_busca():
    """
    Obtém as palavras-chave do usuário
    """
    palavras = []

    print("\n🔤 CONFIGURAÇÃO DE PALAVRAS-CHAVE")
    print("=" * 40)

    try:
        num_palavras = int(input("Quantas palavras-chave você quer buscar? "))

        for i in range(num_palavras):
            palavra = input(f"Digite a palavra-chave {i + 1}: ").strip()
            if palavra:
                palavras.append(palavra)

        return palavras
    except ValueError:
        print("❌ Por favor, digite um número válido!")
        return obter_palavras_busca()


def processar_arquivos(pasta, palavras_busca):
    """
    Processa todos os arquivos PDF na pasta com as palavras-chave
    """
    print(f"\n🚀 INICIANDO PROCESSAMENTO")
    print("=" * 50)

    # Listar arquivos PDF
    arquivos_pdf = listar_pdfs_na_pasta(pasta)

    if not arquivos_pdf:
        print("❌ Nenhum arquivo PDF encontrado na pasta!")
        return

    print(f"📚 Arquivos PDF encontrados: {len(arquivos_pdf)}")
    for arquivo in arquivos_pdf:
        print(f"   📄 {os.path.basename(arquivo)}")

    print(f"\n🔍 Palavras-chave para busca: {', '.join(palavras_busca)}")

    # Processar cada arquivo
    resultados_totais = {}

    for arquivo_pdf in arquivos_pdf:
        print(f"\n{'=' * 60}")
        print(f"📖 PROCESSANDO: {os.path.basename(arquivo_pdf)}")
        print(f"{'=' * 60}")

        resultados_arquivo = {}

        for palavra in palavras_busca:
            resultado = extrair_informacao_pdf(arquivo_pdf, palavra)
            resultados_arquivo[palavra] = resultado

        resultados_totais[os.path.basename(arquivo_pdf)] = resultados_arquivo

    return resultados_totais


def mostrar_resumo(resultados):
    """
    Mostra um resumo final dos resultados
    """
    print(f"\n{'=' * 70}")
    print("📊 RESUMO FINAL DOS RESULTADOS")
    print(f"{'=' * 70}")

    for arquivo, palavras in resultados.items():
        print(f"\n📁 ARQUIVO: {arquivo}")
        print("-" * 50)

        encontrou_algo = False
        for palavra, resultados_palavra in palavras.items():
            if resultados_palavra:
                encontrou_algo = True
                print(f"   🔍 '{palavra}':")
                for i, resultado in enumerate(resultados_palavra, 1):
                    print(f"      {i}. {resultado}")

        if not encontrou_algo:
            print("   ❌ Nenhuma palavra-chave encontrada neste arquivo")


def main():
    """
    Função principal do programa
    """
    print("🦾 EXTRAIDOR DE INFORMAÇÕES DE PDF")
    print("=" * 50)
    print("Este programa busca palavras-chave em arquivos PDF e extrai")
    print("o conteúdo que vem após essas palavras.")
    print("=" * 50)

    # Configurações do usuário
    pasta = selecionar_pasta()
    palavras_busca = obter_palavras_busca()

    if not palavras_busca:
        print("❌ Nenhuma palavra-chave foi informada!")
        return

    # Processar arquivos
    resultados = processar_arquivos(pasta, palavras_busca)

    if resultados:
        mostrar_resumo(resultados)

    print(f"\n{'=' * 70}")
    print("✅ PROCESSAMENTO CONCLUÍDO!")
    print("=" * 70)


def executar_novamente():
    """
    Pergunta se o usuário quer executar novamente
    """
    while True:
        resposta = input("\n🔄 Deseja executar novamente? (s/n): ").strip().lower()
        if resposta in ['s', 'sim', 'y', 'yes']:
            return True
        elif resposta in ['n', 'não', 'nao', 'no']:
            return False
        else:
            print("❌ Por favor, digite 's' para sim ou 'n' para não")


if __name__ == "__main__":
    try:
        while True:
            main()
            if not executar_novamente():
                print("\n👋 Obrigado por usar o Extrator de PDF! Até mais!")
                break
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrompido pelo usuário. Até mais!")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")

    # Manter a janela aberta (especialmente para Windows .exe)
    input("\nPressione Enter para sair...")