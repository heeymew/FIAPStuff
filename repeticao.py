'''
# Exercício 1 com lista
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nota = int(input('Por favor digite uma nota entre 0 e 10: '))

while nota not in lista:
    print('Nota inválida, por favor digite uma nota válida')
    nota = int(input('Por favor digite uma nota entre 0 e 10: '))
    
print(f'Sua nota é: {nota}')

# Exercício 1 sem lista 
nota = int(input('Por favor digite uma nota entre 0 e 10: '))

while nota < 0 or nota > 10:
    print('Nota inválida, por favor digite uma nota válida')
    nota = int(input('Por favor digite uma nota entre 0 e 10: '))
    
print(f'Sua nota é: {nota}')

# Exercício 2

lista = []
nome = input('Digite seu nome: ')
while len(nome) < 3:
    print('Nome inválido! Digite seu nome novamente: ')
    nome = input('Digite seu nome: ').upper()
    
lista.append(nome)

idade = int(input('Digite sua idade: '))
while idade < 0 and idade > 150:
    print('Por favor digite uma idade válida!')
    idade = int(input('Digite sua idade: '))
lista.append(idade)

salario = float(input('Digite seu salário em R$: '))
while salario < 0:
    print('Digite um salário válido')
    salario = float(input('Digite seu salário em R$: '))

lista.append(salario)

sexo_valido = ['F', 'M']
sexo = input("Digite o sexo ('F' para feminino, 'M' para masculino): ").upper()

while sexo not in sexo_valido:
    print('Por favor digite um sexo válido')

if sexo == 'F':
    print('Você escolheu feminino')
    lista.append('Feminino')
else:
    print('Você escolheu masculino')
    lista.append('Masculino')

estado_civil_valido = ['S', 'C', 'V', 'D']
estado_civil = input('Digite seu estado civil: ').upper()

while estado_civil not in estado_civil_valido:
    print('Digite um valor válido')

if estado_civil == 'S':
    estado_civil_inteiro = 'Solteiro'
elif estado_civil == 'C':
    estado_civil_inteiro = 'Casado'
elif estado_civil == 'V':
    estado_civil_inteiro == 'Viúvo'
else:
    estado_civil_inteiro == 'Divorciado'

lista.append(estado_civil_inteiro)

print(f'Seu nome é {nome}, sua idade é {idade}, seu salário é de R${salario}, seu sexo é {sexo} e seu estado civil é {estado_civil_inteiro}')

# Exercício 2 simplificado

nome = input('Digite o seu nome: ').upper()
while len(nome) < 3:
    print('Nome inválido, digite seu nome novamente').upper()

idade = int(input('Digite a sua idade: '))
while idade < 0 or idade > 150:
    print('Digite novamente a sua idade')

salario = float(input('Digite o seu salário em R$: '))
while salario <= 0:
    print('Digite um salário válido')
    
sexo = input('Digite o seu sexo (F) para feminino e (M) para masculino: ').upper()
sexo_permitido = ['M', 'F']
while sexo not in sexo_permitido:
    print('Digite um sexo válido')

estado_civil = input("Digite o seu estado civil, 'S' para solteiro, 'C' para casado, 'V' para viúvo, 'D' para divorciado: ").upper()
estado_civil_letras = ['S', 'C', 'V', 'D']
while estado_civil not in estado_civil_letras:
    print('Por favor digite um estado civil válido')
    
print(f'Nome: {nome}, Idade: {idade}, Salário: {salario:.2f}, Sexo: {sexo}, Estado Civil: {estado_civil}')

# Exercício 2 professor

nome = input("Diga seu nome: ")
while len(nome) < 3:
    print("Tem que ter ao menos 3 caracteres!")
    nome = input("Diga seu nome: ")

while True:
    idade = input("Diga sua idade: ")
    if idade.isnumeric():
        idade = int(idade)
        if idade > 0 and idade < 150:
            break
        print(f"Sua idade não pode ser negativa ou maior que 150")
    else:
        print(f"{idade} não é numérico!")

salario = input("Diga seu salario: ")
while not salario.isnumeric():
    print("Deve ser um número maior que zero!")
    salario = input("Diga seu salario: ")

sexo = input("Diga f ou m: ")
while not (sexo == 'f' or sexo == 'm'):
    sexo = input("Diga f ou m: ")

ec = input("Diga s,c,v ou d: ")
while not (ec == 's' or ec == 'c' or ec == 'v' or ec == 'd'):
    ec = input("Diga s,c,v ou d: ")

# Exercício 3

paisA = 80000
paisB = 200000
anos = 0

while paisA <= paisB:
    paisA *= 1.030 #paisA * 3%
    paisB *= 1.015 #paisB * 1.5%
    anos += 1

print(f'O país A levará {anos} para alcançar a população do país B')

# Exercício 4

n1 = 0
contador = 0

while contador < 5:
    numero = float(input('Digite seu número: '))
    n1 += numero
    contador += 1
    
media = n1 / contador

print(f'A soma do contador é de {n1} e a média é de: {media:.2f}')

# Exercício 4 professor corrigido

n1 = 0
contador = 0

while contador < 5:
    numero = input('Digite seu número: ')
    while not numero.isnumeric():
        numero = input(f"Digite o {contador + 1} número: ")
    n1 += int(numero)
    contador += 1

media = n1 / contador

print(f'A soma do contador é de {n1} e a média é de: {media:.2f}')

# Exercício 5

n1 = int(input('Digite seu primeiro valor: '))
n2 = int(input('Digite seu segundo valor: '))

if n1 < n2:
    n1 += 1
    while n1 < n2:
        print(n1)
        n1 += 1
elif n2 < n1:
    while n2 < n1:
        print(n2)
        n2 += 1
else:
    print('Os números são iguais')

# Exercício 6

nome_usuario = input('Digite o seu nome de usuário: ')
senha = input('Digite sua senha: ')
while senha == nome_usuario:
    nome_usuario = input('Digite o seu nome de usuário: ')
    senha = input('Digite sua senha: ')
else:
    print('Nome de usuário e senha corretos')

# Exercício 7 você defininindo o número

i = int(input('Digite seu número para calcular a tabuada: '))
j = 1
while j <= 10:
    while j <= 10:
        print(f'{i}*{j} = {i * j}')
        j += 1
    i += 1

# Exercício 7 com todas as tabelas aparecendo

i = 1
while i < 11:
    j = 1
    while j < 11:
        print(f'{i}*{j} = {i * j}')
        j += 1
    i += 1

# Exercício 8 com número input do usuário

antecessor = 0
maior = 0
sucessor = 1
n1 = int(input('Digite o número: '))
i = 1
print(1)

while i < n1:
    i += 1
    maior = antecessor
    antecessor = sucessor
    sucessor = sucessor + maior
    print(sucessor)

# Exercício 8 infinito + break para parar o código quando quiser

a = 1
b = 1
qtd = 30
i = 2

print(a, b, end=' ')
while i < qtd: #enquanto i for menor que quantidade, faça isso
    c = b + a # C é a soma de A + B
    a = b # B fica guardado em  A
    b = c # B fica guardado em C
    print(c, end=' ') # end=' ' para printar na mesma linha
    i += 1

# Exercício 9

i = 0
qtd = 10

while i < qtd:
    n1 = input(f'Digite um número: {i + 1}')
    while not n1.isnumeric():
        num = input(f'Diga o {i + 1} número: ")
    num = int(num)
    if num % 2 = 0:
        pares += 1
    i += 1
print(f'{pares} pares e {impares} impares')

# Exercício 10

fator = 1
i = 1
num = 5
fator_string = '5!' = ' '

while i <= num:
    fator_string += f"{i}*"
    fator *= i
    i += 1

fator_string += f' = {fator}'
print(fator)

# Exercício 11 professor

n = int(input('Digite seu número para descobrir se é primo ou não: '))
i = 1

while True:
    i += 1
    if n % i == 0:
        print('Esse não é um número primo')
        break
    elif i >= n**(1/2):
        print('Esse é um número primo')
        break

# Exercício 11 que vou tentar consertar em casa

n = int(input('Digite seu número para descobrir se é primo ou não: '))
i = 1

while n / 1:
    if n % i == 0:
        print('Esse não é um número primo')
        break
    elif i >= n/2:
        print('Esse número é primo')
        break

'''

# Exercício 13

