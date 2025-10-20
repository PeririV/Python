import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import PyPDF2
import re
import os
import threading
from pathlib import Path

# =============================================================================
# CONFIGURAÇÃO DE IDIOMAS
# =============================================================================

TEXTS = {
    "portugues": {
        "title": "🦾 Extrator de Informações de PDF",
        "select_folder": "Selecionar Pasta com PDFs",
        "folder_selected": "Pasta selecionada:",
        "keywords_label": "Palavras-chave para busca:",
        "add_keyword": "Adicionar Palavra",
        "remove_keyword": "Remover Selecionada",
        "process_button": "🔍 Processar PDFs",
        "clear_button": "🧹 Limpar Resultados",
        "results_title": "📊 Resultados da Busca",
        "processing": "Processando...",
        "completed": "Processamento concluído!",
        "no_folder": "Por favor, selecione uma pasta primeiro!",
        "no_keywords": "Por favor, adicione pelo menos uma palavra-chave!",
        "no_pdfs": "Nenhum arquivo PDF encontrado na pasta!",
        "keywords_list": "Lista de Palavras-chave:",
        "file": "Arquivo",
        "keyword": "Palavra-chave",
        "result": "Resultado",
        "status": "Status",
        "found": "Encontrado",
        "not_found": "Não encontrado",
        "error": "Erro"
    },
    "english": {
        "title": "🦾 PDF Information Extractor",
        "select_folder": "Select Folder with PDFs",
        "folder_selected": "Folder selected:",
        "keywords_label": "Keywords to search:",
        "add_keyword": "Add Keyword",
        "remove_keyword": "Remove Selected",
        "process_button": "🔍 Process PDFs",
        "clear_button": "🧹 Clear Results",
        "results_title": "📊 Search Results",
        "processing": "Processing...",
        "completed": "Processing completed!",
        "no_folder": "Please select a folder first!",
        "no_keywords": "Please add at least one keyword!",
        "no_pdfs": "No PDF files found in folder!",
        "keywords_list": "Keywords List:",
        "file": "File",
        "keyword": "Keyword",
        "result": "Result",
        "status": "Status",
        "found": "Found",
        "not_found": "Not found",
        "error": "Error"
    },
    "russian": {
        "title": "🦾 Извлечение информации из PDF",
        "select_folder": "Выбрать папку с PDF",
        "folder_selected": "Выбранная папка:",
        "keywords_label": "Ключевые слова для поиска:",
        "add_keyword": "Добавить слово",
        "remove_keyword": "Удалить выбранное",
        "process_button": "🔍 Обработать PDF",
        "clear_button": "🧹 Очистить результаты",
        "results_title": "📊 Результаты поиска",
        "processing": "Обработка...",
        "completed": "Обработка завершена!",
        "no_folder": "Пожалуйста, сначала выберите папку!",
        "no_keywords": "Пожалуйста, добавьте хотя бы одно ключевое слово!",
        "no_pdfs": "В папке не найдено PDF файлов!",
        "keywords_list": "Список ключевых слов:",
        "file": "Файл",
        "keyword": "Ключевое слово",
        "result": "Результат",
        "status": "Статус",
        "found": "Найдено",
        "not_found": "Не найдено",
        "error": "Ошибка"
    }
}


class PDFExtractorGUI:
    def __init__(self, root):
        self.root = root
        self.lang = "portugues"
        self.setup_ui()

    def setup_ui(self):
        # Configurar janela principal
        self.root.title(TEXTS[self.lang]["title"])
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f0f0')

        # Frame de configuração de idioma
        lang_frame = ttk.Frame(self.root)
        lang_frame.pack(pady=10, padx=20, fill='x')

        ttk.Label(lang_frame, text="Idioma / Language / Язык:").pack(side='left')

        self.lang_var = tk.StringVar(value=self.lang)
        lang_combo = ttk.Combobox(lang_frame, textvariable=self.lang_var,
                                  values=["portugues", "english", "russian"],
                                  state="readonly", width=15)
        lang_combo.pack(side='left', padx=10)
        lang_combo.bind('<<ComboboxSelected>>', self.change_language)

        # Frame de seleção de pasta
        folder_frame = ttk.LabelFrame(self.root, text=TEXTS[self.lang]["select_folder"])
        folder_frame.pack(pady=10, padx=20, fill='x')

        self.folder_path = tk.StringVar()
        ttk.Entry(folder_frame, textvariable=self.folder_path, state='readonly').pack(side='left', fill='x',
                                                                                      expand=True, padx=5)
        ttk.Button(folder_frame, text="📁 Procurar", command=self.select_folder).pack(side='right', padx=5)

        # Frame de palavras-chave
        keywords_frame = ttk.LabelFrame(self.root, text=TEXTS[self.lang]["keywords_label"])
        keywords_frame.pack(pady=10, padx=20, fill='x')

        # Entrada para nova palavra-chave
        input_frame = ttk.Frame(keywords_frame)
        input_frame.pack(fill='x', pady=5)

        self.new_keyword = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.new_keyword).pack(side='left', fill='x', expand=True, padx=5)
        ttk.Button(input_frame, text=TEXTS[self.lang]["add_keyword"],
                   command=self.add_keyword).pack(side='right', padx=5)

        # Lista de palavras-chave
        list_frame = ttk.Frame(keywords_frame)
        list_frame.pack(fill='both', expand=True, pady=5)

        ttk.Label(list_frame, text=TEXTS[self.lang]["keywords_list"]).pack(anchor='w')

        self.keywords_listbox = tk.Listbox(list_frame, height=6)
        self.keywords_listbox.pack(fill='both', expand=True, pady=5)

        # Botões de controle da lista
        button_frame = ttk.Frame(keywords_frame)
        button_frame.pack(fill='x', pady=5)

        ttk.Button(button_frame, text=TEXTS[self.lang]["remove_keyword"],
                   command=self.remove_keyword).pack(side='right', padx=5)

        # Frame de controle
        control_frame = ttk.Frame(self.root)
        control_frame.pack(pady=10, padx=20, fill='x')

        self.process_btn = ttk.Button(control_frame, text=TEXTS[self.lang]["process_button"],
                                      command=self.start_processing, state='disabled')
        self.process_btn.pack(side='left', padx=5)

        ttk.Button(control_frame, text=TEXTS[self.lang]["clear_button"],
                   command=self.clear_results).pack(side='left', padx=5)

        # Barra de progresso
        self.progress = ttk.Progressbar(self.root, mode='indeterminate')
        self.progress.pack(pady=5, padx=20, fill='x')

        # Frame de resultados
        results_frame = ttk.LabelFrame(self.root, text=TEXTS[self.lang]["results_title"])
        results_frame.pack(pady=10, padx=20, fill='both', expand=True)

        # Treeview para resultados
        columns = ('file', 'keyword', 'result', 'status')
        self.results_tree = ttk.Treeview(results_frame, columns=columns, show='headings', height=15)

        # Definir cabeçalhos
        self.update_treeview_headers()

        # Scrollbars
        v_scroll = ttk.Scrollbar(results_frame, orient='vertical', command=self.results_tree.yview)
        h_scroll = ttk.Scrollbar(results_frame, orient='horizontal', command=self.results_tree.xview)
        self.results_tree.configure(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)

        # Empacotar treeview e scrollbars
        self.results_tree.pack(side='left', fill='both', expand=True)
        v_scroll.pack(side='right', fill='y')
        h_scroll.pack(side='bottom', fill='x')

        # Área de log detalhado
        log_frame = ttk.LabelFrame(self.root, text="Log Detalhado")
        log_frame.pack(pady=10, padx=20, fill='both', expand=True)

        self.log_text = scrolledtext.ScrolledText(log_frame, height=10, wrap=tk.WORD)
        self.log_text.pack(fill='both', expand=True, padx=5, pady=5)

        # Status bar
        self.status_var = tk.StringVar(value="Pronto")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief='sunken')
        status_bar.pack(side='bottom', fill='x')

    def change_language(self, event=None):
        self.lang = self.lang_var.get()
        self.root.title(TEXTS[self.lang]["title"])
        self.update_ui_texts()

    def update_ui_texts(self):
        # Atualizar todos os textos da interface
        for widget in self.root.winfo_children():
            if isinstance(widget, ttk.LabelFrame):
                if "select_folder" in widget.cget('text'):
                    widget.configure(text=TEXTS[self.lang]["select_folder"])
                elif "keywords_label" in widget.cget('text'):
                    widget.configure(text=TEXTS[self.lang]["keywords_label"])
                elif "results_title" in widget.cget('text'):
                    widget.configure(text=TEXTS[self.lang]["results_title"])

        self.update_treeview_headers()

    def update_treeview_headers(self):
        self.results_tree.heading('file', text=TEXTS[self.lang]["file"])
        self.results_tree.heading('keyword', text=TEXTS[self.lang]["keyword"])
        self.results_tree.heading('result', text=TEXTS[self.lang]["result"])
        self.results_tree.heading('status', text=TEXTS[self.lang]["status"])

        self.results_tree.column('file', width=200)
        self.results_tree.column('keyword', width=150)
        self.results_tree.column('result', width=400)
        self.results_tree.column('status', width=100)

    def select_folder(self):
        folder = filedialog.askdirectory(title=TEXTS[self.lang]["select_folder"])
        if folder:
            self.folder_path.set(folder)
            self.check_ready_state()

    def add_keyword(self):
        keyword = self.new_keyword.get().strip()
        if keyword and keyword not in self.keywords_listbox.get(0, tk.END):
            self.keywords_listbox.insert(tk.END, keyword)
            self.new_keyword.set("")
            self.check_ready_state()

    def remove_keyword(self):
        selection = self.keywords_listbox.curselection()
        if selection:
            self.keywords_listbox.delete(selection[0])
            self.check_ready_state()

    def check_ready_state(self):
        has_folder = bool(self.folder_path.get())
        has_keywords = self.keywords_listbox.size() > 0

        if has_folder and has_keywords:
            self.process_btn.config(state='normal')
        else:
            self.process_btn.config(state='disabled')

    def clear_results(self):
        for item in self.results_tree.get_children():
            self.results_tree.delete(item)
        self.log_text.delete(1.0, tk.END)
        self.status_var.set("Pronto")

    def start_processing(self):
        self.clear_results()
        self.progress.start()
        self.process_btn.config(state='disabled')
        self.status_var.set(TEXTS[self.lang]["processing"])

        # Executar em thread separada para não travar a interface
        thread = threading.Thread(target=self.process_pdfs)
        thread.daemon = True
        thread.start()

    def process_pdfs(self):
        try:
            folder = self.folder_path.get()
            keywords = list(self.keywords_listbox.get(0, tk.END))

            pdf_files = [f for f in os.listdir(folder) if f.lower().endswith('.pdf')]

            if not pdf_files:
                self.show_message(TEXTS[self.lang]["no_pdfs"])
                return

            self.log_message(f"Encontrados {len(pdf_files)} arquivos PDF")
            self.log_message(f"Palavras-chave: {', '.join(keywords)}")

            for pdf_file in pdf_files:
                full_path = os.path.join(folder, pdf_file)
                self.process_single_pdf(pdf_file, full_path, keywords)

            self.root.after(0, self.processing_completed)

        except Exception as e:
            self.root.after(0, lambda: self.show_error(f"Erro durante o processamento: {str(e)}"))

    def process_single_pdf(self, filename, full_path, keywords):
        try:
            self.log_message(f"\nProcessando: {filename}")

            with open(full_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text_complete = ""

                for page in reader.pages:
                    text_complete += page.extract_text() or ""

                for keyword in keywords:
                    result = self.search_keyword(text_complete, keyword)
                    status = TEXTS[self.lang]["found"] if result else TEXTS[self.lang]["not_found"]

                    # Adicionar à treeview
                    self.root.after(0, self.add_to_treeview,
                                    (filename, keyword, result or "-", status))

        except Exception as e:
            error_msg = f"Erro ao processar {filename}: {str(e)}"
            self.log_message(f"❌ {error_msg}")
            self.root.after(0, self.add_to_treeview,
                            (filename, "-", "-", TEXTS[self.lang]["error"]))

    def search_keyword(self, text, keyword):
        try:
            pattern = re.compile(f"{re.escape(keyword)}\\s*[:]?\\s*(.+?)(?=\\n|\\.|$|;|,)", re.IGNORECASE)
            results = pattern.findall(text)

            if results:
                return "; ".join([result.strip() for result in results])
            return None

        except Exception as e:
            return f"Erro na busca: {str(e)}"

    def add_to_treeview(self, data):
        self.results_tree.insert('', 'end', values=data)

    def log_message(self, message):
        self.root.after(0, self._log_message, message)

    def _log_message(self, message):
        self.log_text.insert(tk.END, message + '\n')
        self.log_text.see(tk.END)

    def processing_completed(self):
        self.progress.stop()
        self.process_btn.config(state='normal')
        self.status_var.set(TEXTS[self.lang]["completed"])
        self.log_message("\n✅ Processamento concluído!")

    def show_message(self, message):
        self.root.after(0, lambda: messagebox.showinfo("Info", message))

    def show_error(self, message):
        self.root.after(0, lambda: messagebox.showerror("Erro", message))


# =============================================================================
# EXECUÇÃO DO PROGRAMA
# =============================================================================

def main():
    try:
        root = tk.Tk()
        app = PDFExtractorGUI(root)
        root.mainloop()
    except Exception as e:
        print(f"Erro ao iniciar aplicação: {e}")
        input("Pressione Enter para sair...")


if __name__ == "__main__":
    main()