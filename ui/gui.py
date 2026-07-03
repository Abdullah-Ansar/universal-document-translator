import os
import customtkinter as ctk
from tkinter import filedialog

from config import LANGUAGES
from services.document_handler import DocumentHandler
from services.translator import TranslatorService


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class UniversalTranslatorApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Universal Document Translator")
        self.geometry("900x650")

        self.selected_file = ""

        self.build_ui()

    def build_ui(self):

        # ==========================
        # Title
        # ==========================
        title = ctk.CTkLabel(
            self,
            text="Universal Document Translator",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=20)

        # ==========================
        # Select File
        # ==========================
        select_button = ctk.CTkButton(
            self,
            text="📄 Select Word File",
            command=self.select_file,
            width=250,
            height=40
        )
        select_button.pack(pady=15)

        self.file_label = ctk.CTkLabel(
            self,
            text="No file selected",
            wraplength=700
        )
        self.file_label.pack()

        # ==========================
        # Source Language
        # ==========================
        source_label = ctk.CTkLabel(
            self,
            text="Source Language"
        )
        source_label.pack(pady=(20, 5))

        self.source_menu = ctk.CTkOptionMenu(
            self,
            values=list(LANGUAGES.keys())
        )
        self.source_menu.set("Kruti Dev Hindi")
        self.source_menu.pack()

        # ==========================
        # Target Language
        # ==========================
        target_label = ctk.CTkLabel(
            self,
            text="Target Language"
        )
        target_label.pack(pady=(20, 5))

        self.target_menu = ctk.CTkOptionMenu(
            self,
            values=list(LANGUAGES.keys())
        )
        self.target_menu.set("Assamese")
        self.target_menu.pack()

        # ==========================
        # Read Button
        # ==========================
        read_button = ctk.CTkButton(
            self,
            text="📖 Read Document",
            command=self.read_file
        )
        read_button.pack(pady=20)

        # ==========================
        # Translate Button
        # ==========================
        translate_button = ctk.CTkButton(
            self,
            text="🌐 Translate Document",
            command=self.translate_document,
            fg_color="green"
        )
        translate_button.pack(pady=10)

    # ==========================
    # Select File
    # ==========================
    def select_file(self):

        self.selected_file = filedialog.askopenfilename(
            filetypes=[("Word Documents", "*.docx")]
        )

        if self.selected_file:
            self.file_label.configure(text=self.selected_file)

    # ==========================
    # Read Document
    # ==========================
    def read_file(self):

        if self.selected_file == "":
            self.file_label.configure(text="Please select a document.")
            return

        handler = DocumentHandler(self.selected_file)

        print("=" * 60)

        for paragraph in handler.get_paragraphs():

            if paragraph.text.strip():
                print(paragraph.text)

        print("=" * 60)
        print("Source :", self.source_menu.get())
        print("Target :", self.target_menu.get())

    # ==========================
    # Translate Document
    # ==========================
    def translate_document(self):

        if self.selected_file == "":
            self.file_label.configure(text="Please select a document.")
            return

        source = LANGUAGES[self.source_menu.get()]
        target = LANGUAGES[self.target_menu.get()]

        handler = DocumentHandler(self.selected_file)
        translator = TranslatorService()

        document = handler.get_document()

        # Translate all paragraphs
        for paragraph in document.paragraphs:

            if paragraph.text.strip():

                try:
                    translated_text = translator.translate(
                        paragraph.text,
                        source,
                        target
                    )

                    paragraph.text = translated_text

                except Exception as e:
                    print("Translation Error:", e)

        # Save translated document
        os.makedirs("output", exist_ok=True)

        filename = os.path.basename(self.selected_file)

        output_path = os.path.join(
            "output",
            f"translated_{filename}"
        )

        handler.save(output_path)

        print("=" * 60)
        print("Translation Completed")
        print("Saved to:", output_path)
        print("=" * 60)

        self.file_label.configure(
            text=f"✅ Translation Completed\n\n{output_path}"
        )