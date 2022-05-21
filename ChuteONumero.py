# Escreva um programa que, ao inicaiar gera um valor aleatório de 1 a 10 e permite que o usuário chute um número até que o valor aleatório gerado no início do programa seja chutado
# (corretamente)
#
# O program deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início no
# inicio do programa.
#
# #método 5Q's para montar um algoritmo:
#
# Analise criticamente o problema e descubra:
# (Tente explicar este problema para você mesmo em voz alta e peça mais informações/ investigue maiis até você compreender completamente o problema)
#
# 1.quais são os dados de entrada necessários ?
#-Valor aleat´rio de 1 a 10
#-chtu do usuaário

# 2.O que devo fazer com estes dados ?
#-eu devo comparar o chut do usuario com o valor aleatorio que foi gerado no inicio do programa e dizer se o chute foi maior, menor ou igual ao valor que foi gerado no inicio do programa

# 3.quais são as restrições deste problema ?
#-Um valor aleatório de 1 a 10

# 4,.Qual é o resultado esperado ?
#- O resultado esperado é que o programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatorio gerado no inicio do programa.

# 5. Qual é sequencia de passos a ser feitas para chegar ao resultado esperado ?
# input valor_aleatorio de 1 a 10
# input chute
# if   chute >valor_aleatorio
#     print "Chute foi maior que o valor gerado"
#     if chute < valor_aleatorio
#         print "chute  foi meno que o valor gerado"
#     if chute = valor_aleatorio
#     print "voce acerto !"


import random

valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
    chute = int(input('Chute um valor de 1 a 10 '))
    if chute > valor_aleatorio:
        print('Chute foi maior que o valor gerado ')
    elif chute < valor_aleatorio:
        print('chute  foi menor que o valor gerado ')
    elif chute == valor_aleatorio:
        acertou = True
        print('Voce acertou!')
