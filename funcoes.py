'''

# Exercício 1

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def soma(numeros):
    return sum(numeros)

resultado = soma(numeros)
print(resultado)

# Exercício 2

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def maior(numeros):
    return max(numeros)

resultado = max(numeros)
print(resultado)

# Exercício 3

lista = ['Maçã', 'Banana', 'Uva', 'Pera', 'Melancia', 'Abacaxi']

def letras_a(lista):
    resultado = []
    for s in lista:
        if s[0].lower() == 'a':
            resultado.append(s)
    return resultado


resultado = letras_a(lista)
print(resultado) 

# Exercício 4

lista_numerica = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def lista_pares(lista_numerica):
        return [num for num in lista_numerica if num % 2 == 0]

resultado_pares = lista_pares(lista_numerica)
print(resultado_pares)

'''
