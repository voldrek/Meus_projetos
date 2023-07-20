import pyodbc
from tkinter import *
from tkinter import ttk
import pandas as pd
from tkinter import messagebox

server = 'DESKTOP-04O4S90'
database = 'BD_BF'
trusted_connection = 'yes'  # Indica o uso da autenticação do Windows


# cores-----------------
co0 = '#f0f3f5' #preto
co1 = '#feffff' #branco
co2 = '#3fb5a3' #verde
co3 = '#38576b' #valor
co4 = '#403d3d' #letra
#funções
login = Tk()



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
        #tela_login()

def apagar_tela():
        for widget in frame_cima.winfo_children():
            widget.destroy()
                        
        for widget in frame_baixo.winfo_children():
            widget.destroy()

login = Tk()
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

login.mainloop()