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














