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

#1-Cadastro
#agora vou definir uma função para cadastrar os novos clientes, se eles ja estiverem cadastrados ocorrerá um erro.

def cadastro():
  global usuario1 #defini a variavel usuario1 como global para poder usa-la com um leque maior de possibilidades. 
  usuario1 = usuario()
  usuario1.nome = input("Insira seu nome ")
  usuario1.cpf = input("Insira seu cpf ")
  valida_cpf(usuario1.cpf)
  usuario1.senha = input("Insira sua senha ")
  usuario1.email = input("Insira seu email ")
  usuario1.limite_credito = int(input("Insira o limite de crédito da sua conta "))
  if usuario1 not in usuarios:
    usuarios.append(usuario1)
  else:
    print("Seu usuário já está cadastrado ")

#2-Consultar cliente
def consulta_cliente(cpf):
  if cpf == usuario1.cpf:
    print(f"O nome do cliente é {usuario1.nome}")
    print(f"O email do cliente é {usuario1.email}")

#3-Comprar
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
  for i in range(len(lista_produtos)):
    print(str(n) + "-" + str(lista_produtos[i]) + " " + str(preco_produtos[i]) + " reais")
    n += 1
  print("Aperte a tecla 'n' para voltar ao menu ")
  while True:
    produto = input("Insira a posição do item que você quer comprar ")
    quantia = input("Insira quantas unidades do produto você deseja ")
    if produto == "n" or quantia == "n":
      break
    elif produto == "N" or quantia == "N":
      break
    for i in range(int(quantia)+1):
      carrinho_compras.append(lista_produtos[int(produto)])
      total_carrinho_compras.append(preco_produtos[int(produto)])

#Acima é onde dependendo do input os produtos serão adicionados ao carrinho do próximo bloco. 


#4-Carrinho de compras
carrinho_compras = []
total_carrinho_compras = []

#Mostrar carrinho
def ver_carrinho():
  ver_carrinho = input("Deseja ter acesso ao seu carrinho de compras?\nDigite 's' para sim e 'n' para não\n")
  if ver_carrinho == "s" or "S":
    for i in lista_produtos:
      print(f"Você colocou no seu carrinho {i.count} {i}'s'")
    print(f"O valor total do seu carrinho é de {sum(total_carrinho_compras)} reais")
    remover_carrinho = input("Deseja remover algum item do seu carrinho?\nDigite 's' para sim e 'n' para não\n")
    if remover_carrinho == 's' or remover_carrinho == 'S':
      n = 0
      for i in range(len(lista_produtos)):
        print(str(n) + "-" + str(lista_produtos[i]))
        n += 1
      while True: 
        item = input("Insira o produto que quer remover pelo seu índice\nDigite 'n' quando quiser parar de remover os produtos\n")
        quantidade = int(input("Insira quantos produtos deseja remover\nDigite '0' para cancelar\n"))
        if item == "n" or item == "N":
          break
        elif quantidade == 0:
          break
        for l in range(quantidade):
          print(f"Você removeu {carrinho_compras.pop(int(item))}'s'")
          total_carrinho_compras.pop(int(item))
    elif ver_carrinho == "n" or "N":
      print("Ação cancelada")
    else:
      print("Erro")

#5-Pagar conta
# Defini logo no cadastro um limite fixo no cartão de crédito de 1000.
def pagar_conta():
  resultado_compra = usuario1.limite_credito - sum(total_carrinho_compras)
  print(f"O total do seu carrinho é de {sum(total_carrinho_compras)}\nSeu limite de crédito atual é de {usuario1.limite_credito}\nO resultado da sua possível compra é de {resultado_compra}")
  comprar = input("Digite 's' para comprar e 'n' para cancelar a compra ")
  if comprar == "n" or comprar == "N":
    print("Compra cancelada!")
  elif comprar == "s" or comprar == "S":
    usuario1.limite_credito = usuario1.limite_credito - sum(total_carrinho_compras)
    print(f"Sua compra foi realizada com sucesso\nVocê ainda tem {usuario1.limite_credito} de crédito")
  elif resultado_compra<0:
    print("Você não possui limite suficiente")
    print(f"O limite do seu cartão de crédito atualmente é de {usuario1.limite_credito} e a tentativa da compra foi de {resultado_compra}")
  else:
    print("Erro")

#6-Validar CPF
#Essas duas listas servem para calcular os dois ultimos dígitos e validar o cpf junto das duas funções que compõe a "valida_cpf".

cpfx_lista_int = []
cpfx_lista_string = 0

ultimo_digitos = []   # <- Essa lista é usada apenas para armazenar os dois ultimos dígitos da função "valida_cpf"     
def valida_cpf1(parametro): 
  operacao = 0
  n = 10
  j = 1
  cpfx_lista_string = parametro
  for i in cpfx_lista_string:
    cpfx_lista_int.append(int(i))
  cpfx_lista_int.pop()
  cpfx_lista_int.pop()
  for i in cpfx_lista_int:
    operacao += i * n
    n = n - j #estou começando do 10 porque a validação exige que eu multiplique os algarismo do cpf da direita para a esquerda começando no 2, eu estou fazendo o caminho inverso começando da esquerda para a direita
    j += 1
  if operacao%11 < 2:
    cpfx_lista_int.append(0)
    ultimo_digitos.append(0)
  else:
    cpfx_lista_int.append(11-operacao%11)
    ultimo_digitos.append(11-operacao%11)


def valida_cpf2():
  operacao = 0
  n = 11
  j = 1
  for i in cpfx_lista_int:
    operacao += i * n
    n = n - j #estou começando do 11 porque a validação exige que eu multiplique os algarismo do cpf da direita para a esquerda começando no 2, eu estou fazendo o caminho inverso começando da esquerda para a direita
    j += 1
  if operacao%11 < 2:
    cpfx_lista_int.append(0)
    ultimo_digitos.append(0)
  else:
    cpfx_lista_int.append(11-operacao%11)
    ultimo_digitos.append(11-operacao%11)

def valida_cpf(parametro):
  valida_cpf1(parametro)
  valida_cpf2()
  if ultimo_digitos[0] == cpfx_lista_int[-2] and ultimo_digitos[1] == cpfx_lista_int[-1]:
    print("O cpf inserido é valido")
  else:
    print("O cpf inserido é inválido")
    cpfx_lista_int.clear()
#Menu Principal

def menu():
  opcao = "-1"
  cadastro()
  while True:
    opcao = input("Seja bem vindo! Esse é o menu principal, escolha dentre as seguinte opções:\n\n1- Cadastro\n2- Consultar cliente\n3- Comprar\n4- Carrinho de compras\n5- Pagar conta \n6- Validar CPF\n0- Sair\n")
    if opcao == "1":
      print("Opção selecionada: Cadastro")
      cadastro()
    elif opcao == "2":
      print("Opção selecionada: Consultar cliente")
      parametro_consulta = input("Insira o CPF\n")
      consulta_cliente(parametro_consulta)
    elif opcao == "3":
      print("Opção selecionada: Comprar")
      comprar()
    elif opcao == "4":
      print("Opção selecionada: Carrinho de compras")
      ver_carrinho()
    elif opcao == "5":
      print("Opção selecionada: Pagar conta")
      pagar_conta()
    elif opcao == "6":
      print("Opção selecionada: Validar CPF")
      parametro_valida_cpf= input("Insira o CPF\n")
      valida_cpf(parametro_valida_cpf)
    elif opcao == "0":
      print("Opção selecionada: Sair")
      break
    else:
      print("Opção inválida, tente novamente")

menu()





    







          
          




