#Condicionais
#if, elif e else

#E ae jhonathan, bora dar uma saida hoje .?
#Se eu terminar meu trabalho aqui, eu consigo.

trabalho_terminado = True
if trabalho_terminado == True:
    print('Opa! Bora dar uma saída')
else:
    print('Não posso sair agora')

#Ei, você consegue me ajudar a mover essas caixas lá para fora hoje a tarde ?
#Se eu estiver livre, sim. mas, se não der pede meu irmão para te ajudar

estou_livre = False
if estou_livre == True:
    print('Ok, posso ajudar hoje sim!')
else:
    print('Peça para meu irmão para te ajudar')

#Condicionais ainda

#Eu chequei atrasado na aula, ainda posso entrar.?
#Se essa não for sua terceira vez chegando atrasado, então pode sim, caso contrário irá tomar uma suspensão.

numero_de_atrasos = 3
if numero_de_atrasos >= 3:
    print('Você está suspenso')
elif numero_de_atrasos == 1:
    print('Pode entrar, porém caso tome mais 2 faltas, irá ser suspenso')
elif numero_de_atrasos ==2:
    print('Pode entrar, porám  caso toma mais 1 falta, irár ser suspenso')
else:
    print('Pode entrar')