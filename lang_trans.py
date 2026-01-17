import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")

        self.translator = Translator()

        self.src_lang_label = ttk.Label(root, text="Source Language:")
        self.src_lang_label.grid(column=0, row=0, padx=10, pady=10)

        self.src_lang_combo = ttk.Combobox(root, values=list(LANGUAGES.values()))
        self.src_lang_combo.grid(column=1, row=0, padx=10, pady=10)
        self.src_lang_combo.set('english')  

        self.tgt_lang_label = ttk.Label(root, text="Target Language:")
        self.tgt_lang_label.grid(column=0, row=1, padx=10, pady=10)

        self.tgt_lang_combo = ttk.Combobox(root, values=list(LANGUAGES.values()))
        self.tgt_lang_combo.grid(column=1, row=1, padx=10, pady=10)
        self.tgt_lang_combo.set('spanish') 

        self.input_label = ttk.Label(root, text="Input Text:")
        self.input_label.grid(column=0, row=2, padx=10, pady=10)

        self.input_text = tk.Text(root, height=10, width=40)
        self.input_text.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

        self.translate_button = ttk.Button(root, text="Translate", command=self.translate_text)
        self.translate_button.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

        self.output_label = ttk.Label(root, text="Translated Text:")
        self.output_label.grid(column=0, row=5, padx=10, pady=10)

        self.output_text = tk.Text(root, height=10, width=40)
        self.output_text.grid(column=0, row=6, columnspan=2, padx=10, pady=10)

    def translate_text(self):
        src_lang = self.get_lang_code(self.src_lang_combo.get())
        tgt_lang = self.get_lang_code(self.tgt_lang_combo.get())
        text = self.input_text.get("1.0", tk.END).strip()

        if text:
            translation = self.translator.translate(text, src=src_lang, dest=tgt_lang)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, translation.text)

    def get_lang_code(self, lang):
        for code, language in LANGUAGES.items():
            if language == lang:
                return code
        return 'en' 

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
