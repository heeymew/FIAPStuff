import matplotlib.pyplot as plt

#1 – Faça uma função que printa uma matriz da maneira convencional, ou seja, uma linha abaixo da outra.

def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

matriz = cria_matriz(30, 30)

def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)
    return

#3 – Faça uma função que recebe uma matriz quadrada como parâmetro e altera todos os elementos da diagonal para 1.

def matriz_diagonal(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == j:
                matriz[i][j] = 1
    return

#4 - Faça uma função que recebe uma matriz quadrada como parâmetro e altera todos os elementos da “contra-diagonal” para 1.

def matriz_contra_diagonal(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i + j == len(matriz) - 1:
                matriz[i][j] = 1
    return

def matriz_contra_diagonal(matriz):
    for i in range(len(matriz)):
        matriz[i][len(matriz) - 1 - i] = 1
    return

# Matriz contra-diagonal alterando valores de cima ou baixo para 1.
def matriz_contra_diagonal(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i + j < len(matriz) - 1:
                matriz[i][j] = 1
    return

#5 – Faça uma função que recebe uma matriz quadrada e altera todos os elementos acima/abaixo da diagonal para 1

def cima_baixo_diagonal(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i != j:
                matriz[i][j] = 1
    return

#6 – Faça uma função que recebe uma matriz quadrada e retorne sua transposta

def matriz_transposta(matriz):
    for i in range(len(matriz)):
        for j in range(i+1,len(matriz)):
            aux = matriz[i][j]
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = aux
    return

matriz_transposta(matriz)

def soma_lista(lista):
    soma = 0
    for elem in lista:
        soma += elem
    return soma
def exercicio_notas():
    notas = [[6, 4, 2, 0, 3, 7, 2, 10, 5, 1], [1, 5, 5, 6, 7, 8, 2, 8, 8, 4], [9, 4, 10, 10, 5, 9, 1, 2, 9, 0], [10, 5, 7, 4, 6, 6, 7, 4, 7, 1], [4, 4, 3, 0, 3, 3, 0, 0, 10, 0]]
    mostra_matriz(notas)
    pesos = [1,2,3,2,1]
    soma_pesos = soma_lista(pesos)
    notas_finais = []
    for j in range(len(notas[0])):
        soma = 0
        for i in range(len(pesos)):
            soma += pesos[i]*notas[i][j]
        soma/= soma_pesos
        notas_finais.append(round(soma,2))
    print(notas_finais)
    return

matriz = cria_matriz(linhas, colunas)
exercicio_notas()
