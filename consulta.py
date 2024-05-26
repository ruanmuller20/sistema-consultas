import pandas as pd
import openpyxl
import customtkinter


nome = input('Digite seu nome todo: ')
numero = int(input('Digite seu numero: '))
cpf = int(input('Informe seu cpf: '))

consulta = input(f'Olá Sr(a).{nome}, digite a palavra "agendamento" para ter acesso as especialidades: ')
especialidade = ['Cardiologia', 'Pediatria', 'Fisiatra']
medicos = ['Ruan Müller', 'Ícaro Lima', 'Alan Gabriel']




match consulta:
    case "agendamento":
        opcao = int(input('Digite a especialidade que deseja agendar: \n [0] Cardiologia \n [1] Pediatria \n [2] Fisiatra \n'))
    
        if opcao < len(especialidade):
           print(f'-----MÉDICOS DISPONÍVEIS----- \n Dr. {medicos[opcao]}')
           
        
           dia_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
           agendar = int(input('Selecione o dia da sua consulta: [0] segunda, [1]terça, [2]quarta, [3]quinta, [4]sexta, [5]sábado '))
        if agendar < len(dia_semana):
               print(f'---DIA SELECIONADO--\n{dia_semana[agendar]}\n ---HORÁRIOS DISPONIVÉIS---\n 14:00\n 15:00\n 16:00\n 17:00')
               
               horario = ['14:00', '15:00', '16:00', '17:00']
               marcar_horario = int(input('Digite o horário desejado [0]14:00, [1]15:00, [2]16:00, [3]17:00: '))
               if marcar_horario < len(horario):
                print(f'CONSULTA MARCADA AS {horario[marcar_horario]} HORAS para o paciente {nome}, portador do cpf {cpf}.')

                # Criando o datadframe

                dados = {'Nome': [nome],
                         'Número': [numero],
                         'CPF': [cpf],
                         'Especialidade': [especialidade[opcao]],
                         'Médico': [medicos[opcao]],
                         'Dia': [dia_semana[agendar]],
                         'Horário': [horario[marcar_horario]]}
                
                # Criando a variavel atribuindo o dataframe

                df = pd.DataFrame(dados)

                # Exportando para Excel
                df.to_excel('consulta_agendada.xlsx', index=False)
                print("Dados exportados com sucesso para 'consulta_agendada.xlsx'.")
                
                
def exibir_consulta():
  global janela_7 
  janela_7 = CTk()
 
  set_appearance_mode("dark")
  set_default_color_theme("dark-blue")
  #janela_7.title("PitMed: Gestão Clínica") 
  #janela_7.geometry("600x400")
  #janela_7.resizable(False, False)
  
  titulo = CTkLabel(janela_7, text="Consultas Agendadas ", font=CTkFont(family="Arial", size=15, weight="bold"))
  titulo.place(x=180, y=35)
  
  frame_descricao2 = CTkFrame(janela_7, width=220, height=400) 
  frame_descricao2.place(x=400, y=50) 
  
  verificar_consultas = "SELECT * FROM consulta"
  cursor.execute(verificar_consultas)
  consultar = cursor.fetchall()
  
  tree = ttk.Treeview(frame_descricao2)
  estilo = ttk.Style()
  estilo.configure("Treeview.Heading", font=('Helvetica', 10, 'bold'))
  
  tree["columns"] = ("ID", "medico", "data", "horario", "cpf")
  
  tree.column("#0", width=0, stretch=tk.NO)
  tree.column("ID", anchor=tk.W, width=200)
  tree.column("medico", anchor=tk.W, width=200)
  tree.column("data", anchor=tk.W, width=200)
  tree.column("horario", anchor=tk.W, width=200)
  tree.column("cpf", anchor=tk.W, width=200)
  
  #cabeçalho
  tree.heading("#0",text="",anchor=tk.W)
  tree.heading("ID",text="ID",anchor=tk.W)
  tree.heading("medico",text="Medico",anchor=tk.W)
  tree.heading("data",text="Data",anchor=tk.W)
  tree.heading("horario",text="Horário",anchor=tk.W)
  tree.heading("cpf",text="Cpf",anchor=tk.W)
  
  tree.insert("", tk.END, values=([0],[1],[2],[3],[4]))
  
  tree.pack(padx=10, pady=10)

      
  
  
  
  
  
  
  
  
  voltar2 = CTkButton(frame_descricao2, text="Voltar", command=lambda: fechar_janela_7_abrir_janela_6(), image=CTkImage(imagem_botao), font=CTkFont(size=12))  
  voltar2.grid(pady=10)

  
  janela_7.mainloop()