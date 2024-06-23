# Clinica-de-consulta-agil
# Desafio:
Desenvolvir a Clínica de Consultas Ágil através do desafio que recebi ao participar do processo seletivo do Programa Aceleradora Ágil.

# Cadastrar Paciente
O programa solicita o nome e o telefone do usuário. Após o cadastro, exibe a mensagem "Paciente cadastrado com sucesso" e adiciona o paciente à lista de Pacientes Cadastrados. Em seguida, retorna ao menu principal.

# Marcações de Consulta
Ao selecionar essa opção, o programa exibe uma lista numerada dos pacientes cadastrados. Ao escolher o número correspondente a um paciente, solicita o dia, a hora e a especialidade desejada para a consulta. Após o envio desses dados, o agendamento é adicionado à lista de agendamentos e o programa retorna ao menu principal.

# Cancelamento de Consultas
Ao selecionar essa opção, o programa exibe uma lista numerada dos agendamentos existentes. Ao escolher o número correspondente ao agendamento que deseja remarcar, é exibida uma mensagem informando a data, a hora e a especialidade da consulta agendada. Nesse momento, o usuário pode optar por cancelar a consulta. Ao confirmar o cancelamento, o agendamento é removido da lista e o programa retorna ao menu principal.

# Sair
O programa encerra a execução.

# Tratamento de Erros
O paciente não pode ser cadastrado mais de uma vez. Para evitar duplicidade, garanta que o número de telefone seja diferente para cada cadastro. Caso ocorra uma tentativa de cadastro duplicado, exiba a mensagem "Paciente já cadastrado!" e retorne ao menu principal.
Pacientes não podem marcar consultas em dias e horários já agendados. Verifique se a data e a hora selecionadas estão disponíveis antes de realizar o agendamento.
Consultas não podem ser marcadas antes da data atual. Certifique-se de que o usuário não possa agendar consultas retroativas.

# Extra
Seria muito legal se você conseguisse implementar uma maneira de armazenar as informações dos pacientes de forma que eles continuassem existindo mesmo após o usuário sair do sistema. Que funcionasse como uma espécie de “banco de dados”.

# Funcionalidades do Projeto
Funcionalidade 1: cadastar pacientes.
Funcionalidade 2: marcações de consultas.
Funcionalidade 3: cancelamento de consultas.
Funcionalidade 4: sair/finalizar o programa.
Funcionalidade 5: armazenamento de dados.

# Tomada de decisão
Escolhi Python pela sua alta abstração, suporte a múltiplos paradigmas e sintaxe simples. Armazeno dados em arquivos de texto pela facilidade e leveza. Para melhorar a simulação, usei a interface Tkinter, que permite criar uma interface gráfica intuitiva sem a necessidade de um SGBD externo.

