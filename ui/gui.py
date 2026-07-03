import customtkinter as ctk
from tkinter import filedialog

from config import LANGUAGES
from services.document_handler import DocumentHandler

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

        # =========================
        # Title
        # =========================
        title = ctk.CTkLabel(
            self,
            text="Universal Document Translator",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=20)

        # =========================
        # Select File Button
        # =========================
        select_button = ctk.CTkButton(
            self,
            text="📄 Select Word File",
            command=self.select_file,
            width=250,
            height=40
        )
        select_button.pack(pady=15)

        # =========================
        # Selected File Label
        # =========================
        self.file_label = ctk.CTkLabel(
            self,
            text="No file selected",
            wraplength=700
        )
        self.file_label.pack()

        # =========================
        # Source Language
        # =========================
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

        # =========================
        # Target Language
        # =========================
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

        # =========================
        # Read Button
        # =========================
        read_button = ctk.CTkButton(
            self,
            text="📖 Read Document",
            command=self.read_file
        )
        read_button.pack(pady=20)

        # =========================
        # Translate Button
        # =========================
        translate_button = ctk.CTkButton(
            self,
            text="🌐 Translate Document",
            command=self.translate_document,
            fg_color="green"
        )
        translate_button.pack(pady=10)

    # =====================================
    # Select File
    # =====================================
    def select_file(self):

        self.selected_file = filedialog.askopenfilename(
            filetypes=[("Word Documents", "*.docx")]
        )

        if self.selected_file:
            self.file_label.configure(text=self.selected_file)

    # =====================================
    # Read Document
    # =====================================
    def read_file(self):

        if self.selected_file == "":
            self.file_label.configure(text="Please select a document.")
            return

        handler = DocumentHandler(self.selected_file)

        paragraphs = handler.get_paragraphs()

        print("=" * 60)

        for paragraph in paragraphs:
            if paragraph.text.strip():
                print(paragraph.text)

        print("=" * 60)

        print("Source :", self.source_menu.get())
        print("Target :", self.target_menu.get())

    # =====================================
    # Translate Document
    # =====================================
    def translate_document(self):

        if self.selected_file == "":
            self.file_label.configure(text="Please select a document.")
            return

        print("=" * 60)
        print("Translation Started...")
        print("File    :", self.selected_file)
        print("Source  :", self.source_menu.get())
        print("Target  :", self.target_menu.get())
        print("=" * 60)