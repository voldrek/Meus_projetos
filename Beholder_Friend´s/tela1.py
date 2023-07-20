from tkinter import *
from tkinter import messagebox
import pyodbc

#conexão com banco de dados 
server = 'DESKTOP-04O4S90'
database = 'BD_BF'
trusted_connection = 'yes'  # Indica o uso da autenticação do Windows
# cores-----------------
co0 = '#f0f3f5' #preto
co1 = '#feffff' #branco
co2 = '#3fb5a3' #verde
co3 = '#38576b' #valor
co4 = '#403d3d' #letra

#Funções
login = Tk()

def tela_cadastro():
    def cadastrar():
        nome = e_nome.get()
        senha = e_pass.get()
        email = e_email.get()

        # Realizar a conexão com o SQL Server
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-04O4S90;DATABASE=BD_BF;Trusted_Connection=yes')
        cursor = conn.cursor()

        # Inserir novo registro na tabela "Usuarios"
        query = "INSERT INTO Usuarios (Nome, Senha, Email) VALUES (?, ?, ?)"
        cursor.execute(query, nome, senha, email)

        # Confirmar a transação e fechar a conexão
        conn.commit()
        conn.close()

        # Limpar os campos de entrada após o cadastro
        e_nome.delete(0, END)
        e_pass.delete(0, END)
        e_email.delete(0, END)

    def voltar():
        apagar_tela()
        tela_login()

    def apagar_tela():
        for widget in frame_cima.winfo_children():
            widget.destroy()
                        
        for widget in frame_baixo.winfo_children():
            widget.destroy()


    #Diâmetro e posicionamento da tela        
    login.geometry("310x300")
    login.resizable(width=False, height=False)
    login.title("Cadastro de Pessoas")
    #Dividindo a tela
    frame_cima = Frame(login,width=310 , height=50, bg=co1 , relief='flat')
    frame_cima.grid(row=0 ,column=0,pady=1,padx=0,sticky=NSEW)
    frame_baixo = Frame(login,width=310 , height=250, bg=co1 , relief='flat')
    frame_baixo.grid(row=1 ,column=0,pady=1,padx=0,sticky=NSEW)

    #Configurando frame_cima
    l_nome = Label(frame_cima, text='Cadastro' , anchor=NE , font=('Ivy 25') ,bg=co1 , fg=co4)
    l_nome.place(x=5 , y=5)
    l_linha = Label(frame_cima, text='' ,width=275, anchor=NW , font=('Ivy 1') ,bg=co2 , fg=co4)
    l_linha.place(x=10 , y=45)

    #configurando frame baixo
    #label nome
    l_nome = Label(frame_baixo, text='Nome *' , anchor=NW , font=('Ivy 10') ,bg=co1 , fg=co4)
    l_nome.place(x=10 , y=15)
    e_nome = Entry(frame_baixo, width=25, justify='left', font=('', 15), highlightthickness=1, relief=SOLID)
    e_nome.place (x=14, y=35)
    #label senha
    l_pass = Label(frame_baixo, text='Senha *' , anchor=NW , font=('Ivy 10') ,bg=co1 , fg=co4)
    l_pass.place(x=10 , y=65)
    e_pass = Entry(frame_baixo, width=25, justify='left',show='*', font=('', 15), highlightthickness=1, relief='solid')
    e_pass.place (x=14, y=85)
    #label email
    l_email = Label(frame_baixo, text='E-mail *' , anchor=NW , font=('Ivy 10') ,bg=co1 , fg=co4)
    l_email.place(x=10 , y=120)
    e_email = Entry(frame_baixo, width=25, justify='left', font=('', 15), highlightthickness=1, relief=SOLID)
    e_email.place (x=14, y=140)


    b_cadastrar = Button(frame_baixo,command=cadastrar,text='cadastrar' ,width=10,height=2, anchor=NW , font=('Ivy 8 bold') ,bg=co2 , fg=co1, relief=RAISED, overrelief=RIDGE)
    b_cadastrar.place(x=200 , y=190)

    b_voltar = Button(frame_baixo,command=voltar, text='Voltar' ,width=10,height=2, anchor=NW , font=('Ivy 8 bold') ,bg=co2 , fg=co1, relief=RAISED, overrelief=RIDGE)
    b_voltar.place(x=10 , y=190)
def tela_login():
    def verifica_senha():
        nome = e_nome.get()
        senha = e_pass.get()

        # Realizar a conexão com o SQL Server
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-04O4S90;DATABASE=BD_BF;Trusted_Connection=yes')
        cursor = conn.cursor()

        # Executar a consulta para verificar o nome de usuário e a senha
        query = "SELECT * FROM Usuarios WHERE Nome = ? AND Senha = ?"
        cursor.execute(query, nome, senha)
        result = cursor.fetchone()

        if result:
            nome_usuario = result.Nome  # Obtém o nome do usuário autenticado
            messagebox.showinfo('Login', 'Seja bem-vindo, ' + str(nome_usuario))
            tela_prinpal(nome_usuario)
            
        else:
            messagebox.showwarning('Erro', 'Verifique a senha')      
    def center():
        altura = 310
        largura = 300
        # resolução do sistema
        larguraScreen = login.winfo_screenwidth()
        alturaScreen = login.winfo_screenheight()
        # posição da janela
        posx = larguraScreen/2 - largura/2
        posy = alturaScreen/2 - altura/2

        # definindo a geometry
        login.geometry(f'{largura}x{altura}+{int(posx)}+{int(posy)}')
    
    center()
    login.resizable(width=False , height=False)
    login.configure(background = co1)
    login.title('Login')

    #Dividindo tela
    frame_cima = Frame(login,width=310 , height=50, bg=co1 , relief='flat')
    frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
    frame_baixo = Frame(login,width=310 , height=250, bg=co1 , relief='flat')
    frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    #configurando frame_cima
    l_nome = Label(frame_cima, text='LOGIN' , anchor=NE , font=('Ivy 25') ,bg=co1 , fg=co4)
    l_nome.place(x=5 , y=5)
    l_linha = Label(frame_cima, text='' ,width=275, anchor=NW , font=('Ivy 1') ,bg=co2 , fg=co4)
    l_linha.place(x=10 , y=45)

    #configurando frame baixo
    l_nome = Label(frame_baixo, text='Nome *' , anchor=NW , font=('Ivy 10') ,bg=co1 , fg=co4)
    l_nome.place(x=10 , y=20)
    e_nome = Entry(frame_baixo, width=25, justify='left', font=('', 15), highlightthickness=1, relief=SOLID)
    e_nome.place (x=14, y=50)

    #senha
    l_pass = Label(frame_baixo, text='Senha *' , anchor=NW , font=('Ivy 10') ,bg=co1 , fg=co4)
    l_pass.place(x=10 , y=95)
    e_pass = Entry(frame_baixo, width=25, justify='left',show='*', font=('', 15), highlightthickness=1, relief='solid')
    e_pass.place (x=14, y=130)

    b_confirmar = Button(frame_baixo,command=verifica_senha, text='Entrar' ,width=10,height=2, anchor=NW , font=('Ivy 8 bold') ,bg=co2 , fg=co1, relief=RAISED, overrelief=RIDGE)
    b_confirmar.place(x=15 , y=180)

    b_cadastro = Button(frame_baixo,command=tela_cadastro, text='Cadastro' ,width=10,height=2, anchor=NW , font=('Ivy 8 bold') ,bg=co2 , fg=co1, relief=RAISED, overrelief=RIDGE)
    b_cadastro.place(x=200 , y=180)
def tela_prinpal(nome_usuario):
    login.geometry('500x300')
    login.resizable(width=False, height=False)
    login.configure(background=co1)

    #Dividindo tela
    frame_cima = Frame(login, width=310 , height=50, bg=co1, relief='flat')
    frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
    frame_baixo = Frame(login, width=500 , height=250, bg=co1, relief='flat')
    frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    #configurando frame_cima
    l_nome = Label(frame_cima, text=nome_usuario, anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
    l_nome.place(x=5, y=5)
    l_linha = Label(frame_cima, text='', width=470, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
    l_linha.place(x=10, y=45)

    #configurando frame baixo
    lista_personagens = Listbox(frame_baixo, width=30, height=14)
    lista_personagens.place(x=310,y=15)

    
    
    #Botões do aplicativo
    b_createCharacter = Button(frame_baixo, text='Criar\nPersonagem' ,width=10,height=2, anchor=NW , font=('Ivy 8 bold') ,bg=co2 , fg=co1, relief=RAISED, overrelief=RIDGE)
    b_createCharacter.place(x=10 , y=20)

    b_diceRoll = Button(frame_baixo, text='Rolagem de\nDados' ,width=10,height=2, anchor=NW , font=('Ivy 8 bold') ,bg=co2 , fg=co1, relief=RAISED, overrelief=RIDGE)
    b_diceRoll.place(x=100 , y=20)

    b_myCharacter = Button(frame_baixo, text='Meus\nPersonagens' ,width=10,height=2, anchor=NW , font=('Ivy 8 bold') ,bg=co2 , fg=co1, relief=RAISED, overrelief=RIDGE)
    b_myCharacter.place(x=10 , y=70)

tela_login()

login.mainloop()