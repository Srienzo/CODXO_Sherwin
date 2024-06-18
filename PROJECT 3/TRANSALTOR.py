import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from googletrans import Translator, LANGUAGES

class LanguageTranslator:
    def __init__(self, root):
        self.root = root
        self.root.title("TRANSLATOR @Sherwin @CODXO")
        self.root.geometry("600x500")

        self.translator = Translator()

        # Load the background image
        self.background_image = Image.open("background.jpg")
        self.background_image = self.background_image.resize((600, 500), Image.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Create a Canvas widget to display the background image
        self.canvas = tk.Canvas(self.root, width=600, height=500)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

        # Create Widgets
        self.create_widgets()

    def create_widgets(self):
        # Source Language
        self.source_lang_label = tk.Label(self.root, text="Source Language:", bg='#ffffff', fg='#333333')
        self.source_lang_label.place(x=50, y=20)

        self.source_lang = ttk.Combobox(self.root, values=list(LANGUAGES.values()), state='readonly')
        self.source_lang.place(x=180, y=20)
        self.source_lang.set('english')  # Default source language

        # Target Language
        self.target_lang_label = tk.Label(self.root, text="Target Language:", bg='#ffffff', fg='#333333')
        self.target_lang_label.place(x=50, y=60)

        self.target_lang = ttk.Combobox(self.root, values=list(LANGUAGES.values()), state='readonly')
        self.target_lang.place(x=180, y=60)
        self.target_lang.set('spanish')  # Default target language

        # Input Text
        self.input_text_label = tk.Label(self.root, text="Enter Text:", bg='#ffffff', fg='#333333')
        self.input_text_label.place(x=50, y=100)

        self.input_text = tk.Text(self.root, height=5, width=40, bg='#ffffff', fg='#333333', bd=1, relief='solid')
        self.input_text.place(x=180, y=100)

        # Translate Button
        self.translate_button = tk.Button(self.root, text="Translate", command=self.translate_text, bg='#4CAF50', fg='#ffffff', bd=0, padx=10, pady=5)
        self.translate_button.place(x=250, y=220)

        # Output Text
        self.output_text_label = tk.Label(self.root, text="Translated Text:", bg='#ffffff', fg='#333333')
        self.output_text_label.place(x=50, y=270)

        self.output_text = tk.Text(self.root, height=5, width=40, state='disabled', bg='#e0e0e0', fg='#333333', bd=1, relief='solid')
        self.output_text.place(x=180, y=270)

        # Clear Button
        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_text, bg='#f44336', fg='#ffffff', bd=0, padx=10, pady=5)
        self.clear_button.place(x=250, y=390)

        # Rights Reserved Label
        self.rights_label = tk.Label(self.root, text="ALL RIGHTS RESERVED BY @Sherwin @CODXO", bg=self.canvas['bg'], fg='#333333')
        self.rights_label.place(x=180, y=440)

    def translate_text(self):
        source_lang = self.get_language_code(self.source_lang.get())
        target_lang = self.get_language_code(self.target_lang.get())
        text = self.input_text.get("1.0", tk.END)

        try:
            translation = self.translator.translate(text, src=source_lang, dest=target_lang)
            self.output_text.config(state='normal')
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, translation.text)
            self.output_text.config(state='disabled')
        except Exception as e:
            messagebox.showerror("Translation Error", str(e))

    def clear_text(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.config(state='normal')
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state='disabled')

    @staticmethod
    def get_language_code(language_name):
        for code, name in LANGUAGES.items():
            if name.lower() == language_name.lower():
                return code
        return 'en'  # Default to English if not found

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageTranslator(root)
    root.mainloop()
