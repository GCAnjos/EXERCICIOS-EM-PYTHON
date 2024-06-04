import tkinter as tk
from tkinter import messagebox
import mysql.connector

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="451451",
        database="dados"
    )

def inserir_dados(nome, disciplina, nota):
    try:
        conexao = conectar_bd()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO usuarios (nome, disciplina, nota) VALUES (%s, %s, %s)", (nome, disciplina, nota))
        conexao.commit()
        messagebox.showinfo("Sucesso", "Dados inseridos com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao inserir dados: {e}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()

def mostrar_dados(nome):
    try:
        conexao = conectar_bd()
        cursor = conexao.cursor()
        cursor.execute("SELECT nome, disciplina, nota FROM usuarios WHERE nome = %s", (nome,))
        dados = cursor.fetchall()

        if dados:
            soma_notas = sum(nota for _, _, nota in dados)
            media_notas = soma_notas / len(dados)

            mensagem = f"Dados de {nome}:\n\n"
            for nome, disciplina, nota in dados:
                mensagem += f"Disciplina: {disciplina}, Nota: {nota}\n"
            mensagem += f"\nSoma das notas: {soma_notas}\nMédia das notas: {media_notas:.2f}"
            messagebox.showinfo("Dados", mensagem)
        else:
            messagebox.showwarning("Aviso", f"Nenhum dado encontrado para {nome}.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao mostrar dados: {e}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()

def inserir_click():
    nome = entry_nome.get()
    disciplina = entry_disciplina.get()
    nota = entry_nota.get()
    if nome and disciplina and nota:
        inserir_dados(nome, disciplina, nota)
    else:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")

def mostrar_click():
    nome = entry_nome.get()
    if nome:
        mostrar_dados(nome)
    else:
        messagebox.showwarning("Aviso", "Por favor, insira um nome para mostrar os dados.")

root = tk.Tk()
root.title("Cadastro & CR")
root.geometry("380x220")

label_nome = tk.Label(root, text="Nome:")
label_nome.grid(row=0, column=0, padx=5, pady=5)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

label_disciplina = tk.Label(root, text="Disciplina:")
label_disciplina.grid(row=1, column=0, padx=5, pady=5)
entry_disciplina = tk.Entry(root)
entry_disciplina.grid(row=1, column=1, padx=5, pady=5)

label_nota = tk.Label(root, text="Nota:")
label_nota.grid(row=2, column=0, padx=5, pady=5)
entry_nota = tk.Entry(root)
entry_nota.grid(row=2, column=1, padx=5, pady=5)

label_instrucao = tk.Label(root, text="Coloque o nome que deseja pesquisar em (Nome),\n"
                                      "em seguida clique em (Mostrar) para ver o CR.")
label_instrucao.grid(row=5, column=1, padx=5, pady=5)

btn_inserir = tk.Button(root, text="Inserir", command=inserir_click)
btn_inserir.grid(row=3, column=1, columnspan=2, padx=5, pady=5, sticky="we")

btn_mostrar = tk.Button(root, text="Mostrar", command=mostrar_click)
btn_mostrar.grid(row=4, column=1, columnspan=2, padx=5, pady=5, sticky="we")

root.mainloop()
