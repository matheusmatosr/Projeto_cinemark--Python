import random

lista_filmes = ["Procurando nemo", "Invocação do mal", "Velozes e furiosos"]
lista_clientes = []
interessados = []
lista_similaridade = []
matriz_votos = []
lista_juntos = []

#=================================== ENTRADA DE DADOS ==========================================================
while (len(interessados) < 3):
  print('----------Cinemark Shopping Vitória----------')
  print("")
  print('Você foi convidado para avaliação dos filmes que estão em cartaz!')
  print('Após avaliar, ganhará um ticket de 10% de desconto na compra de um ingresso!')
  print("")
  tem_interesse = input('Tem interesse em participar? Se sim, digite o n°1 mas se não, digite o n°0. ')
  print("")
  if(tem_interesse == "1"):
    matriz_votos.append([])
    interessados.append(tem_interesse)

    # Pegar o nome do cliente
    nome_cliente = str(input('Informe seu nome completo:  '))
    lista_clientes.append(nome_cliente)
    print(f'Seja bem vindo, {nome_cliente.title()}!')
    print(f'Obrigado por aceitar o convite e vamos para avalicação!')
    print('Os filmes deveram ser avaliados obrigatoriamente de 0-10!')
    print("")
    print('--Avaliação dos filmes--')
    print("")
    
    for i in range(len(lista_filmes)):
      voto = -1
      
      # Pedir o voto do filme i até q seja um voto válido
      while not(voto >= 0 and voto <= 10):
        voto = float(input(f'{lista_filmes[i]}:  '))
        if voto >= 0 and voto <= 10:
          matriz_votos[len(matriz_votos) - 1].append(voto)
        else:
          print("Voto inválido. Digite novamente...")
          print("")
    
    # Verifica se o cliente votou nos 3 filmes
    if(len(matriz_votos[len(matriz_votos) - 1]) == len(lista_filmes)):
      codigo = random.randint(10000, 90000)
      print(f'Parabéns {nome_cliente.title()}, você ganhou 10% de desconto na compra de ingressos com validação de 2 meses a partir de hoje! Código: {codigo} ')
      print("")
      print('Obrigado por votar!')
  elif(tem_interesse == "0"):
    print('Obrigado por votar!')
  else:
    print('Valor inválido, tente novamente!')
print("")
#=================================== Exibicao de votos ==========================================================
print('----------Resultado das avaliações----------')

for i in range(len(lista_clientes)):
  print("")
  print(f'Cliente {i+1}: {lista_clientes[i].title()}')
  for k in range(len(matriz_votos)):
    print(f'Voto filme {lista_filmes[k]}: {matriz_votos[i][k]}')
    
#=================================== Calculo similaridade ==========================================================
for cliente1 in range(len(lista_clientes)):
  for cliente2 in range(len(lista_clientes)):
    if cliente1 != cliente2 and cliente1 < cliente2:
      nomes_juntos = lista_clientes[cliente1]+ '-' + lista_clientes[cliente2]
      lista_juntos.append(nomes_juntos)
      
      soma = 0
      for column1 in range(len(matriz_votos[cliente1])):
        for column2 in range(len(matriz_votos[cliente2])):
          if column1 == column2:
            P1 = matriz_votos[cliente1][column1]
            Q1 = matriz_votos[cliente2][column2]
            soma = soma + (P1-Q1)**2
      d_euclidiana = soma**0.5
      lista_similaridade.append(d_euclidiana)
      print("")
# Calcula a menor distância:  
menor  = 0
for x in range(len(lista_similaridade)):
  if lista_similaridade[x] < lista_similaridade[menor]:
    menor = x
print('Os usuário mais similares são', lista_juntos[menor])
