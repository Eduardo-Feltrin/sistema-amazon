#1 - Cadastrar novos clientes

#primeiramente vou definir uma classe chamada "usuario" para organizar melhor o código

class usuario:
  nome:None
  cpf:None
  senha:None
  email:None
  limite_credito:None

#Pronto isso, agora vou criar uma lista para armazenar as variáveis que são da classe "usuario" para não perder as informações.

usuarios = []

#agora vou definir uma função para cadastrar os novos clientes, se eles ja estiverem cadastrados ocorrerá um erro.

def cadastro():
  global usuario1 #defini a variavel usuario1 como global para poder usa-la com um leque maior de possibilidades. 
  usuario1 = usuario()
  usuario1.nome = input("Insira seu nome ")
  usuario1.cpf = float(input("Insira seu cpf "))
  valida_cpf(usuario1.cpf)
  usuario1.senha = input("Insira sua senha ")
  usuario1.email = input("Insira seu email ")
  usuario1.limite_credito = input("Insira o limite de crédito da sua conta")
  if usuario1 not in usuarios:
    usuarios.append(usuario1)
  else:
    print("Seu usuário já está cadastrado ")

def consulta_cliente(cpf):
  if cpf == usuario1.cpf:
    print(usuario1.nome)
    print(usuario1.email)


#Essa é a função usada acima para validar o cpf      

ultimo_digitos = []   # <- Essa lista é usada apenas para armazenar os dois ultimos dígitos da função "valida_cpf"     
def valida_cpf(cpfx): 
  operacao = 0
  n = 2
  cpfx = cpfx.split() #irei usar a função split para colocar os números do cpf em uma lista e depois valida-lo.
  for x in range(3):
    for i in cpfx:
      operacao += i * n
      n += 1
      if operacao%11 < 2:
        cpfx.append(0)
        ultimo_digitos.append(0)
      else:
        cpfx.append(11-operacao%11)
        ultimo_digitos.append(11-operacao%11)
    if ultimo_digitos[0] == cpfx[-2] and ultimo_digitos[1] == cpfx[-1]:
      print("O cpf inserido é valido")
    else:
      print("O cpf inserido é inválido")

#2 - Compras
#Aqui está a tabela de preços dos produtos disponíveis
#Vou criar uma classe para poder consultar os valores depois e organizar melhor meu código

class produtos:
  valor = None
  nome = None

lista_produtos = []
preco_produtos = []

pasta_dente = produtos()
pasta_dente.valor = 5
pasta_dente.nome = "Pasta de dente"
lista_produtos.append(pasta_dente.nome)
preco_produtos.append(pasta_dente.valor)

arroz_1kg = produtos()
arroz_1kg.valor = 8
arroz_1kg.nome = "Arroz de 1kg"
lista_produtos.append(arroz_1kg.nome)
preco_produtos.append(arroz_1kg.valor)

feijao_1kg = produtos()
feijao_1kg.valor = 4
feijao_1kg.nome = "Feijão de 1kg"
lista_produtos.append(feijao_1kg.nome)
preco_produtos.append(feijao_1kg.valor)

batata_1kg = produtos()
batata_1kg.valor = 4
batata_1kg.nome = "Batata de 1kg"
lista_produtos.append(batata_1kg.nome)
preco_produtos.append(batata_1kg.valor)

brocolis_1kg = produtos()
brocolis_1kg.valor = 12
brocolis_1kg.nome = "Brócolis de 1kg"
lista_produtos.append(brocolis_1kg.nome)
preco_produtos.append(brocolis_1kg.valor)

sardinha_lata = produtos()
sardinha_lata.valor = 5
sardinha_lata.nome = "Sardinha lata"
lista_produtos.append(sardinha_lata.nome)
preco_produtos.append(sardinha_lata.valor)

pao_fatiado = produtos()
pao_fatiado.valor = 5
pao_fatiado.nome = "Pão Fatiado"
lista_produtos.append(pao_fatiado.nome)
preco_produtos.append(pao_fatiado.valor)

cafe_lata = produtos()
cafe_lata.valor = 7
cafe_lata.nome = "Café lata"
lista_produtos.append(cafe_lata.nome)
preco_produtos.append(cafe_lata.valor)

milho_lata = produtos()
milho_lata.valor = 5
milho_lata.nome = "Milho lata"
lista_produtos.append(milho_lata.nome)
preco_produtos.append(milho_lata.valor)

banana_nanica1kg = produtos()
banana_nanica1kg.valor = 4
banana_nanica1kg.nome = "Banana nanica 1kg"
lista_produtos.append(banana_nanica1kg.nome)
preco_produtos.append(banana_nanica1kg.valor)

maca_1kg = produtos()
maca_1kg.valor = 6
maca_1kg.nome = "Maçã 1kg"
lista_produtos.append(maca_1kg.nome)
preco_produtos.append(maca_1kg.valor)

#Essa é a tabela que vai aparecer se selecionarem a opção "comprar"

def comprar():
  n = 0
  y = 0
  for i in range(len(lista_produtos)):
    print(str(n) + "-" + str(lista_produtos[y]) + " " + str(preco_produtos[y]) + " reais")
    n += 1
    y += 1
  print("Aperte a tecla 'n' para voltar ao menu ")
  while True:
    produto = input("Insira a posição do item que você quer comprar ")
    quantia = int(input("Insira quantas unidades do produto você deseja "))
    for i in range(quantia+1):
      carrinho_compras.append(lista_produtos[int(produto)])
    if produto == "n":
      break

#Acima é onde dependendo do input os produtos serão adicionados ao carrinho do próximo bloco. 


#Carrinho de compras
carrinho_compras = []

#Mostrar carrinho
def ver_carrinho():
  ver_carrinho = input("Deseja ter acesso ao seu carrinho de compras?\nDigite 's' para sim e 'n' para não")
  if ver_carrinho == "s":
    print(carrinho_compras)
    print("O valor total do seu carrinho é de ", sum(carrinho_compras), "reais")
  elif ver_carrinho == "n":
    print("Ação cancelada")
  else:
    print("Erro")

#Pagar conta
# Defini logo na criação da classe "usuario" um limite fixo no cartão de crédito de 1000.
def pagar_conta():
  resultado_compra = usuario1.limite_credito - sum(carrinho_compras)
  print(f"O total do seu carrinho é de {sum(carrinho_compras)}\nSeu limite de crédito atual é de {usuario1.limite_credito}\nO resultado da sua possível compra é de {resultado_compra}")
  comprar = input.lower("Digite 's' para comprar e 'n' para cancelar a compra")
  if comprar == "n":
    print("Você não possui limite suficiente")
    print(f"O limite do seu cartão de crédito atualmente é de {usuario1.limite_credito} e o resultado da compra foi de {resultado_compra}")
  elif comprar == "s":
    usuario1.limite_credito = usuario1.limite_credito - sum(carrinho_compras)
    print(f"Sua compra foi realizada com sucesso\nVocê ainda tem {usuario1.limite_credito} de crédito")
  else:
    print("Erro")

#Menu Principal

def menu():
  opcao = "-1"
  print("Seja bem vindo! Esse é o menu principal, escolha dentre as seguinte opções:\n\n1 - Cadastro\n2- Comprar\n3- Mostrar carrinho\n4- Pagar conta\n5- Consultar cliente\n6- Validar CPF\n0- Sair")
  while True:
    opcao = input()
    if opcao == "1":
      print("Opção selecionada: Cadastro")
      cadastro()
    elif opcao == "2":
      print("Opção selecionada: Comprar")
      comprar()
    elif opcao == "3":
      print("Opção selecionada: Mostrar Carrinho")
      ver_carrinho()
    elif opcao == "4":
      print("Opção selecionada: Pagar conta")
      pagar_conta()
    elif opcao == "5":
      print("Opção selecionada: Consultar cliente")
      consulta_cliente()
    elif opcao == "6":
      print("Opção selecionada: Validar CPF")
      valida_cpf()
    elif opcao == "0":
      print("Opção selecionada: Sair")
      break
    else:
      print("Opção inválida, tente novamente")

menu()





    







          
          




