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
else:
    print(f'Nome válido. Nome adicionado à lista {lista}')
    
lista.append(nome)

idade = int(input('Digite sua idade: '))
while idade < 0 and idade > 150:
    print('Por favor digite uma idade válida!')
    idade = int(input('Digite sua idade: '))
else:
    print(f'Sua idade foi adicionada ao seu cadastro {lista}')
lista.append(idade)

salario = float(input('Digite seu salário em R$: '))
while salario < 0:
    print('Digite um salário válido')
    salario = float(input('Digite seu salário em R$: '))
else:
    print(f'Seu salário foi adicionado ao seu cadastro {lista}')

lista.append(salario)

sexo_valido = ['F', 'M']
sexo = input("Digite o sexo ('F' para feminino, 'M' para masculino): ").upper()

while sexo not in sexo_valido:
    print('Por favor digite um sexo válido')

if sexo == 'F':
    print('Você digitou feminino')
    lista.append('Feminino')
else:
    print('Você digitou masculino')
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

# Exercício 2 simplificado

nome = input('Digite o seu nome: ').upper()
while len(nome) < 3:
    print('Nome inválido, digite seu nome novamente').upper()
    nome = input('Digite o seu nome: ')

idade = int(input('Digite a sua idade: '))
while idade < 0 and idade > 150:
    print('Digite novamente a sua idade')
    idade = int(input('Digite a sua idade: '))

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
    estado_civil = input("Digite o seu estado civil, 'S' para solteiro, 'C' para casado, 'V' para viúvo, 'D' para divorciado: ").upper()
    
print(f'Nome: {nome}, Idade: {idade}, Salário: {salario:.2f}, Sexo: {sexo}, Estado Civil: {estado_civil}')

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

# Exercício 5

n1 = int(input('Digite seu primeiro valor: '))
n2 = int(input('Digite seu segundo valor: '))

if n1 < n2:
    n1 += 1
    while n1 < n2:
        print(n1)
        n1 += 1
elif n2 < n1:
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
    
'''

# Exercício 7

tabuada = int(input('Digite seu número que quer gerar a tabuada: '))
contador = 0

while len(tabuada) <= 10:
    contador *= tabuada
else:
    print('Digite um número válido')