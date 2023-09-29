# # def calculadora2():
# #     n1 = float(input("Digite um número aqui: "))
# #     operacao = input("Digite a operação desejada dentro do (), Subtração(-), Divisão(/), Multiplicação(*), Adição(+): ")
    
# #     if operacao not in ["-", "+", "/", "*"]:
# #         print("Insira uma operação válida!")
# #     else:
# #         n2 = float(input("Digite outro número aqui: "))
# #         if operacao == "-":
# #             print(f'{n1} - {n2} = {n1 - n2}')
# #         elif operacao == "+":
# #             print(f'{n1} + {n2} = {n1 + n2}')
# #         elif operacao == "/":
# #             if n2 == 0:
# #                 print("Erro! Divisão por zero não é permitida.")
# #             else:
# #                 print(f'{n1} / {n2} = {n1 / n2}')
# #         elif operacao == "*":
# #             print(f'{n1} * {n2} = {n1 * n2}')

# # calculadora2()

# ####################################################################################################################
# ### Desafio, Restaurante
# ##
# # bebidas = ('Agua', 'Refrigerante', 'Vinho')
# # comidas = ('Macarronada', 'Pizza', 'Camarão')
# # lista = [item.lower() for item in bebidas + comidas] 
# # print(f"Aqui está uma lista do que você pode pedir para comer {comidas}")
# #
# # opcaoComida = input("Digite aqui o que você quer comer: ").lower() 
# # print(f"Aqui está uma lista do que você pode pedir para comer {bebidas}")
# # opcaoBebida = input("Digite aqui o que você quer beber: ").lower()  
# #
# # if opcaoComida in lista and opcaoBebida in lista:
# #     print(f"Para comer, você selecionou {opcaoComida} e para beber você escolheu {opcaoBebida}")
# # else:
# #
# #      print("A opção que você selecionou não está em nosso cardápio!")
# ##
# ####################################################################################################################

# # Solicitar números e operação do usuário
# a = float(input("Digite o primeiro número: "))
# b = float(input("Digite o segundo número: "))
# op = input("Digite a operação desejada (+, -, *, /): ")

# # Definir funções para as operações
# def soma(a, b):
#     return a + b

# def subtracao(a, b):
#     return a - b

# def multiplicacao(a, b):
#     return a * b

# def divisao(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return "Divisão por zero não é permitida."

# # Realizar a operação selecionada
# def calc():
#     if op == '+':
#         resultado = soma(a, b)
#     elif op == '-':
#         resultado = subtracao(a, b)
#     elif op == '*':
#         resultado = multiplicacao(a, b)
#     elif op == '/':
#         resultado = divisao(a, b)
#     else:
#         resultado = "Operação inválida. Use +, -, *, ou /."

#     # Exibir o resultado
#     print(f"Resultado da operação: {resultado}")
# calc()


    ##### AULA 9 PARTE 2

# dicionario = {"key":"value","key2":"value2"}
# # menino = {"nome":"caio","idade":"18","endereco":"rua 30"}
# # x = menino["nome"]
# # y = menino["idade"]
# # z = menino["endereco"]
# # print(x)
# # print(y)
# # print(z)

# # menino = {"nome":"caio","idade":"18","endereco":"rua 30"}
# # del menino["endereco"]
# # print(menino)

# # n = menino.pop('idade')
# # menino['notas'] = 7 # adicionar valor no dicionario
# # if 'nome' in menino:
# #   print("O nome do menino é, " menino['nome'])

# ### Sistema de notas 

# # notas ={
# #     "José": 9,
# #     "Maria": 10,
# #     "João":7
# # }
# # nome = input("Digite aqui o nome do aluno: ")
# # notas = float(input("Digite aqui a nota do aluno: "))
# #   if nota.get(nome):
# #     print("Já existe esse aluno!")
# #   else:
# #     nota[nome] = notas
# #     print(notas)


# #Exercicio 1 - Crie um dicionário que represente um #dicionário de sinônimos. Em seguida, #peça ao usuário para digitar uma palavra e se a palavra estiver no dicionário, mostre o seu sinônimo crie um dicionário com 5 letras, e acesse #o 3º indice

# # dic = {
# #     "feio": "bonito",
# #     "magro": "gordo",
# #     "alto": "baixo",
# #     "magnífico": "belo",
# #     "rápido": "veloz"
# # }

# # opcaoUser = input("Digite uma palavra aqui: ").lower()

# # if opcaoUser in dic:
# #     print(f"O sinônimo de {opcaoUser} é: {dic[opcaoUser]}")
# # else:
# #     print(f"A palavra '{opcaoUser}' não está no dicionário.")

# # ###Exercicio 2 - Crie um dicionário com 5 letras, e acesse #o 3º indice
# #  dic = {
# #      "value0":"a",
# #      "value1":"b",
# #      "value2":"c",
# #      "value3":"d",
# #      "value4":"e"
# #  }
# # valor = dic
# #     print(dic[2]) 

# #####################################################################################################################
# # sinonimos = {
# #     "feliz": "radiante",
# #     "triste": "desolado",
# #     "grande": "colossal",
# #     "pequeno": "minúsculo",
# #     "rápido": "veloz"
# # }

# # while True:
# #     palavra = input("Digite uma palavra para encontrar seu sinônimo (ou 'sair' para encerrar): ").lower()

# #     if palavra == 'sair':
# #         print("Encerrando o programa. Até mais!")
# #         break
    
# #     if palavra in sinonimos:
# #         print("Sinônimo de", palavra, "é", sinonimos[palavra])
# #     else:
# #         print("Palavra não encontrada no dicionário de sinônimos.")
        
# #         novo_sinonimo = input("Digite o sinônimo da palavra ou 'cancelar' para não adicionar: ").lower()
        
# #         if novo_sinonimo == 'cancelar':
# #             continue  # Volte para o início do loop
            
# #         sinonimos[palavra] = novo_sinonimo
# #         print("Nova palavra e sinônimo adicionados ao dicionário.")

# sinonimos = {
#     "feliz": "radiante",
#     "triste": "desolado",
#     "grande": "colossal",
#     "pequeno": "minúsculo",
#     "rápido": "veloz"
# }

# while True:
#     palavra = input("Digite uma palavra para encontrar seu sinônimo (ou 'sair' para encerrar): ").lower()

#     if palavra == 'sair':
#         print("Encerrando o programa. Até mais!")
#         break
    
#     encontrado = False
    
#     # Busca nas chaves do dicionário
#     for chave in sinonimos:
#         if palavra == chave:
#             print("Sinônimo de", palavra, "é", sinonimos[chave])
#             encontrado = True
#             break
    
#     # Se não foi encontrado nas chaves, busca nos valores do dicionário
#     if not encontrado:
#         for chave, valor in sinonimos.items():
#             if palavra == valor:
#                 print("A palavra", chave, "é um sinônimo de", palavra)
#                 encontrado = True
#                 break
    
#     # Se não foi encontrado, permite ao usuário adicionar a palavra e o sinônimo
#     if not encontrado:
#         novo_sinonimo = input(f"A palavra '{palavra}' não foi encontrada. Digite o sinônimo da palavra: ").lower()
#         sinonimos[palavra] = novo_sinonimo
#         print("Palavra e sinônimo adicionados ao dicionário:")
        
#         # Mostra o dicionário com palavras e sinônimos em duas colunas
#         print("{:<15} {:<15}".format("Palavra", "Sinônimo"))
#         for chave, valor in sinonimos.items():
#             print("{:<15} {:<15}".format(chave, valor))















