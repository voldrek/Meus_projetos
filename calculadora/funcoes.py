from tkinter import *
#Cores básicas:

#"white" (branco)
#"black" (preto)
#"red" (vermelho)
#"green" (verde)
#"blue" (azul)
#"yellow" (amarelo)
#'purple" (roxo)
#"orange" (laranja)
#"gray" (cinza)
#"pink" (rosa)
#"brown" (marrom)
#Cores adicionais:

#"cyan" (ciano)
#"magenta" (magenta)
#"lightblue" (azul claro)
#"lightgreen" (verde claro)
#"lightyellow" (amarelo claro)
#"lightgray" (cinza claro)

def centralizar(altura,largura,titulo,cor):
        janela = Tk()
        titulo = janela.title(titulo)
        janela.resizable(width=False,height=False)
        janela.configure(background=cor)
        # resolução do sistema
        larguraScreen = janela.winfo_screenwidth()
        alturaScreen = janela.winfo_screenheight()
        # posição da janela
        posx = larguraScreen/2 - largura/2
        posy = alturaScreen/2 - altura/2

        # definindo a geometry
        janela.geometry(f'{largura}x{altura}+{int(posx)}+{int(posy)}')

        return janela

def criarBotao(frame, texto, valor, altura, largura, corFundo, corLetra, posX, posY, label_resultado):
    def botaoClicado():
        label_resultado.config(text=label_resultado["text"] + valor)

    botao = Button(frame, text=texto, width=altura, height=largura, font=('Ivy 8 bold'), bg=corFundo, fg=corLetra,command=botaoClicado)
    botao.place(x=posX, y=posY)

def criarLabel(frame, texto, corFundo, corLetra, posX, posY):
    label = Label(frame, text=texto ,font=('Ivy 12 bold'), bg=corFundo, fg=corLetra)
    label.place(x=posX, y=posY)
    return label



#def calc():
    