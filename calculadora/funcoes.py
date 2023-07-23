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

#Fontes padrão:

#"TkDefaultFont" (fonte padrão do Tkinter)
#"Helvetica" (ou "TkTextFont" ou "TkFixedFont" dependendo do sistema)
#Fontes serif:

#"Times" ou "Times New Roman" (fonte serif padrão)
#"Courier" (fonte monoespaçada serif)
#"Georgia"
#Fontes sem serifa (sans-serif):

#"Arial" (ou "Helvetica" em alguns sistemas)
#"Verdana"
#"Tahoma"
#Fontes monoespaçadas:

#"Courier" (ou "Courier New" em alguns sistemas)
#"Fixedsys" (fonte monoespaçada padrão no Windows)
#Fontes cursive (manuscritas) e fantasy (fantasia):

#"Comic Sans MS"
#"Zapfino" (somente em sistemas macOS)

#Fontes adicionais:

#"Lucida" (por exemplo, "Lucida Grande", "Lucida Sans Unicode")
#"Century Schoolbook"
#"Bookman"
#"Palatino"
#"URW Chancery L"
#"URW Gothic L"
#"URW Palladio L"

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
    