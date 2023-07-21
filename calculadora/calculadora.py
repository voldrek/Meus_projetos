from tkinter import *
from funcoes import *

# cores-----------------
preto = '#f0f3f5' #preto
branco = '#feffff' #branco
verde = '#3fb5a3' #verde
valor = '#38576b' #valor
letra = '#403d3d' #letra
azul =  '#87CEFA'
azulGelo = '#F0F8FF'

janelaPrincipal = centralizar(500,300,'Calculadora',azulGelo)

labelResultado = criarLabel(janelaPrincipal,'','white','black',5,5)
#operadores
criarBotao(janelaPrincipal,'=','=',5,3,verde,preto,250,440,labelResultado)
criarBotao(janelaPrincipal,'+','+',5,3,verde,preto,250,380,labelResultado)
criarBotao(janelaPrincipal,'-','-',5,3,verde,preto,250,320,labelResultado)
criarBotao(janelaPrincipal,'X','X',5,3,verde,preto,250,260,labelResultado)
criarBotao(janelaPrincipal,'/','/',5,3,verde,preto,250,200,labelResultado)
criarBotao(janelaPrincipal,'+/-','+/-',5,3,verde,preto,100,440,labelResultado)
criarBotao(janelaPrincipal,',',',',5,3,verde,preto,200,440,labelResultado)
#Numeração
criarBotao(janelaPrincipal,'0','0',5,3,verde,preto,150,440,labelResultado)
criarBotao(janelaPrincipal,'1','1',5,3,verde,preto,200,380,labelResultado)
criarBotao(janelaPrincipal,'2','2',5,3,verde,preto,150,380,labelResultado)
criarBotao(janelaPrincipal,'3','3',5,3,verde,preto,100,380,labelResultado)
criarBotao(janelaPrincipal,'4','4',5,3,verde,preto,200,320,labelResultado)
criarBotao(janelaPrincipal,'5','5',5,3,verde,preto,150,320,labelResultado)
criarBotao(janelaPrincipal,'6','6',5,3,verde,preto,100,320,labelResultado)
criarBotao(janelaPrincipal,'7','7',5,3,verde,preto,200,260,labelResultado)
criarBotao(janelaPrincipal,'8','8',5,3,verde,preto,150,260,labelResultado)
criarBotao(janelaPrincipal,'9','9',5,3,verde,preto,100,260,labelResultado)
#Tela de digitar



janelaPrincipal.mainloop()