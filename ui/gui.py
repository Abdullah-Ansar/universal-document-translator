import customtkinter as ctk
from tkinter import filedialog

from services.document_handler import read_document
from config import LANGUAGES
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

        title = ctk.CTkLabel(
            self,
            text="Universal Document Translator",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=20)

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

        source_label = ctk.CTkLabel(
            self,
            text="Source Language"
        )
        source_label.pack(pady=(20, 5))

        self.source_menu = ctk.CTkOptionMenu(
            self,
            values=list(LANGUAGES.keys())
        )
        self.source_menu.pack()

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

        read_button = ctk.CTkButton(
            self,
            text="📖 Read Document",
            command=self.read_file
        )
        read_button.pack(pady=20)

        translate_button = ctk.CTkButton(
            self,
            text="🌐 Translate Document",
            command=self.translate_document,
            fg_color="green"
        )
        translate_button.pack(pady=10)

    def translate_document(self):

        if self.selected_file == "":
            self.file_label.configure(text="Please select a document.")
            return

        print("=" * 60)
        print("Translation Started...")
        print("Source :", self.source_menu.get())
        print("Target :", self.target_menu.get())
        print("=" * 60)

    def select_file(self):

        self.selected_file = filedialog.askopenfilename(
            filetypes=[("Word Documents", "*.docx")]
        )

        if self.selected_file:
            self.file_label.configure(text=self.selected_file)

    def read_file(self):

        if self.selected_file == "":
            self.file_label.configure(text="Please select a document.")
            return

        data = read_document(self.selected_file)

        print("=" * 60)

        for line in data:
            print(line)

        print("=" * 60)

        print("Source :", self.source_menu.get())
        print("Target :", self.target_menu.get())