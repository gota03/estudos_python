# def media(lista: list) -> tuple[float, str]:
#     media = sum(lista) / len(lista)
#     if media >= 6.0:
#         situacao = 'Aprovado'
#     else:
#         situacao = 'Reprovado'
#
#     return (media, situacao)
#
#
# media, situacao = media([8.5, 7.0])
# print(f'Média: {media}\nSituação: {situacao}')

#A função lambda é uma forma de criar uma função anônima, ou seja, uma função sem nome.
# Ela é definida usando a palavra-chave "lambda" seguida de uma ou mais variáveis, dois-pontos e a
# expressão que a função deve retornar. Essa função lambda pode ser atribuída a uma variável e usada como
# qualquer outra função.

#lambda <parametros>: <corpo da função>

media = lambda nota_1, nota_2: (nota_1 + nota_2) / 2
print(media(8.0, 7.5))

# A função map() aplica uma determinada função a cada elemento de um iterável (como uma lista, tupla, etc.)
# Quando usamos a função map() em conjunto com uma função lambda, podemos aplicar essa função lambda a cada elemento do iterável
#OBS: retorna um objeto map que precisa ser convertido em uma lista, tupla ou outro tipo de coleção para visualizar os resultados.

#map(<função>, <estrutura iterável>)

notas = [8.0, 7.5, 9.0, 6.5]
qualitativo = 0.5

notas_atualizada = map(lambda lista: lista + qualitativo, notas)
notas_atualizada = list(notas_atualizada)
print(notas_atualizada)
