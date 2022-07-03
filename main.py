from tkinter import Tk, Text, Menu, messagebox
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess


WIDTH = 700
HEIGHT = 550


class Main:
    def __init__(self):
        self.file_path = ''
        self.screen = Tk()
        self.screen_configurator()
        self.text_configurator()
        self.menu_configurator()
        self.screen.mainloop()

    def screen_configurator(self):
        self.screen.title("Overlay Editor")
        self.screen.geometry(f"{WIDTH}x{HEIGHT}")
        self.screen.iconbitmap("icone.ico")

    def text_configurator(self):
        self.code_text = Text(self.screen)
        self.code_text.pack(fill="both", expand=True)

    def set_file_path(self, path):
        self.file_path = path

    def open_file(self):
        path = askopenfilename(filetypes=[('Python Files', '*.py')])
        with open(path, 'r') as file:
            code = file.read()
            self.code_text.delete('1.0', 'end')
            self.code_text.insert('1.0', code)
            self.file_path = path

    def save_as(self):
        if self.file_path == '':
            path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
        else:
            path = self.file_path
        with open(path, 'w') as file:
            code = self.code_text.get('1.0', 'end')
            file.write(code)
            self.set_file_path(path)

    def run(self):
        if self.file_path == '':
            messagebox.showerror("Erro", "Você precisa salvar o arquivo primeiro!")
            return
        command = f'python {self.file_path}'
        process = subprocess.Popen(["start", "cmd", "/k", f"{command}"], shell=True)
        process.wait()

    def menu_configurator(self):
        self.main_menu = Menu(self.screen)

        self.file_menu_bar = Menu(self.main_menu, tearoff=0)
        self.file_menu_bar.add_command(label="Abrir", command=self.open_file)
        self.file_menu_bar.add_command(label="Salvar como", command=self.save_as)
        self.file_menu_bar.add_command(label="Salvar", command=self.save_as)
        self.file_menu_bar.add_command(label="Sair", command=self.screen.quit)
        self.main_menu.add_cascade(label="Opções", menu=self.file_menu_bar)

        self.run_menu_bar = Menu(self.main_menu, tearoff=0)
        self.run_menu_bar.add_command(label="Executar", command=self.run)
        self.main_menu.add_cascade(label="Execução", menu=self.run_menu_bar)

        self.screen.config(menu=self.main_menu)

if __name__ == "__main__":
    Main()

