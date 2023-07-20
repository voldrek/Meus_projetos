from tkinter import *
# cores-----------------
co0 = '#f0f3f5' #preto
co1 = '#feffff' #branco
co2 = '#3fb5a3' #verde
co3 = '#38576b' #valor
co4 = '#403d3d' #letra

login = Tk()
def center():
    altura = 600
    largura = 400
    # resolução do sistema
    larguraScreen = login.winfo_screenwidth()
    alturaScreen = login.winfo_screenheight()
    # posição da janela
    posx = larguraScreen/2 - largura/2
    posy = alturaScreen/2 - altura/2
    # definindo a geometry
    login.geometry(f'{largura}x{altura}+{int(posx)}+{int(posy)}')

center()
login.resizable(width=False,height=False)
login.configure(background=co1)
login.title('Ficha de Personagem')

frame_cima = Frame(login,width=400 , height=50, bg=co1 , relief='flat')
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
frame_baixo = Frame(login,width=400, height=600, bg=co1 , relief='flat')
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

#l_nome = Label(frame_cima, text=nome_usuario, anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
#l_nome.place(x=5, y=5)
l_linha = Label(frame_cima, text='', width=470, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
l_linha.place(x=10, y=45)

#Entry e label nome do personagem
labelNameCharacter = Label(frame_baixo, text='Nome' , anchor=NW , font=('Ivy 10') ,bg=co1 , fg=co4)
labelNameCharacter.place(x=10 , y=10)
entryNameCharacter = Entry(frame_baixo, width=15, justify='left', font=('', 10), highlightthickness=1, relief=SOLID)
entryNameCharacter.place(x=12, y=30)

#Entry e label nome do jogador
labelNameCharacter = Label(frame_baixo, text='Jogador' , anchor=NW , font=('Ivy 10') ,bg=co1 , fg=co4)
labelNameCharacter.place(x=130 , y=10)
entryNameCharacter = Entry(frame_baixo, width=15, justify='left', font=('', 10), highlightthickness=1, relief=SOLID)
entryNameCharacter.place(x=132, y=30)

#Entry e label Raça,Nivel,Classe e divindade
labelClass = Label(frame_baixo, text='Classe' , anchor=NW , font=('Ivy 10') ,bg=co1 , fg=co4)
labelClass.place(x=250, y=10)
entryClass = Entry(frame_baixo, width=10, justify='left', font=('', 10), highlightthickness=1, relief=SOLID)
entryClass.place(x=252, y=30)

labelLevel = Label(frame_baixo, text='Nivel' , anchor=NW , font=('Ivy 10') ,bg=co1 , fg=co4)
labelLevel.place(x=330, y=10)
entryLevel = Entry(frame_baixo, width=8, justify='left', font=('', 10), highlightthickness=1, relief=SOLID)
entryLevel.place(x=332, y=30)

labelBreed = Label(frame_baixo, text='Raça' , anchor=NW , font=('Ivy 10') ,bg=co1 , fg=co4)
labelBreed.place(x=10 , y=55)
entryBreed = Entry(frame_baixo, width=15, justify='left', font=('', 10), highlightthickness=1, relief=SOLID)
entryBreed.place(x=12, y=75)

labelBreed = Label(frame_baixo, text='Origem' , anchor=NW , font=('Ivy 10') ,bg=co1 , fg=co4)
labelBreed.place(x=130 , y=55)
entryBreed = Entry(frame_baixo, width=15, justify='left', font=('', 10), highlightthickness=1, relief=SOLID)
entryBreed.place(x=132, y=75)

#Entry e label Vida e Mana
labelLife = Label(frame_baixo, text='Vida' , anchor=NW , font=('Ivy 10') ,bg=co1 , fg=co4)
labelLife.place(x=250 , y=55)
entryLife = Entry(frame_baixo, width=10, justify='left', font=('', 10), highlightthickness=1, relief=SOLID)
entryLife.place(x=252, y=75)

labelLevel = Label(frame_baixo, text='Mana ' , anchor=NW , font=('Ivy 10') ,bg=co1 , fg=co4)
labelLevel.place(x=330, y=55)
entryLevel = Entry(frame_baixo, width=8, justify='left', font=('', 10), highlightthickness=1, relief=SOLID)
entryLevel.place(x=332, y=75)

#Entry e Label do atributos base do personagem
labelStrength = Label(frame_baixo, text='Força' , anchor=NW , font=('Comic Sans MS', 10, 'bold') ,bg=co1 , fg=co4)
labelStrength.place(x=10, y=100)
entryStrength = Entry(frame_baixo, width=4, justify='left', font=('',15), highlightthickness=1, relief=SOLID)
entryStrength.place(x=12, y=123)
modifierLabelStrength = Label(frame_baixo,text='0', anchor=NW , font=('Ivy 10') ,bg=co1 , fg=co4)
modifierLabelStrength.place(x=45, y=150)

labelDexterity = Label(frame_baixo, text='Constit.' , anchor=NW , font=('Comic Sans MS', 10, 'bold') ,bg=co1 , fg=co4)
labelDexterity.place(x=70, y=100)
entryDexterity = Entry(frame_baixo, width=4, justify='left', font=('',15), highlightthickness=1, relief=SOLID)
entryDexterity.place(x=72, y=123)
modifierLabelDexterity = Label(frame_baixo,text='0', anchor=NW , font=('Ivy 10') ,bg=co1 , fg=co4)
modifierLabelDexterity.place(x=75, y=150)

labelConstitution = Label(frame_baixo, text='Intelig.' , anchor=NW , font=('Comic Sans MS', 10, 'bold') ,bg=co1 , fg=co4)
labelConstitution.place(x=10, y=170)
entryConstitution = Entry(frame_baixo, width=4, justify='left', font=('',15), highlightthickness=1, relief=SOLID)
entryConstitution.place(x=12, y=193)
modifierLabelConstitution = Label(frame_baixo,text='0', anchor=NW , font=('Ivy 10') ,bg=co1 , fg=co4)
modifierLabelConstitution.place(x=125, y=150)

labelintelligence = Label(frame_baixo, text='Destreza' , anchor=NW , font=('Comic Sans MS', 10, 'bold') ,bg=co1 , fg=co4)
labelintelligence.place(x=70, y=170)
entryintelligence = Entry(frame_baixo, width=4, justify='left', font=('',15), highlightthickness=1, relief=SOLID)
entryintelligence.place(x=72, y=193)
modifierLabelintelligence = Label(frame_baixo,text='0', anchor=NW , font=('Ivy 10') ,bg=co1 , fg=co4)
modifierLabelintelligence.place(x=175, y=150)

labelWisdom = Label(frame_baixo, text='Sabed.' , anchor=NW , font=('Comic Sans MS', 10, 'bold') ,bg=co1 , fg=co4)
labelWisdom.place(x=10, y=240)
entryWisdom = Entry(frame_baixo, width=4, justify='left', font=('',15), highlightthickness=1, relief=SOLID)
entryWisdom.place(x=12, y=263)
modifierLabelWisdom = Label(frame_baixo, text='0' , anchor=NW , font=('Ivy 10') ,bg=co1 , fg=co4)
modifierLabelWisdom.place(x=225, y=150)

labelCharisma = Label(frame_baixo, text='Carisma' , anchor=NW , font=('Comic Sans MS', 10, 'bold') ,bg=co1 , fg=co4)
labelCharisma.place(x=70, y=240)
entryCharisma = Entry(frame_baixo, width=4, justify='left', font=('',15), highlightthickness=1, relief=SOLID)
entryCharisma.place(x=72, y=263)
modifierLabelCharisma = Label(frame_baixo, text='0' , anchor=NW , font=('Ivy 10') ,bg=co1 , fg=co4)
modifierLabelCharisma.place(x=275, y=150)

#Calculo da defesa
labelDefense = Label(frame_baixo, text='Defesa' , anchor=NW , font=('Comic Sans MS', 10, 'bold') ,bg=co1 , fg=co4)
labelDefense.place(x=130, y=100)
entryDefense = Entry(frame_baixo, width=3, justify='left', font=('',15), highlightthickness=1, relief=SOLID)
entryDefense.place(x=130, y=123)
#Atributos
entryModDext = Entry(frame_baixo, width=2, justify='left', font=('',15), highlightthickness=1, relief=SOLID)
entryModDext.place(x=225, y=123)
labelSoma1 = Label(frame_baixo, text='+' , anchor=NW , font=('Comic Sans MS', 10, 'bold') ,bg=co1 , fg=co4)
labelSoma1.place(x=255, y=123)
entryBonusArmor = Entry(frame_baixo, width=2, justify='left', font=('',15), highlightthickness=1, relief=SOLID)
entryBonusArmor.place(x=270, y=123)
labelSoma2 = Label(frame_baixo, text='+' , anchor=NW , font=('Comic Sans MS', 10, 'bold') ,bg=co1 , fg=co4)
labelSoma2.place(x=300, y=123)
entryBonusShield = Entry(frame_baixo, width=2, justify='left', font=('',15), highlightthickness=1, relief=SOLID)
entryBonusShield.place(x=315, y=123)
labelSoma3 = Label(frame_baixo, text='+' , anchor=NW , font=('Comic Sans MS', 10, 'bold') ,bg=co1 , fg=co4)
labelSoma3.place(x=345, y=123)
entryOthers = Entry(frame_baixo, width=2, justify='left', font=('',15), highlightthickness=1, relief=SOLID)
entryOthers.place(x=360, y=123)
labelSoma4 = Label(frame_baixo, text='+' , anchor=NW , font=('Comic Sans MS', 10, 'bold') ,bg=co1 , fg=co4)
labelSoma4.place(x=210, y=123)
labelSoma4 = Label(frame_baixo, text='10' , anchor=NW , font=('Comic Sans MS', 10, 'bold') ,bg=co1 , fg=co4)
labelSoma4.place(x=190, y=123)
labelIgual = Label(frame_baixo, text='=' , anchor=NW , font=('Comic Sans MS', 10, 'bold') ,bg=co1 , fg=co4)
labelIgual.place(x=175, y=123)
login.mainloop()