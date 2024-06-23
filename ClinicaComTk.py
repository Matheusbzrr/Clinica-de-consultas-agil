import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import re


cadastro_arquivo = "cadastros.txt"
consultas_arquivo = "consultas.txt"

class MenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu Principal")
        
        self.create_widgets()

    def create_widgets(self):
        # Botão para abrir a janela de cadastro
        self.cadastro_btn = tk.Button(self.root, text="Cadastrar Paciente", command=self.open_cadastro)
        self.cadastro_btn.pack(pady=20)

        # Botão para marcar a consulta
        self.marcar_btn = tk.Button(self.root, text="Marcar consulta", command=self.open_marcarConsulta)
        self.marcar_btn.pack(pady=20)

        # Botão para cancelar consulta
        self.cancelarConsulta_btn = tk.Button(self.root, text="Cancelar consulta", command=self.open_cancelarConsulta)
        self.cancelarConsulta_btn.pack(pady=20)

        # Botão para sair do programa
        self.fechar_btn = tk.Button(self.root, text="Fechar", command=self.root.quit)
        self.fechar_btn.pack(pady=20) 

    def open_cadastro(self):
        CadastroPaciente(self.root)

    def open_marcarConsulta (self):
        MarcarConsulta(self.root)

    def open_cancelarConsulta(self):
        CancelarConsulta(self.root)
    
    def open_visualizarClientes(self):
        VisualizarClientes(self.root)

class CadastroPaciente:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Cadastro de Paciente")

        self.create_widgets()

    def create_widgets(self):
        # Cria e posiciona os rótulos e campos de entrada
        self.nome_label = tk.Label(self.window, text="Nome")
        self.nome_label.grid(row=0, column=0)
        self.nome_entry = tk.Entry(self.window)
        self.nome_entry.grid(row=0, column=1)

        self.telefone_label = tk.Label(self.window, text="Telefone")
        self.telefone_label.grid(row=1, column=0)
        self.telefone_entry = tk.Entry(self.window)
        self.telefone_entry.grid(row=1, column=1)

        # Cria e posiciona o botão para cadastrar o paciente
        self.cadastrar_btn = tk.Button(self.window, text="Cadastrar Paciente", command=self.cadastrar_paciente)
        self.cadastrar_btn.grid(row=2, column=0, columnspan=2)
        
        # Botão de Voltar
        self.voltar_btn = tk.Button(self.window, text="Voltar", command=self.window.destroy)
        self.voltar_btn.grid(row=3, column=0, columnspan=2, pady=10)

       
    def cadastrar_paciente(self):
        nome = self.nome_entry.get()
        telefone = self.telefone_entry.get()
        if self.validar_nome(nome) and self.validar_telefone(telefone):
            if self.verificar_cadastro_existente(telefone):
                messagebox.showerror("Erro", "Paciente já cadastrado!")
            else:
                with open(cadastro_arquivo, "a") as file:
                    file.write(f"{nome},{telefone}\n")
                messagebox.showinfo("Sucesso", f"Paciente {nome} cadastrado com sucesso!")
                self.nome_entry.delete(0, tk.END)
                self.telefone_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos corretamente")

    def validar_nome(self, nome):
        return bool(re.match(r'^[a-zA-Z ]+$', nome))

    def validar_telefone(self, telefone):
        return bool(re.match(r'^[\d()+-]+$', telefone))

    def verificar_cadastro_existente(self, telefone):
        try:
            with open(cadastro_arquivo, "r") as file:
                for line in file:
                    _, tel = line.strip().split(",")
                    if tel == telefone:
                        return True
        except FileNotFoundError:
            return False
        return False


class MarcarConsulta:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.title("Marcar consulta")

        self.create_widgets()
        
    def create_widgets(self):
        self.telefone_label = tk.Label(self.window, text="Telefone")
        self.telefone_label.grid(row=0, column=0)
        self.telefone_entry = tk.Entry(self.window)
        self.telefone_entry.grid(row=0, column=1)

        self.data_label = tk.Label(self.window, text="Data (DD/MM/AAAA)")
        self.data_label.grid(row=1, column=0)
        self.data_entry = tk.Entry(self.window)
        self.data_entry.grid(row=1, column=1)

        self.hora_label = tk.Label(self.window, text="Horário (HH:MM)")
        self.hora_label.grid(row=2, column=0)
        self.hora_entry = tk.Entry(self.window)
        self.hora_entry.grid(row=2, column=1)

        self.especialidade_label = tk.Label(self.window, text="Especialidade")
        self.especialidade_label.grid(row=3, column=0)
        self.especialidade_entry = tk.Entry(self.window)
        self.especialidade_entry.grid(row=3, column=1)

        
        self.marcar_btn = tk.Button(self.window, text="Marcar Consulta", command=self.verificar_cadastro_e_marcar)
        self.marcar_btn.grid(row=4, column=0, columnspan=2)
        
        
        self.voltar_btn = tk.Button(self.window, text="Voltar", command=self.window.destroy)
        self.voltar_btn.grid(row=5, column=0, columnspan=2, pady=10)

    def verificar_cadastro_e_marcar(self):
        telefone = self.telefone_entry.get()
        if not self.verificar_cadastro_existente(telefone):
            messagebox.showerror("Erro", "Paciente não cadastrado! Por favor, cadastre o paciente primeiro.")
            return

        self.marcar_consulta()

    def marcar_consulta(self):
        telefone = self.telefone_entry.get()
        data = self.data_entry.get()
        hora = self.hora_entry.get()
        especialidade = self.especialidade_entry.get()
        if telefone and data and hora and especialidade:
            if self.validar_data_hora(data, hora):
                nome_paciente = self.obter_nome_paciente(telefone)
                with open(consultas_arquivo, "a") as file:
                    file.write(f"{telefone},{data},{hora},{especialidade}\n")
                messagebox.showinfo("Sucesso!", f"Consulta marcada com sucesso para o paciente {nome_paciente}!")
                self.telefone_entry.delete(0, tk.END)
                self.data_entry.delete(0, tk.END)
                self.hora_entry.delete(0, tk.END)
                self.especialidade_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Erro", "Data ou horário inválido")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos")

    def verificar_cadastro_existente(self, telefone):
        try:
            with open(cadastro_arquivo, "r") as file:
                for line in file:
                    _, tel = line.strip().split(",")
                    if tel == telefone:
                        return True
        except FileNotFoundError:
            return False
        return False

    def obter_nome_paciente(self, telefone):
        try:
            with open(cadastro_arquivo, "r") as file:
                for line in file:
                    nome, tel = line.strip().split(",")
                    if tel == telefone:
                        return nome
        except FileNotFoundError:
            pass
        return "Desconhecido"  

    def validar_data_hora(self, data, hora):
        try:
            data_hora = datetime.strptime(f"{data} {hora}", "%d/%m/%Y %H:%M")
            if data_hora < datetime.now():
                return False
        except ValueError:
            return False
        return True


class CancelarConsulta:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.title("Cancelar consulta")

        self.create_widgets()

    def create_widgets(self):
        self.telefone_label = tk.Label(self.window, text="Telefone")
        self.telefone_label.grid(row=0, column=0)
        self.telefone_entry = tk.Entry(self.window)
        self.telefone_entry.grid(row=0, column=1)

        self.buscar_btn = tk.Button(self.window, text="Buscar Consulta", command=self.buscar_consulta)
        self.buscar_btn.grid(row=1, column=0, columnspan=2)

        self.result_label = tk.Label(self.window, text="", justify=tk.LEFT)
        self.result_label.grid(row=2, column=0, columnspan=2)
        
        self.voltar_btn = tk.Button(self.window, text="Voltar", command=self.window.destroy)
        self.voltar_btn.grid(row=3, column=0, columnspan=2, pady=10)

    def buscar_consulta(self):
        telefone = self.telefone_entry.get()
        if telefone:
            consultas = self.obter_consultas(telefone)
            if consultas:
                nome_paciente = self.obter_nome_paciente(telefone)
                consulta_info = "\n".join([f"Data: {c[1]}, Hora: {c[2]}, Especialidade: {c[3]}" for c in consultas])
                self.result_label.config(text=f"Paciente: {nome_paciente}\nConsultas encontradas:\n{consulta_info}")
               
                self.cancelar_btn = tk.Button(self.window, text="Cancelar Consulta", command=lambda: self.cancelar_consulta(telefone))
                self.cancelar_btn.grid(row=3, column=0, columnspan=2)
            else:
                self.result_label.config(text="Nenhuma consulta encontrada para este telefone.")
        else:
            messagebox.showerror("Erro", "Por favor, preencha o campo de telefone.")

    def obter_nome_paciente(self, telefone):
        try:
            with open(cadastro_arquivo, "r") as file:
                for line in file:
                    nome, tel = line.strip().split(",")
                    if tel == telefone:
                        return nome
        except FileNotFoundError:
            pass
        return "Desconhecido"  

    def obter_consultas(self, telefone):
        consultas = []
        try:
            with open(consultas_arquivo, "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if parts[0] == telefone:
                        consultas.append(parts)
        except FileNotFoundError:
            pass
        return consultas

    def cancelar_consulta(self, telefone):
        consultas = []
        try:
            with open(consultas_arquivo, "r") as file:
                lines = file.readlines()
            with open(consultas_arquivo, "w") as file:
                for line in lines:
                    parts = line.strip().split(",")
                    if parts[0] == telefone:
                        continue  
                    file.write(line)
            messagebox.showinfo("Sucesso", f"Consulta(s) cancelada(s) para o paciente {self.obter_nome_paciente(telefone)}.")
            self.result_label.config(text="")
            self.cancelar_btn.grid_forget()  
        except FileNotFoundError:
            pass

class VisualizarClientes:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Visualizar Clientes")

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.window, text="Clientes Cadastrados e Consultas Marcadas")
        self.title_label.pack(pady=10)

        self.clientes_text = tk.Text(self.window, height=20, width=60)
        self.clientes_text.pack(padx=20, pady=10)

        
        self.voltar_btn = tk.Button(self.window, text="Voltar", command=self.window.destroy)
        self.voltar_btn.pack(pady=10)

        self.exibir_clientes()

    def exibir_clientes(self):
        try:
            with open(cadastro_arquivo, "r") as file:
                for line in file:
                    nome, telefone = line.strip().split(",")
                    consultas = self.obter_consultas(telefone)
                    if consultas:
                        consulta_info = "\n".join([f"  - Data: {c[1]}, Hora: {c[2]}, Especialidade: {c[3]}" for c in consultas])
                        self.clientes_text.insert(tk.END, f"Nome: {nome}, Telefone: {telefone}\nConsultas marcadas:\n{consulta_info}\n\n")
                    else:
                        self.clientes_text.insert(tk.END, f"Nome: {nome}, Telefone: {telefone}\nNenhuma consulta marcada.\n\n")
        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo de cadastros não encontrado.")

    def obter_consultas(self, telefone):
        consultas = []
        try:
            with open(consultas_arquivo, "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if parts[0] == telefone:
                        consultas.append(parts)
        except FileNotFoundError:
            pass
        return consultas


root = tk.Tk()


app = MenuApp(root)


root.mainloop()
