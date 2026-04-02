import tkinter as tk

from tkinter import font 
from funcoes import salvar_nome
import sqlite3


# ----FUNÇÕES------------#


def deleta_nome():
        selected_name = listbox.get(tk.ACTIVE) # Obtém o nome selecionado na caixa de listagem (listbox)
        conn = sqlite3.connect("Bancoteste.db") # Conecta ao banco de dados
        cursor = conn.cursor() # Cria um cursor para executar comandos SQL
        cursor.execute("DELETE FROM Bancoteste WHERE nome = ?", (selected_name,)) # Deleta o nome selecionado do banco de dados
        conn.commit() # Salva as alterações no banco de dados
        conn.close() # Fecha a conexão com o banco de dados
        listbox.delete(tk.ACTIVE) # Remove o nome da caixa de listagem (listbox)



def listar_nomes():
        conn = sqlite3.connect("Bancoteste.db") # Conecta ao banco de dados
        cursor = conn.cursor() # Cria um cursor para executar comandos SQL
        cursor.execute("select * from bancoteste") # Seleciona todos os registros da tabela bancoteste
        nomes = cursor.fetchall() # Armazena os resultados da consulta em uma variável
        conn.close() # Fecha a conexão com o banco de dados     
        for rows in nomes:
            listbox.insert(tk.END, rows[1]) # Insere os nomes na caixa de listagem (listbox)

def salvar_nome():
    name = entry.get() # Obtém o texto digitado no campo de entrada (entry)
    conn = sqlite3.connect("Bancoteste.db") # Conecta ao banco de dados
    cursor = conn.cursor() # Cria um cursor para executar comandos SQL
    cursor.execute("INSERT INTO Bancoteste (nome) VALUES (?)", (name,)) # Insere o nome no banco de dados
    conn.commit() # Salva as alterações no banco de dados
    conn.close() # Fecha a conexão com o banco de dados
    entry.delete(0, tk.END) # Limpa o campo de entrada após salvar o nome

  




window = tk.Tk() #Cria uma janela usando a biblioteca tkinter
window.title("Orange Juice") #Define o título da janela
window.geometry("780x640") #Define o tamanho da janela (largura x altura)

my_font = tk.font.Font(family="Arial", size=18) #Define a fonte a ser usada no rótulo (label) da janela

label = tk.Label(window, text='Ola mundo', font = my_font ) #Cria um rótulo (label) com o texto "Ola mundo" e o associa à janela criada anteriormente
label.pack(pady=20) #Adiciona o rótulo à janela e define um espaçamento vertical (pady) de 20 pixels

entry = tk.Entry(window, font = my_font) #Cria um campo de entrada (entry) para o usuário digitar texto, usando a fonte definida anteriormente
entry.pack(pady=20,padx=20) #Adiciona o campo de entrada à janela e define um espaçamento vertical (pady) e horizontal (padx) de 20 pixels

button = tk.Button(window, text="Salvar", font = my_font, command= salvar_nome) #Cria um botão (button) com o texto "Salvar" e o associa à janela criada anteriormente
button.pack(pady=10, padx=0) #Adiciona o botão à ja e define um espaçamento vertical (pady) de 20 pixels

button = tk.Button(window, text="listar nomes", font = my_font,width= 20,height=2, command= listar_nomes) #Cria um botão (button) com o texto "listar nomes" e o associa à janela criada anteriormente
button.pack(pady=10, padx=0) #Adiciona o botão à janela e define um espaçamento vertical (pady) de 20 pixels

button = tk.Button(window, text="Deletar nome", width= 20,height=2, command= deleta_nome)#Cria um botão (button) com o texto "Limpar lista" e o associa à janela criada anteriormente
button.pack(pady=10, padx=0) #Adiciona o botão à janela e define um espaçamento vertical (pady) de 20 pixels

listbox = tk.Listbox(window,width=40,height=10,font = ("Helvetica", 20)) #Cria uma caixa de listagem (listbox) para exibir uma lista de itens, usando a fonte definida anteriormente
listbox.pack(pady=10) #Adiciona a caixa de listagem à janela e define um espaçamento vertical (pady) de 20 pixels



window.mainloop() #Inicia o loop principal da janela, permitindo que ela seja exibida e interativa para o usuário



#________Banco de dados__________#

  #Importa a função de banco de dados sqlite
conn = sqlite3.connect("Bancoteste.db") #Cria uma conecção com um banco que eu criei
cursor = conn.cursor() # cria um cursor para executar comandos SQL
cursor.execute('''create  table if not exists Bancoteste (id integer primary key autoincrement, nome text )''') #  Cria uma tabela com os campos id e nome
conn.commit() # Salva as alterações no banco de dados
conn.close() # Fecha a conexão com o banco de dados
