# # Projeto medidor de velocidade
# #
# # Levando em cosideração a velocidade maxima permitida 980 km em uma determinda rua. crie um programa que recebe do usuaririo um valor que representa a velocidade e com base nessa velocidade diga se ele tomou um multa leve,
#
# input velocidade
# velocidade_maxima = 80
# if velocidade <= valocidade_maxima:
#     print'Voce não levou multa'
#     if velocidade > velocidade_maxima e velocidade <= velociade_maxima + 10:
#         print 'voce levou multa leve'
#
#         if velocidade_maxima > velocidade_maxima +11 e velocidade <= velocidade_maxima +20:
#             print 'levo multa grave'
#             if velocidade > velocidade_maxima +20:
#                 print 'levou multa gravissima'

velocidade = int(input('Digite sua velocidade '))
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
    print('Não levoou multa ')
elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima +10:
    print('Levou multa leve ')
elif velocidade >= velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
    print('Leveol multa grave')
elif velocidade > velocidade_maxima + 20:
    print('Levou multa gravíssima')