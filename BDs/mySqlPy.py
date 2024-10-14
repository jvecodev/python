import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

# Conexão com o banco de dados
def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="controle_estoque"
    )

# Função para adicionar categoria
def adicionar_categoria():
    nome_categoria = entrada_categoria.get()
    if nome_categoria:
        try:
            conn = conectar_banco()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO categorias (nome) VALUES (%s)", (nome_categoria,))
            conn.commit()
            cursor.close()
            conn.close()
            messagebox.showinfo("Sucesso", "Categoria adicionada com sucesso!")
            entrada_categoria.delete(0, tk.END)
            atualizar_tabela_categorias()
        except Exception as e:
            messagebox.showerror("Erro", str(e))
    else:
        messagebox.showwarning("Aviso", "Por favor, insira um nome de categoria.")

# Função para atualizar a tabela de categorias
def atualizar_tabela_categorias():
    try:
        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM categorias")
        categorias = cursor.fetchall()
        cursor.close()
        conn.close()
        
        # Limpa a tabela antes de atualizar
        for linha in tabela_categorias.get_children():
            tabela_categorias.delete(linha)
        
        for categoria in categorias:
            tabela_categorias.insert("", tk.END, values=categoria)
    except Exception as e:
        messagebox.showerror("Erro", str(e))

# Função para adicionar produto
def adicionar_produto():
    nome = entrada_nome.get()
    descricao = entrada_descricao.get()
    quantidade = entrada_quantidade.get()
    preco_compra = entrada_preco_compra.get()
    preco_venda = entrada_preco_venda.get()
    categoria_id = entrada_categoria_id.get()
    
    if all([nome, quantidade, preco_compra, preco_venda, categoria_id]):
        try:
            conn = conectar_banco()
            cursor = conn.cursor()
            cursor.execute(""" 
                INSERT INTO produtos (nome, descricao, quantidade, preco_compra, preco_venda, categoria_id)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (nome, descricao, quantidade, preco_compra, preco_venda, categoria_id))
            conn.commit()
            cursor.close()
            conn.close()
            messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
            atualizar_tabela_produtos()
        except Exception as e:
            messagebox.showerror("Erro", str(e))
    else:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")

# Função para atualizar a tabela de produtos
def atualizar_tabela_produtos():
    try:
        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()
        cursor.close()
        conn.close()
        
        # Limpa a tabela antes de atualizar
        for linha in tabela_produtos.get_children():
            tabela_produtos.delete(linha)
        
        for produto in produtos:
            tabela_produtos.insert("", tk.END, values=produto)
    except Exception as e:
        messagebox.showerror("Erro", str(e))

# Função para retirar produto
def retirar_produto():
    try:
        produto_id = entrada_produto_id.get()
        quantidade = int(entrada_retirar_quantidade.get())
        
        if produto_id and quantidade > 0:
            conn = conectar_banco()
            cursor = conn.cursor()
            cursor.execute("SELECT quantidade FROM produtos WHERE id = %s", (produto_id,))
            resultado = cursor.fetchone()
            
            if resultado:
                if resultado[0] >= quantidade:
                    nova_quantidade = resultado[0] - quantidade
                    cursor.execute("UPDATE produtos SET quantidade = %s WHERE id = %s", (nova_quantidade, produto_id))
                    cursor.execute("INSERT INTO movimentacoes (produto_id, tipo, quantidade) VALUES (%s, 'saida', %s)", (produto_id, quantidade))
                    conn.commit()

                    # Excluir produto se a nova quantidade for zero
                    if nova_quantidade == 0:
                        cursor.execute("DELETE FROM movimentacoes WHERE produto_id = %s", (produto_id,))
                        conn.commit()
                        cursor.execute("DELETE FROM produtos WHERE id = %s", (produto_id,))
                        conn.commit()

                    messagebox.showinfo("Sucesso", "Produto retirado com sucesso!")
                else:
                    messagebox.showwarning("Aviso", "Quantidade insuficiente para retirar.")
            else:
                messagebox.showwarning("Aviso", "Produto não encontrado.")
            
            cursor.close()
            conn.close()
            atualizar_tabela_produtos()
            atualizar_tabela_movimentacoes()
        else:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos corretamente.")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

# Função para atualizar a tabela de movimentações
def atualizar_tabela_movimentacoes():
    try:
        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM movimentacoes")
        movimentacoes = cursor.fetchall()
        cursor.close()
        conn.close()
        
        # Limpa a tabela antes de atualizar
        for linha in tabela_movimentacoes.get_children():
            tabela_movimentacoes.delete(linha)
        
        for mov in movimentacoes:
            tabela_movimentacoes.insert("", tk.END, values=mov)
    except Exception as e:
        messagebox.showerror("Erro", str(e))

# Função para configurar a rolagem de tela
def configurar_rolagem(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

# Configuração da interface gráfica
root = tk.Tk()
root.title("Controle de Estoque")
root.geometry("1000x800")  

# Cores de fundo
root.configure(bg='#2E2E2E')

# Canvas para rolagem
canvas = tk.Canvas(root, bg='#2E2E2E')
canvas.pack(side="left", fill="both", expand=True)

# Barra de rolagem para o canvas
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

# Frame dentro do canvas para os widgets
frame_principal = ttk.Frame(canvas)
canvas.create_window((0, 0), window=frame_principal, anchor="nw")

frame_principal.bind("<Configure>", configurar_rolagem)

# Estilo para o botão azul
style = ttk.Style()
style.configure("Blue.TButton", background="blue", foreground="blue", font=("Arial", 10, "bold"))
style.map("Blue.TButton", background=[("active", "#1E90FF")])

# Entradas para categorias
ttk.Label(frame_principal, text="Categoria:", background='#2E2E2E', foreground='white').grid(row=0, column=0, padx=5, pady=5)
entrada_categoria = ttk.Entry(frame_principal)
entrada_categoria.grid(row=0, column=1, padx=5, pady=5)
ttk.Button(frame_principal, text="Adicionar Categoria", command=adicionar_categoria, style="Blue.TButton").grid(row=0, column=2, padx=5, pady=5)

# Frame com scrollbar para a tabela de categorias
frame_tabela_categorias = ttk.Frame(frame_principal)
frame_tabela_categorias.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

scrollbar_categorias = ttk.Scrollbar(frame_tabela_categorias, orient="vertical")
scrollbar_categorias.pack(side="right", fill="y")

# Tabela de categorias
tabela_categorias = ttk.Treeview(frame_tabela_categorias, columns=("ID", "Nome"), show="headings", height=5, yscrollcommand=scrollbar_categorias.set, style="Custom.Treeview")
tabela_categorias.heading("ID", text="ID", anchor="w")
tabela_categorias.heading("Nome", text="Nome", anchor="w")

# Estilo para cabeçalhos de colunas
style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"), background="#007ACC")

tabela_categorias.column("ID", width=50)
tabela_categorias.column("Nome", width=150)
tabela_categorias.pack(side="left", fill="y")

scrollbar_categorias.config(command=tabela_categorias.yview)

# Entradas para produtos
ttk.Label(frame_principal, text="Nome do Produto:", background='#2E2E2E', foreground='white').grid(row=2, column=0, padx=5, pady=5)
entrada_nome = ttk.Entry(frame_principal)
entrada_nome.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(frame_principal, text="Descrição:", background='#2E2E2E', foreground='white').grid(row=3, column=0, padx=5, pady=5)
entrada_descricao = ttk.Entry(frame_principal)
entrada_descricao.grid(row=3, column=1, padx=5, pady=5)

ttk.Label(frame_principal, text="Quantidade:", background='#2E2E2E', foreground='white').grid(row=4, column=0, padx=5, pady=5)
entrada_quantidade = ttk.Entry(frame_principal)
entrada_quantidade.grid(row=4, column=1, padx=5, pady=5)

ttk.Label(frame_principal, text="Preço de Compra:", background='#2E2E2E', foreground='white').grid(row=5, column=0, padx=5, pady=5)
entrada_preco_compra = ttk.Entry(frame_principal)
entrada_preco_compra.grid(row=5, column=1, padx=5, pady=5)

ttk.Label(frame_principal, text="Preço de Venda:", background='#2E2E2E', foreground='white').grid(row=6, column=0, padx=5, pady=5)
entrada_preco_venda = ttk.Entry(frame_principal)
entrada_preco_venda.grid(row=6, column=1, padx=5, pady=5)

ttk.Label(frame_principal, text="ID da Categoria:", background='#2E2E2E', foreground='white').grid(row=7, column=0, padx=5, pady=5)
entrada_categoria_id = ttk.Entry(frame_principal)
entrada_categoria_id.grid(row=7, column=1, padx=5, pady=5)

ttk.Button(frame_principal, text="Adicionar Produto", command=adicionar_produto, style="Blue.TButton").grid(row=8, column=0, columnspan=3, padx=5, pady=5)

# Frame com scrollbar para a tabela de produtos
frame_tabela_produtos = ttk.Frame(frame_principal)
frame_tabela_produtos.grid(row=9, column=0, columnspan=3, padx=5, pady=5)

scrollbar_produtos = ttk.Scrollbar(frame_tabela_produtos, orient="vertical")
scrollbar_produtos.pack(side="right", fill="y")

# Tabela de produtos
tabela_produtos = ttk.Treeview(frame_tabela_produtos, columns=("ID", "Nome", "Descrição", "Quantidade", "Preço de Compra", "Preço de Venda", "Categoria ID"), show="headings", height=5, yscrollcommand=scrollbar_produtos.set)
tabela_produtos.heading("ID", text="ID", anchor="w")
tabela_produtos.heading("Nome", text="Nome", anchor="w")
tabela_produtos.heading("Descrição", text="Descrição", anchor="w")
tabela_produtos.heading("Quantidade", text="Quantidade", anchor="w")
tabela_produtos.heading("Preço de Compra", text="Preço de Compra", anchor="w")
tabela_produtos.heading("Preço de Venda", text="Preço de Venda", anchor="w")
tabela_produtos.heading("Categoria ID", text="Categoria ID", anchor="w")

tabela_produtos.column("ID", width=50)
tabela_produtos.column("Nome", width=150)
tabela_produtos.column("Descrição", width=200)
tabela_produtos.column("Quantidade", width=100)
tabela_produtos.column("Preço de Compra", width=100)
tabela_produtos.column("Preço de Venda", width=100)
tabela_produtos.column("Categoria ID", width=100)
tabela_produtos.pack(side="left", fill="y")

scrollbar_produtos.config(command=tabela_produtos.yview)

# Entradas para retirar produtos
ttk.Label(frame_principal, text="ID do Produto para Retirar:", background='#2E2E2E', foreground='white').grid(row=10, column=0, padx=5, pady=5)
entrada_produto_id = ttk.Entry(frame_principal)
entrada_produto_id.grid(row=10, column=1, padx=5, pady=5)

ttk.Label(frame_principal, text="Quantidade para Retirar:", background='#2E2E2E', foreground='white').grid(row=11, column=0, padx=5, pady=5)
entrada_retirar_quantidade = ttk.Entry(frame_principal)
entrada_retirar_quantidade.grid(row=11, column=1, padx=5, pady=5)

ttk.Button(frame_principal, text="Retirar Produto", command=retirar_produto, style="Blue.TButton").grid(row=12, column=0, columnspan=3, padx=5, pady=5)

# Frame com scrollbar para a tabela de movimentações
frame_tabela_movimentacoes = ttk.Frame(frame_principal)
frame_tabela_movimentacoes.grid(row=13, column=0, columnspan=3, padx=5, pady=5)

scrollbar_movimentacoes = ttk.Scrollbar(frame_tabela_movimentacoes, orient="vertical")
scrollbar_movimentacoes.pack(side="right", fill="y")

# Tabela de movimentações
tabela_movimentacoes = ttk.Treeview(frame_tabela_movimentacoes, columns=("ID", "Produto ID", "Tipo", "Quantidade"), show="headings", height=5, yscrollcommand=scrollbar_movimentacoes.set)
tabela_movimentacoes.heading("ID", text="ID", anchor="w")
tabela_movimentacoes.heading("Produto ID", text="Produto ID", anchor="w")
tabela_movimentacoes.heading("Tipo", text="Tipo", anchor="w")
tabela_movimentacoes.heading("Quantidade", text="Quantidade", anchor="w")

tabela_movimentacoes.column("ID", width=50)
tabela_movimentacoes.column("Produto ID", width=100)
tabela_movimentacoes.column("Tipo", width=100)
tabela_movimentacoes.column("Quantidade", width=100)
tabela_movimentacoes.pack(side="left", fill="y")

scrollbar_movimentacoes.config(command=tabela_movimentacoes.yview)

# Atualiza as tabelas ao iniciar
atualizar_tabela_categorias()
atualizar_tabela_produtos()
atualizar_tabela_movimentacoes()

# Executa a interface
root.mainloop()
