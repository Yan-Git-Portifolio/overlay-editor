from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess


class Funcs:
    def set_file_path(self, path):
        self.file_path = path

    def open_file(self):
        global path
        path = askopenfilename(filetypes=[('Python Files', '*.py')])
        with open(path, 'r', encoding='utf8') as file:
            code = file.read()
            self.code_text.delete('1.0', 'end')
            self.code_text.insert('1.0', code)
            self.file_path = path

    def save_as(self):
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
        with open(path, 'w', encoding='utf8') as file:
            code = self.code_text.get('1.0', 'end')
            file.write(code)
            self.set_file_path(path)

    def save(self):
        if self.file_path == '':
            path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
        else:
            path = self.file_path
        with open(path, 'w', encoding='utf8') as file:
            code = self.code_text.get('1.0', 'end')
            file.write(code)
            self.set_file_path(path)

    def run(self):
        if self.file_path == '':
            messagebox.showerror("Erro", "Você precisa salvar o arquivo primeiro!")
            return
        tem_interpretador = messagebox.askyesno("Interpretador", "Você está usando um ambiente virtual?")
        if tem_interpretador == True:
            interpretador = askopenfilename()
            command = f'{interpretador} {self.file_path}'
            process = subprocess.Popen(["start", "cmd", "/k", f"{command}"], shell=True)
            process.wait()
            return
        else:
            command = f'python {self.file_path}'
            process = subprocess.Popen(["start", "cmd", "/k", f"{command}"], shell=True)
            process.wait()
            return

    def aplicar_preferencias(self, tema, tamanho, familia):
        atual = f'"theme_name": "{tema}","font_size": {tamanho},"font_family": "{familia}"'
        atual = "{" + atual + "}"
        # atual = json.dumps(atual, indent=4)
        with open('atual.json', 'w') as arquivo:
            arquivo.write(atual)
        messagebox.showinfo("Reinicio", "O programa deve reiniciar para aplicar as configurações")
        self.screen.update()
        self.screen.update_idletasks()
