import PyPDF2
import re
import os
import sys
from pathlib import Path

# =============================================================================
# CONFIGURAÇÃO DE IDIOMAS
# =============================================================================

TEXTS = {
    "portugues": {
        "title": "🦾 EXTRAIDOR DE INFORMAÇÕES DE PDF",
        "select_language": "Selecione o idioma / Select language / Выберите язык:",
        "folder_prompt": "📁 Digite o caminho da pasta com os arquivos PDF:",
        "folder_not_found": "❌ Pasta não encontrada! Tente novamente.",
        "config_keywords": "🔤 CONFIGURAÇÃO DE PALAVRAS-CHAVE",
        "how_many_keywords": "Quantas palavras-chave você quer buscar? ",
        "enter_keyword": "Digite a palavra-chave {}: ",
        "invalid_number": "❌ Por favor, digite um número válido!",
        "starting_processing": "🚀 INICIANDO PROCESSAMENTO",
        "no_pdfs_found": "❌ Nenhum arquivo PDF encontrado na pasta!",
        "pdfs_found": "📚 Arquivos PDF encontrados: {}",
        "keywords_for_search": "🔍 Palavras-chave para busca: {}",
        "processing_file": "📖 PROCESSANDO: {}",
        "analyzing_pdf": "🔍 Analisando PDF: {}",
        "total_pages": "📄 Total de páginas: {}",
        "keyword_found": "✅ Palavra '{}' encontrada!",
        "keyword_not_found": "❌ Palavra '{}' não encontrada",
        "result_item": "   Resultado {}: {}",
        "error_processing": "❌ Erro ao processar {}: {}",
        "final_summary": "📊 RESUMO FINAL DOS RESULTADOS",
        "file_header": "📁 ARQUIVO: {}",
        "no_keywords_found": "   ❌ Nenhuma palavra-chave encontrada neste arquivo",
        "processing_complete": "✅ PROCESSAMENTO CONCLUÍDO!",
        "run_again": "🔄 Deseja executar novamente? (s/n): ",
        "invalid_response": "❌ Por favor, digite 's' para sim ou 'n' para não",
        "goodbye": "👋 Obrigado por usar o Extrator de PDF! Até mais!",
        "press_enter_exit": "Pressione Enter para sair...",
        "program_interrupted": "👋 Programa interrompido pelo usuário. Até mais!",
        "unexpected_error": "❌ Erro inesperado: {}"
    },
    "english": {
        "title": "🦾 PDF INFORMATION EXTRACTOR",
        "select_language": "Select language / Выберите язык:",
        "folder_prompt": "📁 Enter the folder path with PDF files:",
        "folder_not_found": "❌ Folder not found! Please try again.",
        "config_keywords": "🔤 KEYWORDS CONFIGURATION",
        "how_many_keywords": "How many keywords do you want to search for? ",
        "enter_keyword": "Enter keyword {}: ",
        "invalid_number": "❌ Please enter a valid number!",
        "starting_processing": "🚀 STARTING PROCESSING",
        "no_pdfs_found": "❌ No PDF files found in the folder!",
        "pdfs_found": "📚 PDF files found: {}",
        "keywords_for_search": "🔍 Keywords for search: {}",
        "processing_file": "📖 PROCESSING: {}",
        "analyzing_pdf": "🔍 Analyzing PDF: {}",
        "total_pages": "📄 Total pages: {}",
        "keyword_found": "✅ Keyword '{}' found!",
        "keyword_not_found": "❌ Keyword '{}' not found",
        "result_item": "   Result {}: {}",
        "error_processing": "❌ Error processing {}: {}",
        "final_summary": "📊 FINAL RESULTS SUMMARY",
        "file_header": "📁 FILE: {}",
        "no_keywords_found": "   ❌ No keywords found in this file",
        "processing_complete": "✅ PROCESSING COMPLETED!",
        "run_again": "🔄 Do you want to run again? (y/n): ",
        "invalid_response": "❌ Please enter 'y' for yes or 'n' for no",
        "goodbye": "👋 Thank you for using PDF Extractor! Goodbye!",
        "press_enter_exit": "Press Enter to exit...",
        "program_interrupted": "👋 Program interrupted by user. Goodbye!",
        "unexpected_error": "❌ Unexpected error: {}"
    },
    "russian": {
        "title": "🦾 ИЗВЛЕЧЕНИЕ ИНФОРМАЦИИ ИЗ PDF",
        "select_language": "Выберите язык / Select language:",
        "folder_prompt": "📁 Введите путь к папке с PDF файлами:",
        "folder_not_found": "❌ Папка не найдена! Попробуйте снова.",
        "config_keywords": "🔤 НАСТРОЙКА КЛЮЧЕВЫХ СЛОВ",
        "how_many_keywords": "Сколько ключевых слов вы хотите найти? ",
        "enter_keyword": "Введите ключевое слово {}: ",
        "invalid_number": "❌ Пожалуйста, введите правильное число!",
        "starting_processing": "🚀 НАЧАЛО ОБРАБОТКИ",
        "no_pdfs_found": "❌ В папке не найдено PDF файлов!",
        "pdfs_found": "📚 Найдено PDF файлов: {}",
        "keywords_for_search": "🔍 Ключевые слова для поиска: {}",
        "processing_file": "📖 ОБРАБОТКА: {}",
        "analyzing_pdf": "🔍 Анализ PDF: {}",
        "total_pages": "📄 Всего страниц: {}",
        "keyword_found": "✅ Ключевое слово '{}' найдено!",
        "keyword_not_found": "❌ Ключевое слово '{}' не найдено",
        "result_item": "   Результат {}: {}",
        "error_processing": "❌ Ошибка обработки {}: {}",
        "final_summary": "📊 ИТОГОВЫЙ ОТЧЕТ",
        "file_header": "📁 ФАЙЛ: {}",
        "no_keywords_found": "   ❌ В этом файле не найдено ключевых слов",
        "processing_complete": "✅ ОБРАБОТКА ЗАВЕРШЕНА!",
        "run_again": "🔄 Хотите выполнить снова? (д/н): ",
        "invalid_response": "❌ Пожалуйста, введите 'д' для да или 'н' для нет",
        "goodbye": "👋 Спасибо за использование PDF экстрактора! До свидания!",
        "press_enter_exit": "Нажмите Enter для выхода...",
        "program_interrupted": "👋 Программа прервана пользователем. До свидания!",
        "unexpected_error": "❌ Неожиданная ошибка: {}"
    }
}


# =============================================================================
# FUNÇÕES PRINCIPAIS
# =============================================================================

def selecionar_idioma():
    """Permite ao usuário selecionar o idioma"""
    print("=" * 60)
    print(TEXTS["portugues"]["select_language"])
    print("1 - Português")
    print("2 - English")
    print("3 - Русский (Russian)")
    print("=" * 60)

    while True:
        escolha = input("Digite sua escolha (1-3): ").strip()
        if escolha == "1":
            return "portugues"
        elif escolha == "2":
            return "english"
        elif escolha == "3":
            return "russian"
        else:
            print(
                "❌ Opção inválida! Por favor, escolha 1, 2 ou 3 / Invalid option! Please choose 1, 2 or 3 / Неверный выбор! Пожалуйста, выберите 1, 2 или 3")


def extrair_informacao_pdf(waytothedoc, palavra_chave, lang):
    """Extrai informação específica após uma palavra-chave no PDF"""
    try:
        with open(waytothedoc, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text_complete = ""

            print(f"🔍 {TEXTS[lang]['analyzing_pdf'].format(waytothedoc)}")
            print(f"📄 {TEXTS[lang]['total_pages'].format(len(reader.pages))}")

            for pag in range(len(reader.pages)):
                text_pag = reader.pages[pag].extract_text()
                text_complete += f" {text_pag}"

            # Padrão: palavra_chave seguida de qualquer coisa até quebra de linha ou ponto
            padrao = re.compile(
                f"{re.escape(palavra_chave)}\\s*[:]?\\s*(.+?)(?=\\n|\\.|$|;|,)",
                re.IGNORECASE
            )

            resultados = padrao.findall(text_complete)

            if resultados:
                print(f"✅ {TEXTS[lang]['keyword_found'].format(palavra_chave)}")
                for i, resultado in enumerate(resultados, 1):
                    print(f"   {TEXTS[lang]['result_item'].format(i, resultado.strip())}")
                return resultados
            else:
                print(f"❌ {TEXTS[lang]['keyword_not_found'].format(palavra_chave)}")
                return None

    except Exception as e:
        print(f"❌ {TEXTS[lang]['error_processing'].format(waytothedoc, e)}")
        return None


def selecionar_pasta(lang):
    """Permite ao usuário selecionar uma pasta com arquivos PDF"""
    while True:
        caminho = input(f"\n{TEXTS[lang]['folder_prompt']} ").strip()

        # Remove aspas se o usuário colar o caminho com aspas
        caminho = caminho.strip('"\'')

        if os.path.exists(caminho):
            return caminho
        else:
            print(f"❌ {TEXTS[lang]['folder_not_found']}")


def listar_pdfs_na_pasta(caminho_pasta):
    """Lista todos os arquivos PDF na pasta selecionada"""
    pdfs = []
    for arquivo in os.listdir(caminho_pasta):
        if arquivo.lower().endswith('.pdf'):
            pdfs.append(os.path.join(caminho_pasta, arquivo))

    return pdfs


def obter_palavras_busca(lang):
    """Obtém as palavras-chave do usuário"""
    palavras = []

    print(f"\n{TEXTS[lang]['config_keywords']}")
    print("=" * 40)

    try:
        num_palavras = int(input(TEXTS[lang]['how_many_keywords']))

        for i in range(num_palavras):
            palavra = input(TEXTS[lang]['enter_keyword'].format(i + 1)).strip()
            if palavra:
                palavras.append(palavra)

        return palavras
    except ValueError:
        print(f"❌ {TEXTS[lang]['invalid_number']}")
        return obter_palavras_busca(lang)


def processar_arquivos(pasta, palavras_busca, lang):
    """Processa todos os arquivos PDF na pasta com as palavras-chave"""
    print(f"\n{TEXTS[lang]['starting_processing']}")
    print("=" * 50)

    # Listar arquivos PDF
    arquivos_pdf = listar_pdfs_na_pasta(pasta)

    if not arquivos_pdf:
        print(f"❌ {TEXTS[lang]['no_pdfs_found']}")
        return

    print(f"📚 {TEXTS[lang]['pdfs_found'].format(len(arquivos_pdf))}")
    for arquivo in arquivos_pdf:
        print(f"   📄 {os.path.basename(arquivo)}")

    print(f"\n🔍 {TEXTS[lang]['keywords_for_search'].format(', '.join(palavras_busca))}")

    # Processar cada arquivo
    resultados_totais = {}

    for arquivo_pdf in arquivos_pdf:
        print(f"\n{'=' * 60}")
        print(f"📖 {TEXTS[lang]['processing_file'].format(os.path.basename(arquivo_pdf))}")
        print(f"{'=' * 60}")

        resultados_arquivo = {}

        for palavra in palavras_busca:
            resultado = extrair_informacao_pdf(arquivo_pdf, palavra, lang)
            resultados_arquivo[palavra] = resultado

        resultados_totais[os.path.basename(arquivo_pdf)] = resultados_arquivo

    return resultados_totais


def mostrar_resumo(resultados, lang):
    """Mostra um resumo final dos resultados"""
    print(f"\n{'=' * 70}")
    print(f"📊 {TEXTS[lang]['final_summary']}")
    print(f"{'=' * 70}")

    for arquivo, palavras in resultados.items():
        print(f"\n📁 {TEXTS[lang]['file_header'].format(arquivo)}")
        print("-" * 50)

        encontrou_algo = False
        for palavra, resultados_palavra in palavras.items():
            if resultados_palavra:
                encontrou_algo = True
                print(f"   🔍 '{palavra}':")
                for i, resultado in enumerate(resultados_palavra, 1):
                    print(f"      {i}. {resultado}")

        if not encontrou_algo:
            print(f"   ❌ {TEXTS[lang]['no_keywords_found']}")


def executar_novamente(lang):
    """Pergunta se o usuário quer executar novamente"""
    while True:
        resposta = input(f"\n{TEXTS[lang]['run_again']}").strip().lower()

        if lang == "portugues":
            if resposta in ['s', 'sim']:
                return True
            elif resposta in ['n', 'não', 'nao']:
                return False
        elif lang == "english":
            if resposta in ['y', 'yes']:
                return True
            elif resposta in ['n', 'no']:
                return False
        elif lang == "russian":
            if resposta in ['д', 'да', 'y', 'yes']:
                return True
            elif resposta in ['н', 'нет', 'n', 'no']:
                return False

        print(f"❌ {TEXTS[lang]['invalid_response']}")


def main():
    """Função principal do programa"""
    # Selecionar idioma primeiro
    lang = selecionar_idioma()

    print(f"\n{TEXTS[lang]['title']}")
    print("=" * 50)
    print("Este programa busca palavras-chave em arquivos PDF e extrai" if lang == "portugues" else
          "This program searches for keywords in PDF files and extracts" if lang == "english" else
          "Эта программа ищет ключевые слова в PDF файлах и извлекает")
    print("o conteúdo que vem após essas palavras." if lang == "portugues" else
          "the content that comes after those words." if lang == "english" else
          "содержимое, которое идет после этих слов.")
    print("=" * 50)

    # Configurações do usuário
    pasta = selecionar_pasta(lang)
    palavras_busca = obter_palavras_busca(lang)

    if not palavras_busca:
        print("❌ Nenhuma palavra-chave foi informada!" if lang == "portugues" else
              "❌ No keywords were provided!" if lang == "english" else
              "❌ Не было предоставлено ключевых слов!")
        return

    # Processar arquivos
    resultados = processar_arquivos(pasta, palavras_busca, lang)

    if resultados:
        mostrar_resumo(resultados, lang)

    print(f"\n{'=' * 70}")
    print(f"✅ {TEXTS[lang]['processing_complete']}")
    print("=" * 70)


# =============================================================================
# EXECUÇÃO DO PROGRAMA
# =============================================================================

if __name__ == "__main__":
    try:
        while True:
            main()
            # Manter o mesmo idioma para a próxima execução ou perguntar?
            if not executar_novamente(lang):
                print(f"\n{TEXTS[lang]['goodbye']}")
                break
    except KeyboardInterrupt:
        print(f"\n\n{TEXTS[lang]['program_interrupted']}")
    except Exception as e:
        lang = "portugues"  # Idioma padrão em caso de erro
        print(f"\n❌ {TEXTS[lang]['unexpected_error'].format(e)}")

    # Manter a janela aberta (especialmente para Windows .exe)
    input(f"\n{TEXTS[lang]['press_enter_exit']}")