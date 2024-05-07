#1)
# num_1 = int(input("num1: "))
# num_2 = int(input("num2: "))
# for numeros in range(num_1, num_2):
#     print(numeros)

#2)
# bacteria_a = 4
# bacteria_b = 10
# taxa_crescimento_a = 0.03
# taxa_crescimento_b = 0.15
# qtd_dias = 0
#
# while bacteria_a < bacteria_b:
#     bacteria_a += (taxa_crescimento_a * bacteria_a)
#     bacteria_b += (taxa_crescimento_b * bacteria_b)
#     qtd_dias += 1
#
# print(f"A quantidade de dias para ultrapassar foi {qtd_dias}")

#3)
# for elemento in range(1, 16):
#     nota = int(input(f"informe a nota {elemento}: "))
#     while nota < 0 or nota > 5:
#         nota = int(input(f"por favor, informe novamente a nota {elemento} com um valor válido: "))
#     print(nota)

#4)
# temp_celsius = float(input("informe uma temperatura em celsius: "))
# media_temp = 0.0
# qtd_temp = 0
# soma_temp = 0.0
# while temp_celsius != -273:
#     qtd_temp += 1
#     soma_temp += temp_celsius
#     media_temp = soma_temp/qtd_temp
#     temp_celsius = float(input("informe uma temperatura em celsius: "))
#
# print(f"Média: {media_temp}")

#5)
# num = int(input("informe um número: "))
# fatorial = num
# while num > 1:
#     num -=1
#     fatorial *= num
#
# print(f"Fatorial: {fatorial}")

#6)
# num = int(input("informe um número: "))
# for i in range(1, 11):
#     print(f"{num} * {i} = {num*i}")

#7
# num = int(input("informe um número: "))
# if num % 2 == 0:
#     print("não é número primo")
# else:
#     print("é número primo")

#8)
# idade_pensionistas = int(input("informe uma idade: "))
# while idade_pensionistas != -1:
#     if idade_pensionistas <= 25:
#         print("Intervalo [0-25]")
#     elif idade_pensionistas <= 50:
#         print("Intervalo [26-50]")
#     elif idade_pensionistas <= 75:
#         print("Intervalo [51-75]")
#     elif idade_pensionistas <= 100:
#         print("Intervalo [76-100]")
#     else:
#         print("Idade fora do intervalo")
#
#     idade_pensionistas = int(input("informe uma idade: "))

#9)
# qtd_votos_candidato_1 = 0
# qtd_votos_candidato_2 = 0
# qtd_votos_candidato_3 = 0
# qtd_votos_candidato_4 = 0
#
# qtd_votos_branco_candidato_1 = 0
# qtd_votos_branco_candidato_2 = 0
# qtd_votos_branco_candidato_3 = 0
# qtd_votos_branco_candidato_4 = 0
#
# qtd_votos_nulo_candidato_1 = 0
# qtd_votos_nulo_candidato_2 = 0
# qtd_votos_nulo_candidato_3 = 0
# qtd_votos_nulo_candidato_4 = 0
#
# total_votos_candidato_1 = 0
# total_votos_candidato_2 = 0
# total_votos_candidato_3 = 0
# total_votos_candidato_4 = 0
#
# porcentagem_votos_brancos_candidato_1 = 0.0
# porcentagem_votos_brancos_candidato_2 = 0.0
# porcentagem_votos_brancos_candidato_3 = 0.0
# porcentagem_votos_brancos_candidato_4 = 0.0
#
# porcentagem_votos_nulos_candidatos_1 = 0.0
# porcentagem_votos_nulos_candidatos_2 = 0.0
# porcentagem_votos_nulos_candidatos_3 = 0.0
# porcentagem_votos_nulos_candidatos_4 = 0.0
#
# for i in range(1, 21):
#     opcao_candidato = int(input("\nEm qual candidato deseja votar? "))
#
#     if opcao_candidato == 1:
#         print("\nDigite 1 para votar no candidato 1")
#         print("Digite 5 para votar nulo no candidato 1")
#         print("Digite 6 para votar em branco no candidato 1")
#         opcao_voto = int(input("Digite aqui o seu voto: "))
#
#         if opcao_voto == 1:
#             qtd_votos_candidato_1 += 1
#         elif opcao_voto == 5:
#             qtd_votos_branco_candidato_1 += 1
#         elif opcao_voto == 6:
#             qtd_votos_nulo_candidato_1 += 1
#         else:
#             opcao_voto = int(input("Opção inválida, informe novamente seu voto:"))
#
#         total_votos_candidato_1 += 1
#
#         porcentagem_votos_brancos_candidato_1 = qtd_votos_branco_candidato_1/total_votos_candidato_1 * 100
#         porcentagem_votos_nulos_candidatos_1 = qtd_votos_nulo_candidato_1/total_votos_candidato_1 * 100
#
#     elif opcao_candidato == 2:
#         print("\nDigite 1 para votar no candidato 2")
#         print("Digite 5 para votar nulo no candidato 2")
#         print("Digite 6 para votar em branco no candidato 2")
#         opcao_voto = int(input("Digite aqui o seu voto: "))
#
#         if opcao_voto == 1:
#             qtd_votos_candidato_2 += 1
#         elif opcao_voto == 5:
#             qtd_votos_branco_candidato_2 += 1
#         elif opcao_voto == 6:
#             qtd_votos_nulo_candidato_2 += 1
#         else:
#             opcao_voto = int(input("Opção inválida, informe novamente seu voto:"))
#
#         total_votos_candidato_2 += 1
#
#         porcentagem_votos_brancos_candidato_2 = qtd_votos_branco_candidato_2/total_votos_candidato_2 * 100
#         porcentagem_votos_nulos_candidatos_2 = qtd_votos_nulo_candidato_2/total_votos_candidato_2 * 100
#
#     elif opcao_candidato == 3:
#         print("\nDigite 1 para votar no candidato 3")
#         print("Digite 5 para votar nulo no candidato 3")
#         print("Digite 6 para votar em branco no candidato 3")
#         opcao_voto = int(input("Digite aqui o seu voto: "))
#
#         if opcao_voto == 1:
#             qtd_votos_candidato_3 += 1
#         elif opcao_voto == 5:
#             qtd_votos_branco_candidato_3 += 1
#         elif opcao_voto == 6:
#             qtd_votos_nulo_candidato_3 += 1
#         else:
#             opcao_voto = int(input("Opção inválida, informe novamente seu voto:"))
#
#         total_votos_candidato_3 += 1
#
#         porcentagem_votos_brancos_candidato_3 = qtd_votos_branco_candidato_3/total_votos_candidato_3 * 100
#         porcentagem_votos_nulos_candidatos_3 = qtd_votos_nulo_candidato_3/total_votos_candidato_3 * 100
#
#     elif opcao_candidato == 4:
#         print("\nDigite 1 para votar no candidato 4")
#         print("Digite 5 para votar nulo no candidato 4")
#         print("Digite 6 para votar em branco no candidato 4")
#         opcao_voto = int(input("Digite aqui o seu voto: "))
#
#         if opcao_voto == 1:
#             qtd_votos_candidato_4 += 1
#         elif opcao_voto == 5:
#             qtd_votos_branco_candidato_4 += 1
#         elif opcao_voto == 6:
#             qtd_votos_nulo_candidato_4 += 1
#         else:
#             opcao_voto = int(input("Opção inválida, informe novamente seu voto: "))
#
#         total_votos_candidato_4 += 1
#
#         porcentagem_votos_brancos_candidato_4 = qtd_votos_branco_candidato_4/total_votos_candidato_4 * 100
#         porcentagem_votos_nulos_candidatos_4 = qtd_votos_branco_candidato_4/total_votos_candidato_4 * 100
#
#     else:
#         print("Opção inválida!")
#         opcao_voto = int(input("Em qual candidato deseja votar? "))
#
# print(f"\nTotal votos candidato 1: {total_votos_candidato_1}")
# print(f"Qtd votos candidato 1: {qtd_votos_candidato_1}")
# print(f"Qtd votos nulo candidato 1: {qtd_votos_nulo_candidato_1}")
# print(f"Qtd votos branco candidato 1: {qtd_votos_branco_candidato_1}")
# print(f"Porcentagem votos brancos candidato 1: {porcentagem_votos_brancos_candidato_1:.2f}%")
# print(f"Porcentagem votos nulos candidato 1: {porcentagem_votos_nulos_candidatos_1:.2f}%")
#
# print(f"\nQtd votos candidato 2: {total_votos_candidato_2}")
# print(f"Qtd votos candidato 2: {qtd_votos_candidato_2}")
# print(f"Qtd votos nulo candidato 2: {qtd_votos_nulo_candidato_2}")
# print(f"Qtd votos branco candidato 2: {qtd_votos_branco_candidato_2}")
# print(f"Porcentagem votos brancos candidato 2: {porcentagem_votos_brancos_candidato_2:.2f}%")
# print(f"Porcentagem votos nulos candidato 2: {porcentagem_votos_nulos_candidatos_2:.2f}%")
#
# print(f"\nQtd votos candidato 3: {total_votos_candidato_3}")
# print(f"Qtd votos candidato 3: {qtd_votos_candidato_3}")
# print(f"Qtd votos nulo candidato 3: {qtd_votos_nulo_candidato_3}")
# print(f"Qtd votos branco candidato 3: {qtd_votos_branco_candidato_3}")
# print(f"Porcentagem votos brancos candidato 3: {porcentagem_votos_brancos_candidato_3:.2f}%")
# print(f"Porcentagem votos nulos candidato 3: {porcentagem_votos_nulos_candidatos_3:.2f}%")
#
# print(f"\nQtd votos candidato 4: {total_votos_candidato_4}")
# print(f"Qtd votos candidato 4: {qtd_votos_candidato_4}")
# print(f"Qtd votos nulo candidato 4: {qtd_votos_nulo_candidato_4}")
# print(f"Qtd votos branco candidato 4: {qtd_votos_branco_candidato_4}")
# print(f"Porcentagem votos brancos candidato 4: {porcentagem_votos_brancos_candidato_4:.2f}%")
# print(f"Porcentagem votos nulos candidato 4: {porcentagem_votos_nulos_candidatos_4:.2f}%")
