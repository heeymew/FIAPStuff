'''
1 – Modifique o seguinte Código para eliminar o uso de condicionais

resp = input('Digite oi ou tchau: ')
dicionario = {'Oi': 'Olá', 'Tchau': 'Adios'}

print(dicionario[resp])

2 - Traga ao usuário todas as informações sobre um carro de sua
escolha:

'''

def forca_opcao(msg, opcoes):
    possibilidades = opcoes
    opcao = input(f'{msg}\n{possibilidades}\n')
    while opcao not in opcoes:
        print('Opção inválida!')
        opcao = input(f'{msg}\n{possibilidades}\n')
    return opcao

def achar_indice(lista, elemento):
    for i in range(len(lista)):
        if elemento in lista[i]:
            return i
    return

def menor_maior_preco(precos):
    menor = 0
    maior = 0

    for i in range(len(precos)):
        if precos[i] > precos[maior]:
            maior = i
        if precos[i] < precos[menor]:
            menor = i

    return menor, maior

carros = {
    'nome': ['celta', 'up', 'kombi', 'uno'],
    'portas': [4, 2, 6, 2],
    'preço': [1000, 200, 300, 100],
    'ano de fabricação': [2014, 2018, 1970, 2005]
}

carro = forca_opcao('Qual carro você quer escolher? ', carros['nome'])
indices = achar_indice(carros['nome'], carro)

for key in carros.keys():
    print(f'{key}: {carros[key][indices]}')

menor_preco, maior_preco = menor_maior_preco(carros['preço'])

print(f'\nO carro mais caro é o {carros["nome"][maior_preco]} custando R$ {carros["preço"][maior_preco]}')
print(f'\nO carro mais barato é o {carros["nome"][menor_preco]} custando R$ {carros["preço"][menor_preco]}\n')