print("oi")
#1)
#gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
# print(f"Média: {sum(gastos)}")
#print(f"Quantidade: {len(gastos)}")

#2)
# cont = 0
# percentual = 0.0
# gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
# for i in gastos:
#     if i > 3000.00:
#         cont += 1
#         percentual = (cont/len(gastos)) * 100
#
# print(f"Compras maiores que R$3000.00{cont}")
# print(f"Percentual : {percentual:.2f}%")

#3)
# lista = []
# for i in range(1, 6):
#
#     num = int(input("informe um número inteiro: "))
#     lista.append(num)
#
# print(lista)

#4)
# lista = []
# for i in range(1, 6):
#     num = int(input("informe um número: "))
#     lista.append(num)
#
# lista.sort(reverse=True)
# print(lista)

#5)
# lista_numeros_primos = []
#
# num = int(input("informe um número: "))
# for i in range(1, num):
#     if i % 2 == 1:
#         lista_numeros_primos.append(i)
#
# print(lista_numeros_primos)

#6)
# data_valida = input("informe uma data: ")
# if len(data_valida) == 10 or len(data_valida) == 8:
#     print("data valida")
# else:
#     print("data invalida")

#7)
# num_bacterias_dia = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
# percentual_crescimento = 0.0
# 100 * (amostra_atual - amostra_passada) / (amostra_passada)
#
# for i in range(1, len(num_bacterias_dia)):
#     percentual_crescimento = 100 * (num_bacterias_dia[i] - num_bacterias_dia[i -1]) /(num_bacterias_dia[i] -1)
#
# print(f"Porcentagem de crescimento: {percentual_crescimento:.2f}%")

#8)
# qtd_produtos_doces = 0
# qtd_produtos_amargos = 0
# for i in range(1, 11):
#     id = int(input("informe um id: "))
#     if id % 2 == 0:
#         qtd_produtos_doces += 1
#     else:
#         qtd_produtos_amargos += 1
#
# print(f"Quantidade produtos doces: {qtd_produtos_doces}")
# print(f"Quantidade produtos amargos: {qtd_produtos_amargos}")

#9)
# gabarito_prova = {
#     1: 'D',
#     2: "A",
#     3: "C",
#     4: "B",
#     5: "A",
#     6: "D",
#     7: "C",
#     8: "C",
#     9: "A",
#     10: "B"
# }
#
# pontuacao = 0
# for i in range(1, 11):
#     resposta_aluno = input(f"informe sua resposta para a questão {i}º: ")
#     if resposta_aluno in gabarito_prova[i]:
#         print(gabarito_prova[i])
#         pontuacao += 1
#
# print(f"Nota: {pontuacao}")

#10)
# lista_meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
# lista_temperatura_media = []
#
# for i in range(0, 12):
#     temperatura_media = float(input(f"informe a temperatura média do mês {lista_meses[i]}: "))
#     lista_temperatura_media.append(temperatura_media)
#
# media_anual = sum(lista_temperatura_media)/len(lista_temperatura_media)
# print(f"A média anual foi: {media_anual:.2f}")
#
# for i in range(len(lista_temperatura_media)):
#     if lista_temperatura_media[i] > media_anual:
#         print(f"{lista_meses[i]}: {lista_temperatura_media[i]:.2f}")

#11)
# vendas_produto = {
#     'Produto A': 300,
#     'Produto B': 80,
#     'Produto C': 60,
#     'Produto D': 200,
#     'Produto E': 250,
#     'Produto F': 30
# }
# total_produtos = 0
# produto_mais_vendido = vendas_produto.get("Produto B")
#
# for i in vendas_produto:
#     total_produtos += vendas_produto[i]
#     if vendas_produto[i] > produto_mais_vendido:
#         produto_mais_vendido = vendas_produto[i]
#
# print(f"Total de produtos: {total_produtos}")
# print(f"Produto mais vendido: {produto_mais_vendido}")

#12)
# votos_marcas = {
#     "Design 1": 1334,
#     "Design 2": 982,
#     "Design 3": 1751,
#     "Design 4": 210,
#     "Design 5": 1811
# }
# design_vencedor = votos_marcas.get("Design 4")
# qtd_votos = 0
#
# for i in votos_marcas:
#     qtd_votos += votos_marcas[i]
#     if votos_marcas[i] > design_vencedor:
#         design_vencedor = votos_marcas[i]
#
# porcentagem = design_vencedor/qtd_votos * 100
# print(f"Design vencedor: {design_vencedor}")
# print(f"Porcentagem de votos: {porcentagem:.2f}%")

#13)
# salarios_receber_abono = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
# porcentagem_abono = 0.1
# salario_com_abono = []
# salarios_dict = {}
# total_gastos_abono = 0.0
# abono_minimo = 200.0
# qtd_abono_minimo = 0
#
# for i in range(len(salarios_receber_abono)):
#     salario_com_abono.append(salarios_receber_abono[i] * porcentagem_abono)
#     if salario_com_abono[i] < 200:
#         salario_com_abono[i] = 200
#     salarios_dict[salarios_receber_abono[i]] = salario_com_abono[i]
#
# total_gastos_abono = sum(salario_com_abono)
# maior_abono = salarios_dict.get(1172)
# for i in salarios_dict:
#     if salarios_dict[i] == 200:
#         qtd_abono_minimo += 1
#     if salarios_dict[i] > maior_abono:
#         maior_abono = salarios_dict[i]
#
# print(f"Total gasto com abono: {total_gastos_abono}")
# print(f"Quantidade abono minimo: {qtd_abono_minimo}")
# print(f"Maior abono: {maior_abono:.2f}")

#14)
# especies = {'Área Norte': [2819, 7236],
#             'Área Leste': [1440, 9492],
#             'Área Sul': [5969, 7496],
#             'Área Oeste': [14446, 49688],
#             'Área Centro': [22558, 45148]
#             }
# media_especies = 0.0
# for i in especies.items():
#     media_especies = sum(i[1])/len(i[1])
#     print(f"{i[0]}: {media_especies}")

#15)
# idades_por_setor = {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
#                     'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
#                     'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
#                     'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]
#                     }
#
# media_idade_geral = 0.0
# pessoas_acima_idade_geral = 0
#
# for i in idades_por_setor:
#
#     media_idade_setor = sum(idades_por_setor[i])/len(idades_por_setor[i])
#     print(f"{i}: {media_idade_setor}")
#     media_idade_geral = sum(idades_por_setor[i])/len(i)
#
#     for j in idades_por_setor[i]:
#
#         if j > media_idade_geral:
#             pessoas_acima_idade_geral += 1
#
# print(f"\nMédia idade geral: {media_idade_geral:.2f} anos")
# print(f"Quantidade de pessoas acima da média geral de idades: {pessoas_acima_idade_geral}")
