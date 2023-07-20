from googlesearch import search
from tkinter import *
import webbrowser


window = Tk()

def pesquisarNoGoogle():
    resultadoDaPesquisa = entryPesquisar.get()

    # Realiza a pesquisa no Google
    resultados = search(resultadoDaPesquisa, num_results=1, lang='pt-br')

    # Retorna o primeiro link encontrado
    for link in resultados:
        labelResultado.config(text=link, fg="blue", cursor="hand2")
        labelResultado.bind("<Button-1>", lambda e: webbrowser.open(link))


def center():
    altura = 400
    largura = 400
    # resolução do sistema
    larguraScreen = window.winfo_screenwidth()
    alturaScreen = window.winfo_screenheight()
    # posição da janela
    posx = larguraScreen/2 - largura/2
    posy = alturaScreen/2 - altura/2

    # definindo a geometry
    window.geometry(f'{largura}x{altura}+{int(posx)}+{int(posy)}')

center()
window.title('Pesquisa link')
window.resizable(width=False,height=False)

entryPesquisar = Entry(window,width=10, justify='left', font=('', 15), highlightthickness=1, relief=SOLID)
entryPesquisar.place(x=130, y=150)

botaoPesquisar = Button(window,command=pesquisarNoGoogle, text='Pesquisar' ,width=10,height=2, anchor=NW , font=('Ivy 8 bold') , relief=RAISED, overrelief=RIDGE)
botaoPesquisar.place(x=150 , y=190)

labelResultado = Label(window, text=f'' , anchor=NW , font=('Ivy 10'))
labelResultado.place(x=110 , y=120)



window.mainloop()

