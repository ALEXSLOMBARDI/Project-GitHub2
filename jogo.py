import random
import tkinter as tk

# Cria a janela principal
root = tk.Tk()
root.title("Jogo de Bingo")
root.geometry("600x500")

# Frame para o numero grande
numero_grande_frame = tk.Frame(root)
numero_grande_frame.pack(pady=20)

# Label para exibir o número sorteado
numero_grande_label = tk.Label(numero_grande_frame, text="Bingo!", font=("Arial", 48))
numero_grande_label.pack()

# Definindo as letras do Bingo
letras = ['B', 'I', 'N', 'G', 'O']

# Criando a tabela de números de 1 a 70
tabela = {letra: list(range(i, i + 15)) for i, letra in zip(range(1, 71, 15), letras)}

# Frame para a tabela de Bingo
tabela_frame = tk.Frame(root)
tabela_frame.pack(pady=20)

# Criando os labels da tabela
labels_tabela = {letra: [] for letra in letras}

for letra in letras:
    letra_label = tk.Label(tabela_frame, text=letra, font=("Arial", 14, "bold"))
    letra_label.grid(row=0, column=letras.index(letra), padx=10)
    for i, numero in enumerate(tabela[letra]):
        label = tk.Label(tabela_frame, text=str(numero), width=4, height=2, relief="solid", font=("Arial", 12))
        label.grid(row=i + 1, column=letras.index(letra), padx=5, pady=2)
        labels_tabela[letra].append(label)


# Inicia o loop da interface gráfica
root.mainloop()