from tkinter import Tk, Text, Menu, Toplevel, LabelFrame, Label, Button
from tkinter import ttk
import json
from funcs import Funcs


WIDTH = 700
HEIGHT = 550
with open("config.json", "r") as config:
    configuracoes = json.load(config)
    themes = configuracoes["themes"]
    fonts = configuracoes["fonts"]
    temas_disponiveis = []
    fontes_disponiveis = []
    for tema in themes:
        temas_disponiveis.append(tema)
    for fonte in fonts:
        fontes_disponiveis.append(fonte)

with open("atual.json", "r") as config_atual:
    atual = json.load(config_atual)

tema_atual = themes[atual["theme_name"]]
tamanhos_disponiveis = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]


class Main(Funcs):
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
        self.code_text = Text(self.screen, background=tema_atual["background"], fg=tema_atual["color"],
                              font=f"{atual['font_family']} {atual['font_size']}")
        self.code_text.pack(fill="both", expand=True)



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

        self.configs_menu_bar = Menu(self.main_menu, tearoff=0)
        self.configs_menu_bar.add_command(label="Temas", command=self.preferences_configurator)
        self.main_menu.add_cascade(label="Configurações", menu=self.configs_menu_bar)

        self.screen.config(menu=self.main_menu)

    def preferences_configurator(self):
        preferences_screen = Toplevel(self.screen)
        # Configurações da tela #
        preferences_screen.title("Preferencias")
        preferences_screen.geometry("200x220")
        preferences_screen.resizable(False, False)
        # Label Frame #
        temas_e_fonte = LabelFrame(preferences_screen, text="Tema e fonte")
        temas_e_fonte.pack(fill="both", padx=10)
        # Combobox #
        Label(temas_e_fonte, text="Tema").pack()
        temas = ttk.Combobox(temas_e_fonte, values=temas_disponiveis)
        temas.set(tema_atual["name"])
        temas.pack(pady=5)
        Label(temas_e_fonte, text="Tamanho").pack()
        tamanho = ttk.Combobox(temas_e_fonte, values=tamanhos_disponiveis)
        tamanho.set(atual["font_size"])
        tamanho.pack(pady=5)
        Label(temas_e_fonte, text="Fontes").pack()
        fontes = ttk.Combobox(temas_e_fonte, values=fontes_disponiveis)
        fontes.set(atual["font_family"])
        fontes.pack(pady=5)
        aplicar = Button(preferences_screen, text="Aplicar", bg="#ddd",
                         command=lambda : self.aplicar_preferencias(tema=temas.get(), tamanho=int(tamanho.get()), familia=fontes.get()))
        aplicar.pack(pady=7)


if __name__ == "__main__":
    Main()
