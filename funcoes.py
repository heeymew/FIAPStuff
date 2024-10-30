'''

# Exercício 1

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def soma(numeros):
    return sum(numeros)

resultado = soma(numeros)
print(resultado)

# Exercício 1 sem sum

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def lista_numerica(lista):
    numero = 0
    for s in lista:
        numero += s

    total = numero
    print(total)

lista_numerica(lista)

# Exercício 2

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def maior(numeros):
    return max(numeros)

resultado = max(numeros)
print(resultado)

# Exercício 2 sem max

def lista_numerica(lista):
    maior = lista[0]
    for i in range (len(lista)):
        if lista[i] > maior:
           maior = lista[i]
    return maior

lista = [9, 5, 6, 8, 4, 3, 7, 2, 1, 10]

print(lista_numerica(lista))

# Exercício 2 pt 2

def lista_numerica(lista):
    indice_maior = lista[0]
    maior = lista[indice_maior]
    for i in range (len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            indice_maior = i
    return indice_maior

lista = [9, 5, 6, 8, 4, 3, 7, 2, 1, 10]
alunos = ['Lucas', 'Pedro', 'Leandro', 'Victor', 'Ian', 'Cilas', 'Witalonn', 'David', 'Icaro', 'Saori']

# Exercício 3

lista = ['Maçã', 'Banana', 'Uva', 'Pera', 'Melancia', 'Abacaxi']

def letras_a(lista):
    resultado = []
    for s in lista:
        if s[0].lower() == 'a':
            resultado.append(s)
    return resultado

lista_frutas = ['Banana', 'Maçã', 'Abacaxi', 'Ameixa', 'Pêra']

# Exercício 3 pt 2

def letras_a(lista):
    resultado = []
    for s in lista:
        if s[0].lower() == 'a':
            resultado.append(s)
    return resultado

resultado = letras_a(lista)
print(resultado)

resultado = letras_a(lista)
print(resultado) 

# Exercício 3 com alunos

alunos = ['Lucas', 'Pedro', 'Leandro', 'Victor', 'Ian', 'Cilas', 'Witalonn', 'David', 'Icaro', 'Saori', 'Allan']

def comeca_com_a(lista):
    filtro = []
    for palavra in lista:
        if palavra[0].lower() == 'l':
            filtro.append(palavra)
    return filtro

print(comeca_com_a(alunos))

# Exercício 4

lista_numerica = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def lista_pares(lista_numerica):
        return [num for num in lista_numerica if num % 2 == 0]

resultado_pares = lista_pares(lista_numerica)
print(resultado_pares)


# Exercício 4 com append

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def pares(lista):
    pares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
    return pares

pares = pares(lista)
print(pares)

# Exercício 5

lista_frutas = ['Maçã', 'Banana', 'Uva', 'Pera', 'Melancia', 'Abacaxi']

def frutas_listadas(lista_frutas):
    palavras = []
    for frutas in range(len(lista_frutas)):
        return frutas[]

# Exercício 6

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_numeros2 = [2, 4, 6, 8, 10, 12, 14]

def comparar():
    compare = []
    for num in lista_numeros:
        if num in lista_numeros2:
            compare.append(num)
    return compare

print(comparar())

'''

# Exercício 7

lista_n = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def lista_crescente(lista_n):

    for crescente in lista_n:

'''

def verifica_numero(msg, msg_erro='Inválido!'):

    num = input(msg)
    while not num.isnumeric():
        print(msg_erro)
        num = input(msg)
    num = int(num)
    return num


ano = verifica_numero('Diga o seu ano de nascimento: ',)
qtd = verifica_numero('Digita a quantidade de garrafas: ')

print(f'O ano que você nasceu é: {ano} e a quantidade de garrafas é de {qtd}')

def opcao(msg, vinhos):
    opcao = input(msg)
    while not opcao in vinhos:
        print('Inválido')
        opcao = input(msg)
    return opcao

vinhos = ['Pérgola', 'Chapinha', 'Sangue de Boi']
escolha = opcao('Qual vinho você quer? ', vinhos)
print(escolha)

notas = [5, 9, 10, 1, 4]
soma = 0

for s in notas:
    soma += s
media = soma/len(notas)

print(media)

def media_notas(notas):
    soma = 0
    for s in notas:
        soma += s
        media = soma/len(notas)
    return media

notas = [5, 9, 10, 1, 4]
media = media_notas(notas)
print(media)

# Exercício 7

def invertida_lista(lista):
    lista_invertida = []

    for i in range(len(lista) - 1, -1, -1):
        lista_invertida.append(lista[i])

    return lista_invertida 


lista = [2, 3, 1, 6, 5, 4]
print(invertida_lista(lista))


'''
