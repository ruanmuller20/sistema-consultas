import sqlite3
from customtkinter import *
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import ttk



# Criando conexão com banco de dados
connection = sqlite3.connect('novo_banco.db')
cursor = connection.cursor()

# Criação da tabela sql
cursor.execute('''CREATE TABLE IF NOT EXISTS patients
                (
                nome TEXT,
                cpf TEXT PRIMARY KEY,
                telefone TEXT,
                nascimento TEXT,
                especialidade TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS consulta
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                medico TEXT,
                data TEXT,
                horario TEXT,
                cpf TEXT,
                FOREIGN KEY(cpf) REFERENCES patients(cpf))''')

connection.commit()





# Função para inserir informações no BD
def inserir_informacao(nome, cpf, telefone, nascimento, especialidade):
    cursor.execute('''INSERT INTO patients (nome, cpf, telefone, nascimento, especialidade)
                    VALUES (?, ?, ?, ?, ?)''', (nome, cpf, telefone, nascimento, especialidade))
    connection.commit()

def inserir_consulta(medico, data, horario, cpf):
            cursor.execute('''INSERT INTO consulta (medico, data, horario, cpf) 
                           VALUES (?, ?, ?, ?)''',(medico, data, horario, cpf))
            connection.commit()
   





def validar_cpf(cpf):
            return len(cpf) == 14 and cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-'

def validar_data(nascimento):
            try:
                datetime.strptime(nascimento, '%d/%m/%Y')
                return True
            except ValueError:
                return False
def validar_telefone(telefone):
            return len(telefone) == 14 and telefone[0] == '(' and telefone[3] == ')' and telefone[9] == '-'


def fechar_conexao():
     connection.close()
     
  
        
        

def salvar_info_e_fechar_janela(nome, cpf, telefone, nascimento, especialidade):
    if validar_cpf(cpf) and validar_data(nascimento) and validar_telefone(telefone):
            try:
                # Verificar se o CPF já está cadastrado
                cursor.execute("SELECT * FROM patients WHERE cpf = ?", (cpf,))
                resultado = cursor.fetchone()

                if resultado:
                    messagebox.showinfo('Mensagem de Aviso', 'CPF já cadastrado. Por favor, insira um CPF diferente.')
                else:
                    # Inserir dados no banco de dados
                    inserir_informacao(nome, cpf, telefone, nascimento, especialidade)
                    messagebox.showinfo('Cadastro finalizado', 'Cadastro criado com sucesso!')
                    fechar_janela_2_abrir_janela_3()
            except sqlite3.Error as e:
                messagebox.showerror('Erro', f'Erro ao salvar informações: {e}')
    else:
            messagebox.showinfo('Mensagem de Erro', 'Dados inválidos. Por favor, insira o CPF no formato xxx.xxx.xxx-xx, a data no formato DD/MM/YYYY e o telefone no formato (xx) xxxxx-xxxx.')
   

def fechar_janela_6_abrir_janela_2():
    janela_6.destroy() 
    informacoes_paciente()
    
def fechar_janela_6_abrir_janela_3():
    janela_6.destroy() 
    marcar_consulta()

def fechar_janela_6_abrir_janela_4():
    janela_6.destroy()
    excluir_consulta() 

def fechar_janela_2_abrir_janela_3():
    janela_2.destroy()
    marcar_consulta()
    
def  fechar_janela_6_abrir_janela_5():
    janela_6.destroy()
    excluir_cadastro()

def fechar_janela_5_abrir_janela_6():
    janela_5.destroy()
    janela_principal()
   

def fechar_janela_1_abrir_janela_6():
    janela_1.destroy()
    janela_principal()
    
def fechar_janela_3_abrir_janela_6():
    janela_3.destroy()
    janela_principal()
    
def fechar_janela_6_abrir_janela_7():
    janela_6.destroy()
    exibir_consulta()
    
def fechar_janela_2_abrir_janela_6():
    janela_2.destroy()
    janela_principal()

def fechar_janela_7_abrir_janela_6():
    janela_7.destroy()
    janela_principal()
    
    




def informacoes_paciente():
    global janela_2
    janela_2 = CTk() 
    set_appearance_mode("dark")
    set_default_color_theme("dark-blue")
    janela_2.title("PitMed: Gestão Clínica")
    janela_2.geometry("600x400")
    janela_2.resizable(False, False)
    
    titulo = CTkLabel(janela_2, text="Preencha suas informações:", font=CTkFont(family="Arial", size=15, weight="bold"))
    titulo.place(x=210, y=35)
    
        
    frame_principal = CTkFrame(janela_2, width=580, height=380)
    frame_principal.place(x=90, y=90)
    
    nome_descricao = CTkLabel(frame_principal, text="Digite o seu nome completo:", font=CTkFont(size=12))
    nome_descricao.grid(column=0, row=0, padx=10, pady=10)

    nome_entrada = CTkEntry(frame_principal, placeholder_text='Apenas Letras', width=200, font=CTkFont(size=12), justify="center") 
    nome_entrada.grid(column=1, row=0, padx=10, pady=10)

    cpf_descricao = CTkLabel(frame_principal, text="Digite o seu CPF:", font=CTkFont(size=12))
    cpf_descricao.grid(column=0, row=1, padx=10, pady=10)

    cpf_entrada = CTkEntry(frame_principal, placeholder_text='Insira no formato xxx.xxx.xxx-xx)', width=210, font=CTkFont(size=12), justify="center")  
    cpf_entrada.grid(column=1, row=1, padx=10, pady=10)

    telefone_descricao = CTkLabel(frame_principal, text="Digite o seu telefone com DDD:", font=CTkFont(size=12))
    telefone_descricao.grid(column=0, row=2, padx=10, pady=10)

    telefone_entrada = CTkEntry(frame_principal, placeholder_text='Digite no formato (xx)xxxxx-xxxx', width=200, font=CTkFont(size=12), justify="center")
    telefone_entrada.grid(column=1, row=2, padx=10, pady=10)

    nascimento_descricao = CTkLabel(frame_principal, text="Digite sua data de nascimento:", font=CTkFont(size=12))
    nascimento_descricao.grid(column=0, row=3, padx=10, pady=10)

    nascimento_entrada = CTkEntry(frame_principal, placeholder_text='Digite no formato DD/MM/AAAA', width=205, font=CTkFont(size=12), justify="center")
    nascimento_entrada.grid(column=1, row=3, padx=10, pady=10)
    
    especialidade_descricao = CTkLabel(frame_principal, text="Selecione sua especialidade:", font=CTkFont(size=12))
    especialidade_descricao.grid(column=0, row=4, padx=10, pady=10)
    
    especialidade_escolha = CTkComboBox(frame_principal, values=['(Selecione)', 'Cardiologia', 'Pediatria', 'Fisiatra'], font=CTkFont(size=12))
    especialidade_escolha.grid(column=1, row=4, padx=10, pady=10)
    
    
    
    
    confirmacao = CTkButton(frame_principal, text="Confirmar", command=lambda: salvar_info_e_fechar_janela(nome_entrada.get(), cpf_entrada.get(), telefone_entrada.get(), nascimento_entrada.get(), especialidade_escolha.get()), image=CTkImage(imagem_botao), font=CTkFont(size=12))  
    confirmacao.grid(column=1, row=5, padx=10, pady=10)
    
    voltar_2 = CTkButton(frame_principal,command= fechar_janela_2_abrir_janela_6, text="Voltar",image=CTkImage(imagem_botao), font=CTkFont(size=12))
    voltar_2.grid(column=0, row=5, padx=10, pady=10)
    
    janela_2.mainloop()
    

  

    
    

def marcar_consulta():
    global janela_3
    janela_3 = CTk() # Abertura da Janela 
   
    set_appearance_mode("dark")
    set_default_color_theme("dark-blue")
    janela_3.title("PitMed: Gestão Clínica")
    janela_3.geometry("600x400")
    janela_3.resizable(False, False)
    
    titulo_marcacao = CTkLabel(janela_3, text="Bem-vindo a marcação de consultas!", font=CTkFont(family="Arial", size=15, weight="bold"))
    titulo_marcacao.place(x=180, y=35)

    
    frame_principal3 = CTkFrame(janela_3, width=580, height=380)
    frame_principal3.place(x=90, y=90)
    
    
    medico_descricao = CTkLabel(frame_principal3, text="Selecione o médico:", font=CTkFont(size=12))
    medico_descricao.grid(column=0, row=1, padx=10, pady=10)
    
    medico_escolha = CTkComboBox(frame_principal3, values=['(Selecione)','Dr. João', 'Dra. Maria', 'Dr. Pedro', 'Dra. Ana'], font=CTkFont(size=12))
    medico_escolha.grid(column=1, row=1, padx=10, pady=10)
    
    data_descricao = CTkLabel(frame_principal3, text="Selecione a data:", font=CTkFont(size=12))
    data_descricao.grid(column=0, row=2, padx=10, pady=10)
    
    data_entrada = CTkEntry(frame_principal3, placeholder_text='DD/MM/AAAA', width=200, font=CTkFont(size=12), justify="center")
    data_entrada.grid(column=1, row=2, padx=10, pady=10)
    
    horario_descricao = CTkLabel(frame_principal3, text="Selecione o horário:", font=CTkFont(size=12))
    horario_descricao.grid(column=0, row=3, padx=10, pady=10)
    
    horario_escolha = CTkComboBox(frame_principal3, values=['(Selecione)','09:00', '14:00', '18:00'], font=CTkFont(size=12))
    horario_escolha.grid(column=1, row=3, padx=10, pady=10)
    
    cpf_consulta_descricao = CTkLabel(frame_principal3, text="Insira o CPF para Marcação da consulta :", font=CTkFont(size=12))
    cpf_consulta_descricao.grid(column=0, row=4, padx=10, pady=10)

    cpf_consulta_entrada = CTkEntry(frame_principal3, placeholder_text='CPF do Paciente (no formato xxx.xxx.xxx-xx)', width=205, font=CTkFont(size=12), justify="center")
    cpf_consulta_entrada.grid(column=1, row=4, padx=10, pady=10)
    
    def salvar_consulta():
        medico = medico_escolha.get()
        data = data_entrada.get()
        horario = horario_escolha.get()
        cpf = cpf_consulta_entrada.get()
        
        def validar_cpf(cpf):
                return len(cpf) == 14 and cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-'
        
        try:
            if validar_cpf(cpf):
                    # Verificar se o CPF existe no banco de dados
                    consulta_verificacao = "SELECT * FROM patients WHERE cpf = ?"
                    cursor.execute(consulta_verificacao, (cpf,))
                    resultado = cursor.fetchone()
            
            if resultado:
                inserir_consulta(medico, data, horario, cpf)
                messagebox.showinfo('Consulta marcada','Sua consulta foi marcada com sucesso!')
                fechar_janela_3_abrir_janela_6()
            else:
                messagebox.showerror('Erro', 'Paciente não encontrado. Verifique o CPF do paciente')
                
        except sqlite3.Error as e:
            messagebox.showerror('Erro', f'Erro ao marcar consulta: {e}')
        finally:
            fechar_conexao()
     
        
    confirmar = CTkButton(frame_principal3, command=salvar_consulta, text="Confirmar",image=CTkImage(imagem_botao), font=CTkFont(size=12))
    confirmar.grid(column=1, row=5, padx=10, pady=10)
    
    voltar = CTkButton(frame_principal3,command= fechar_janela_3_abrir_janela_6, text="Voltar",image=CTkImage(imagem_botao), font=CTkFont(size=12))
    voltar.grid(column=0, row=5, padx=10, pady=10)
    


    
    


  
    janela_3.mainloop() # Fechamento da Janela 
    
def excluir_consulta():
    global janela_4
    janela_4 = CTk() # Abertura da Janela 
    
    titulo_excluir = CTkLabel(janela_4,text="Insira o ID atribuido a consulta:", font=CTkFont(family="Arial", size=15, weight="bold"))
    titulo_excluir.place(x=220, y=35)
    
    titulo_excluir2 = CTkLabel(janela_4,text="*Clique o botão 'Verificar ID' para obter o ID da consulta*", font=CTkFont(family="Arial", size=12, weight="bold"))
    titulo_excluir2.place(x=175, y=65)
    
    set_appearance_mode("dark")
    set_default_color_theme("dark-blue")
    janela_4.title("PitMed: Gestão Clínica")
    janela_4.geometry("700x400")
    janela_4.resizable(False, False)
    
    frame_principal3 = CTkFrame(janela_4, width=580, height=200)
    frame_principal3.place(x=65, y=90)
    
    
    inseririd_descricao = CTkLabel(frame_principal3, text="Insira o ID da consulta que deseja excluir:", font=CTkFont(size=12))
    inseririd_descricao.grid(column=0, row=1, padx=10, pady=10)
    
    inserir_id = CTkEntry(frame_principal3, placeholder_text='Insira o ID',width=210, font=CTkFont(size=12), justify="center")
    inserir_id.grid(column=1, row=1, padx=10, pady=10)
    
    
    
    
    verificarid = CTkButton(frame_principal3, text="Verificar ID", command=lambda:exibir_consulta(), image=CTkImage(imagem_botao), font=CTkFont(size=12))  
    verificarid.grid(row=2, column=0, padx=10, pady=10)
    
    
    
    

    

  
    janela_4.mainloop() # Fechamento da Janela

def excluir_cadastro():
    global janela_5
    janela_5 = CTk() # Abertura da Janela 
    
    titulo_exclusao = CTkLabel(janela_5, text="Preencha as informações a seguir:", font=CTkFont(family="Arial", size=15, weight="bold"))
    titulo_exclusao.place(x=210, y=35)
    
    set_appearance_mode("dark")
    set_default_color_theme("dark-blue")
    janela_5.title("PitMed: Gestão Clínica")
    janela_5.geometry("600x400")
    janela_5.resizable(False, False)
    
    frame_principal2 = CTkFrame(janela_5, width=580, height=380)
    frame_principal2.place(x=90, y=90)
    
    cpf_descricao2 = CTkLabel(frame_principal2, text="Digit o CPF a ser excluído:", font=CTkFont(size=12))
    cpf_descricao2.grid(column=0, row=1, padx=10, pady=10)
    
    cpf_excluir = CTkEntry(frame_principal2, placeholder_text='Insira o CPF (no formato xxx.xxx.xxx-xx)', width=210, font=CTkFont(size=12), justify="center")
    cpf_excluir.grid(column=1, row=1, padx=10, pady=10)


        
    def confirmar_remover_cadastro(cpf):
            cpf = cpf_excluir.get()
                
            def validar_cpf(cpf):
                return len(cpf) == 14 and cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-'
            
            try:
            
                if validar_cpf(cpf):
                    # Verificar se o CPF existe no banco de dados
                    consulta_verificacao = "SELECT * FROM patients WHERE cpf = ?"
                    cursor.execute(consulta_verificacao, (cpf,))
                    resultado = cursor.fetchone()

                    if resultado:
                        # CPF encontrado, realizar a remoção
                        consulta_remocao = "DELETE FROM patients WHERE cpf = ?"
                        cursor.execute(consulta_remocao, (cpf,))
                        connection.commit()
                        messagebox.showinfo('Cadastro Removido', 'Cadastro removido com sucesso!')
                        fechar_janela_5_abrir_janela_6()
                    else:
                        messagebox.showinfo('Mensagem de Aviso', 'CPF não encontrado. Insira um CPF válido.')
            except Exception as ex:
                messagebox.showerror('Erro', f'Erro inesperado: {str(ex)}')
            finally:
                fechar_conexao()

            
            # Fechar a janela de remoção após a operação
            frame_principal2.destroy()
    
    confirmar = CTkButton(frame_principal2, text="Excluir Cadastro", command=lambda: confirmar_remover_cadastro(cpf_excluir.get()), image=CTkImage(imagem_botao), font=CTkFont(size=12))  
    confirmar.grid(row=2, column=0, padx=10, pady=10)
    
    cancelar = CTkButton(frame_principal2, text="Cancelar", command=lambda: fechar_janela_5_abrir_janela_6(), image=CTkImage(imagem_botao), font=CTkFont(size=12))  
    cancelar.grid(row=3, column=0, padx=10, pady=10)
            
    

  
    janela_5.mainloop() # Fechamento da Janela
    
def janela_principal():
 global janela_6
 janela_6 = CTk() # Abertura da Janela 

 set_appearance_mode("dark")
 set_default_color_theme("dark-blue")
 janela_6.title("PitMed: Gestão Clínica") 
 janela_6.geometry("600x400")
 janela_6.resizable(False, False)
 
 imagem_tela = CTkImage(dark_image=Image.open("Logo_clinica.png"), size=(400, 300))

# Adicionando a imagem como fundo
 label_imagem = CTkLabel(janela_6,image=imagem_tela, text="")  # Convertendo para ImageTk
 label_imagem.place(x=250, y=50)
 

 titulo_principal = CTkLabel(janela_6, text="Selecione o que deseja abaixo: ", font=CTkFont(family="Arial", size=15, weight="bold"))
 titulo_principal.place(x=180, y=35)
 
 frame_principal4 = CTkFrame(janela_6, width=580, height=380)
 frame_principal4.place(x=90, y=90)
 
 criar_cadastro = CTkButton(frame_principal4,text="Criar Cadastro", command=fechar_janela_6_abrir_janela_2, width=20, image=CTkImage(imagem_botao), font=CTkFont(size=12)) 
 criar_cadastro.grid(row=1, column=0, padx=10, pady=10)

 agendamento = CTkButton(frame_principal4,text="Marcar Consulta",command=fechar_janela_6_abrir_janela_3, width=20, image=CTkImage(imagem_botao), font=CTkFont(size=12)) 
 agendamento.grid(row=2, column=0, padx=10, pady=10)

 excluir_agendamento = CTkButton(frame_principal4,text="Excluir Agendamento",command=fechar_janela_6_abrir_janela_4, width=20, image=CTkImage(imagem_botao), font=CTkFont(size=12)) 
 excluir_agendamento.grid(row=3, column=0, padx=10, pady=10)

 excluir_paciente = CTkButton(frame_principal4,text="Excluir Cadastro",command=fechar_janela_6_abrir_janela_5, width=20, image=CTkImage(imagem_botao), font=CTkFont(size=12)) 
 excluir_paciente.grid(row=4, column=0, padx=10, pady=10)
 
 mostrar_consulta =  CTkButton(frame_principal4,text="Exibir Consultas",command=exibir_consulta, width=20, image=CTkImage(imagem_botao), font=CTkFont(size=12)) 
 mostrar_consulta.grid(row=4, column=0, padx=10, pady=10)
 
 janela_6.mainloop()
 

 

def exibir_consulta():
  global janela_7 
  janela_7 = CTk()
  
 
  set_appearance_mode("dark")
  set_default_color_theme("dark-blue")
  janela_7.title("PitMed: Gestão Clínica") 
  janela_7.geometry("700x400")
  janela_7.resizable(False, False)
  
  titulo = CTkLabel(janela_7, text="Consultas Agendadas", font=CTkFont(family="Arial", size=15, weight="bold"))
  titulo.place(x=250, y=35)
  
  
  frame_descricao2 = CTkFrame(janela_7, width=220, height=400) 
  frame_descricao2.place(relx=0.5, rely=0.5, anchor="center") 
  
  style = ttk.Style()
  style.configure("Treeview.Heading", font=('Arial', 10, 'bold'))
  
  tree = ttk.Treeview(frame_descricao2, columns=("medico", "data", "horario", "cpf"), show='headings')
  tree.heading("medico",text="Médico", anchor=tk.CENTER)
  tree.heading("data", text="Data", anchor=tk.CENTER)
  tree.heading("horario", text="Horário", anchor=tk.CENTER)
  tree.heading("cpf", text="CPF", anchor=tk.CENTER)
  tree.pack(fill="both", expand=True)
  
  scrollbar = ttk.Scrollbar(frame_descricao2, orient="vertical",command=tree.yview)
  scrollbar.pack(side="right", fill="y")
  tree.configure(yscrollcommand=scrollbar.set)
  
  cursor.execute("SELECT medico, data, horario, cpf FROM consulta")
  consultas = cursor.fetchall()
  for consulta in consultas:
      tree.insert("", "end", values=consulta)
      
  tree.pack(padx=10, pady=10)
 
      
  
  
  
  
  
  
  
  
  #voltar2 = CTkButton(frame_descricao2, text="Voltar", command=lambda: fechar_janela_7_abrir_janela_6(),font=CTkFont(size=12))  
  #voltar2.pack(padx=10,pady=10)

  
  janela_7.mainloop()
 

    

janela_1 = CTk() # Abertura da Janela 

set_appearance_mode("dark")
set_default_color_theme("dark-blue")
janela_1.title("PitMed: Gestão Clínica") 
janela_1.geometry("600x400")
janela_1.resizable(False, False)

imagem_botao = Image.open("gestao_clinica.ico")

imagem_tela = CTkImage(dark_image=Image.open("Logo_clinica.png"), size=(400, 300))

# Adicionando a imagem como fundo
label_imagem = CTkLabel(janela_1, image=imagem_tela, text="")  # Convertendo para ImageTk
label_imagem.place(x=0, y=50)

frame_descricao = CTkFrame(janela_1, width=220, height=400) 
frame_descricao.place(x=400, y=50) 

descricao = CTkLabel(frame_descricao, text="Bem-vindo a PitMED!", wraplength=180, justify='center', font=CTkFont(size=20))
descricao.grid(row=0, column=0, padx=10, pady=10) 

iniciar = CTkButton(frame_descricao,text="Vamos La!",command=fechar_janela_1_abrir_janela_6, width=20, image=CTkImage(imagem_botao), font=CTkFont(size=12)) 
iniciar.grid(row=2, column=0, padx=10, pady=10)

 

janela_1.mainloop() #Fechamento da Janela


