#Crie um programa que receber um numero e imprime o fatorial daquele número.

#Método 5Q's para montar um algoritmo:
#Analise criticamente o problema e descubra:
#(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais ate voce compreender completamente o problema.)

#1.quais são os dados de entrada necessarios ?
#2.o que devo fazer com estes dados ?
#R: eu devo calcular o fatorial do número que for passado para o meu programa e o exibir na tela.
#3.quais são as restrições deste problema?
#R:O numero deve ser um valor positivo
#O numero deve ser um valor inteiro
#4.qual é o resultado esperado?
#R:O resultado esperado é que o fatorial do núemro providenciado seja exibido.
#5.qual é sequência de passos a ser feitas para chegar ao resultado esperado ?
#R.
#
# if numero >0
# if numero = inteiro
# fatorial = 1
# loop de 1 a numero
# fatorial = fatorial * numero
# print(fatorial)


numero = int(input('Digite um numero '))
if numero > 0:
    fatorial = 1
    for item in range(1,numero +1):
        fatorial = fatorial * item
        print(fatorial)