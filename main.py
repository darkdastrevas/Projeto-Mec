from modulo import *

cinema = []
exibir_menu()
while True:
  n = int(input('Escolha uma opção de 1 a 6: '))
  
  #Adicionar Sala
  if n == 1:
    while True:
      numero_sala = int(input('\nNúmero da sala: '))
      filme = input('Nome do filme: ')
      genero = input('Gênero do filme: ')
      idade_minima = int(input(f'Idade mínima para assistir ao filme {filme}: '))
      data_saida = formatar_data(input('Data de saída (ddmmaaaa): '))
      adicionar_sala(cinema, numero_sala, filme, genero, idade_minima, data_saida)
      op = input('\nDeseja adicionar outra sala? S/N: ')
      while op not in 'SsNn':
        print('Opção inválida! Digite S para Sim ou N para Não.')
        op = input('\nDeseja adicionar outra sala? S/N: ').strip()
      if op in 'Nn':
        break
          
  #Atualizar sala     
  elif n == 2:
    while True:
      sala = int(input('Número da sala que deseja atualizar: '))
      atualizar_filme(cinema, sala)
      op = input('\nDeseja atualizar outra sala? S/N: ')
      while op not in 'SsNn':
        print('Opção inválida! Digite S para Sim ou N para Não.')
        op = input('\nDeseja atualizar outra sala? S/N: ').strip()
      if op in 'Nn':
        break

  #Remover sala
  elif n == 3:
    while True:
      sala = int(input('Número da sala para remover: '))
      remover_sala(cinema, sala)
      op = input('\nDeseja remover outra sala? S/N: ')
      while op not in 'SsNn':
        print('Opção inválida! Digite S para Sim ou N para Não.')
        op = input('\nDeseja remover outra sala? S/N: ').strip().upper()
      if op in 'Nn':
        break
  
  #Parar programa
  m = input("\nDeseja realizar outra operação? S/N: ")
  while m not in 'SsNn':
    print('Opção inválida! Digite S para Sim ou N para Não.')
    m = input('\nDeseja realizar outra operação? S/N: ').strip()
  if m in 'Nn':
    break
print(cinema)
