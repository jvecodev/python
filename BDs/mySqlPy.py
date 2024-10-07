import tkinter as tk     # interface padrão da linguagem de programação Python
from   tkinter import simpledialog
from   tkinter import ttk #Styles https://wiki.tcl-lang.org/page/List+of+ttk+Themes ; https://tkdocs.com/tutorial/styles.html
import mysql.connector  

# Exemplo baseado em: https://www.youtube.com/watch?v=QQM9Q1Cd5CA

# --------------------------------------------------------
# selectAllRows Function
# --------------------------------------------------------
def selectAllRows():
      clearEntries()
      conexao = mysql.connector.connect(host='localhost', user='root', password='PUC@1234', database='DB_Python')
      cursor = conexao.cursor() # Mantém o retorno de consulta SQL, linha por linha
      comandoR = f"Select ID_Usuario, Nome, Celular, Login FROM DB_Python.usuario" #READ data
      cursor.execute(comandoR)
      result = cursor.fetchall() #busca todas as linhas de um conjunto de resultao
      if cursor.rowcount != 0:  # -- result != None: 
            for row in result:
                  print(row) 
                  tree.insert("", tk.END, values=row)        
      else:
            tk.messagebox.showinfo(title="Cadastro Usuários", message="Cadastro Vazio") 
      cursor.close()
      conexao.close()


# --------------------------------------------------------
# selectRow Function
# --------------------------------------------------------
def selectRow():
      # limpa entradas
      id_entry.delete(0,'end')
      nm_entry.delete(0,'end')
      cl_entry.delete(0,'end')
      lg_entry.delete(0,'end')
      pw_entry.delete(0,'end')

      # preenche entradas com valores selecionados da treeView
      if len(tree.selection()) > 0:
            selectedItem = tree.selection()[0]
            id_entry.insert(0, tree.item(selectedItem)['values'][0])
            nm_entry.insert(0, tree.item(selectedItem)['values'][1])
            cl_entry.insert(0, tree.item(selectedItem)['values'][2])
            lg_entry.insert(0, tree.item(selectedItem)['values'][3])
            return True
      else:
            tk.messagebox.showinfo("ALERT", "Select a valid ID from the options in the data frame.")
            return False
     

# --------------------------------------------------------
# clearEntries Function
# --------------------------------------------------------
def clearEntries():
      id_entry.delete(0,'end')
      nm_entry.delete(0,'end')
      cl_entry.delete(0,'end')
      lg_entry.delete(0,'end')
      pw_entry.delete(0,'end')
      for i in tree.get_children():
            tree.delete(i)

# --------------------------------------------------------
# insert Function
# --------------------------------------------------------
def insert():
      id   = id_entry.get()
      nome = nm_entry.get()
      cel  = cl_entry.get()
      log  = lg_entry.get()
      pwd  = pw_entry.get()

      if(nome == "" or cel == "" or log == "" or pwd == ""):
            tk.messagebox.showinfo("ALERT", "Fill in your [nome], [celular], [login] and [senha].")
      else:
            conexao = mysql.connector.connect(host='localhost', user='root', password='PUC@1234', database='DB_Python')
            cursor = conexao.cursor()
            comandoC = f"INSERT INTO DB_Python.usuario (ID_usuario, Nome, Celular, Login, Senha) VALUES ({id},'{nome}', '{cel}', '{log}', MD5('{pwd}'))"  #grava a senha criptografada com MD5
            cursor.execute(comandoC)
            conexao.commit()
            tk.messagebox.showinfo("Status", "insert successful!")

            clearEntries()

            cursor.close()
            conexao.close()
            selectAllRows()

# --------------------------------------------------------            
# delete Function
# --------------------------------------------------------
def delete():
      if selectRow():
            ident = id_entry.get() 
            log  = lg_entry.get()
            conexao = mysql.connector.connect(host='localhost', user='root', password='PUC@1234', database='DB_Python')
            cursor = conexao.cursor()
            comandoC = f"DELETE FROM DB_Python.usuario WHERE (ID_usuario='{ident}' OR Login = '{log}')" 
            cursor.execute(comandoC)
            conexao.commit()
            tk.messagebox.showinfo("Status", "Deleção bem sucedida!")
            cursor.close()
            conexao.close()
      
      clearEntries()
      selectAllRows()

# --------------------------------------------------------
# update Function
# --------------------------------------------------------
def update():
      nome = nm_entry.get()
      cel  = cl_entry.get()
      log  = lg_entry.get()
      pwd  = pw_entry.get()

      if(nome == "" or cel == "" or log == ""):
            tk.messagebox.showinfo("ALERT", "select a valid ID (select a record / row).")
      else:            
            # Preenche variáveis com respectivos campos de entrada
            ident = id_entry.get()
            nome  = nm_entry.get()
            cel   = cl_entry.get()
            log   = lg_entry.get()
            pwd   = pw_entry.get()

            conexao = mysql.connector.connect(host='localhost', user='root', password='PUC@1234', database='DB_Python')
            cursor = conexao.cursor()

            comandoU = f"UPDATE DB_Python.usuario SET Nome = '{nome}', Celular = '{cel}', Login = '{log}'"
            if pwd  != "": 
                  comandoU += f", Senha = MD5('{pwd}')" # concatena na delcaração SQL a senha criptografada com MD5

            comandoU += f" WHERE ID_Usuario = '{ident}'" # concatena na declaração SQL a condição para atualização
            
            cursor.execute(comandoU)
            conexao.commit()
            tk.messagebox.showinfo("Status", "Update successful!")
            cursor.close()
            conexao.close()
      clearEntries()
      selectAllRows()


# --------------------------------------------------------
# Main - Create Tkinter window
# --------------------------------------------------------
root = tk.Tk()
root.title("MySQL Simple CRUD sample")
root.geometry("530x670+700+50") # Janela de tamanho 500x500 pixels, posicionanda em x=500 y=300
root.style = ttk.Style()
root.style.theme_use("clam")

# --------------------------------------------------------
# Add labels and inputs (entry boxes)
# --------------------------------------------------------
id = tk.Label(root,text="ID:", font=("verdana 15"))
id.place(x=50,y=250)
id_entry = tk.Entry(root, font=("verdana 15"))
id_entry.place(x=150, y=250)

nm = tk.Label(root,text="Nome:", font=("verdana 15"))
nm.place(x=50,y=300)
nm_entry = tk.Entry(root, font=("verdana 15"))
nm_entry.place(x=150, y=300)

cl = tk.Label(root,text="Celular:", font=("verdana 15"))
cl.place(x=50,y=350)
cl_entry = tk.Entry(root, font=("verdana 15"))
cl_entry.place(x=150, y=350)

lg = tk.Label(root,text="Login:", font=("verdana 15"))
lg.place(x=50,y=400)
lg_entry = tk.Entry(root, font=("verdana 15"))
lg_entry.place(x=150, y=400)

pw = tk.Label(root,text="Senha:", font=("verdana 15"))
pw.place(x=50,y=450)
pw_entry = tk.Entry(root, font=("verdana 15"))
pw_entry.place(x=150, y=450)

tree = ttk.Treeview(root, column=("ID", "Nome", "Celular", "Login"), show='headings')
tree.column("#1", anchor=tk.CENTER, minwidth=50, width=50, stretch=False)
tree.heading("#1", text="ID")
tree.column("#2", anchor=tk.CENTER, minwidth=150, width=150, stretch=False)
tree.heading("#2", text="Nome")
tree.column("#3", anchor=tk.CENTER, minwidth=150, width=150, stretch=False)
tree.heading("#3", text="Celular")
tree.column("#4", anchor=tk.CENTER, minwidth=150, width=150, stretch=False)
tree.heading("#4", text="Login")
tree.pack(padx=10, pady=10)

btninsert    = tk.Button(root,text="INSERT",command=insert,               font=("verdada 15")).place(x= 50, y = 500)
btnselectALL = tk.Button(root,text="SELECT *", command=selectAllRows,     font=("verdada 15")).place(x=150, y = 500)
btnselectOne = tk.Button(root,text="SELECT one record",command=selectRow, font=("verdada 15")).place(x=270, y = 500)
btnDelete    = tk.Button(root,text="DELETE",command=delete,               font=("verdada 15")).place(x=150, y = 550)
btnUpdate    = tk.Button(root,text="UPDATE",command=update,               font=("verdada 15")).place(x=260, y = 550)

btnClearAll  = tk.Button(root,text="CLEAR ENTRIES",command=clearEntries,  font=("verdada 15"), bg='#081947', fg='#fff',).place(x=170, y = 600)

selectAllRows()

root.mainloop()