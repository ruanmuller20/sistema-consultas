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