print('Bem-vindo à Vinheria Agnello!')

nome = input('Digite o seu nome: ')
while len(nome) < 3:
    nome = input('Digite o seu nome: ')

endereco = input('Por favor, insira o seu endereço para entrega: ')

while True:
    idade = input('Digite a sua idade: ')
    if idade.isnumeric():
        idade = int(idade)
        if idade >= 18:
            print(f'Bem-vindo {nome}') 
        else:
            print('Você deve ter 18 anos ou mais para comprar bebidas.')
            break
    else:
        print('Por favor, digite uma idade válida.')
        break
        
    vinho1 = 'Chapinha'
    vinho2 = 'Rosé'
    vinho3 = 'Branco'
    preco_vinho1 = 40
    preco_vinho2 = 80
    preco_vinho3 = 120
    qtd_chapinha = 0
    qtd_rose = 0
    qtd_branco = 0
    frete = 20
    sair = 4

    while True:
        opcao = input('Digite o vinho que você quer selecionar:\n1: Chapinha R$: 40 \n2: Branco R$ 120 \n3: Rose R$ 80\nDigite qual opção você quer: ')
        
        if opcao.isnumeric():
            opcao = int(opcao)
            
            if opcao == 1:
                qtd = int(input('Digite a quantidade de vinhos que você quer selecionar: '))
                qtd_chapinha += qtd
                print(f'A quantidade de vinhos {vinho1} selecionados foi de: {qtd_chapinha}') 
            
            elif opcao == 2:
                qtd = int(input('Digite a quantidade de vinhos que você quer selecionar: '))
                qtd_rose += qtd
                print(f'A quantidade de vinhos {vinho2} selecionados foi de: {qtd_rose}') 
                
            elif opcao == 3:
                qtd = int(input('Digite a quantidade de vinhos que você quer selecionar: '))
                qtd_branco += qtd
                print(f'A quantidade de vinhos {vinho3} selecionados foi de: {qtd_branco}') 
                
            elif opcao == 4:
                print('Saindo')
                break
            
            else:
                print('Opção inválida, tente novamente.')
                
            continuar = input('Você quer escolher mais vinhos? (Digite Sim) para sim e outra tecla para sair: ')
            if continuar != 'Sim':
                break
        else:
            print('Por favor digite um número válido.')
    soma_total = (qtd_chapinha * preco_vinho1) + (qtd_rose * preco_vinho2) + (qtd_branco * preco_vinho3)


    if soma_total > 500:
        print(f'A Soma total dos vinhos é de R$: {soma_total}, o produto será entregue em: {endereco} e você tem frete grátis')
        break
    else:
        soma_total += frete
        print(f'A Soma total dos vinhos é de R$: {soma_total}, o produto será entregue em {endereco} e o frete é de R$:{frete}')
        break

#teste cp2 com for

print('Bem vindos a Vinheria Agnello')

vinhos = ["Chapinha", "Pérgola", "La Dorni"]
precos = [60, 80, 120]

endereco = input('Digite o seu endereço: ')


qtd_vinho1 = 0
qtd_vinho2 = 0
qtd_vinho3 = 0
valor_total = 0
frete = 20

while True:
    ano = input('Digite o ano em que você nasceu: ')
    if ano.isnumeric():
        ano = int(ano)
    else:
        print("Ano inválido, por favor digite apenas números.")
        continue
    
    if ano < 2006:
        print('Nós temos 3 opções de vinho:\n')
        
        i = 1
        for vinho in vinhos:
            print(f'{i} - {vinho}')
            i += 1
    
        while True:
            vinho_escolhido = input('Informe qual vinho você quer escolher: ')
            if vinho_escolhido.isnumeric(): 
                vinho_escolhido = int(vinho_escolhido)
                
                if vinho_escolhido == 1:
                    print('Você escolheu o vinho Chapinha')
                    qtd_vinho1 = int(input('Digite a quantidade de garrafas que você quer comprar: '))
                    valor_total += 60 * qtd_vinho1
                    print(f'Você escolheu {qtd_vinho1} Chapinha')
                
                elif vinho_escolhido == 2:
                    print('Você escolheu o vinho Pérgola')
                    qtd_vinho2 = int(input('Digite a quantidade de garrafas que você quer comprar: '))
                    valor_total += 80 * qtd_vinho2
                    print(f'Você escolheu {qtd_vinho2} Pérgola')
                    
                elif vinho_escolhido == 3:
                    print('Você escolheu o vinho La Dorni')
                    qtd_vinho3 = int(input('Digite a quantidade de garrafas que você quer comprar: '))
                    valor_total += 120 * qtd_vinho3
                    print(f'Você escolheu {qtd_vinho3} La Dorni')
                
                else:
                    print('Opção inválida! Por favor escolha 1, 2 ou 3.')
                    continue
                
                continuar = input('Digite (S) para continuar ou (N) para sair: ')
                if continuar == 'N':
                    break
            else:
                print('Valor inválido, por favor escolha uma opção numérica.')
                
        garrafas = qtd_vinho1 + qtd_vinho2 + qtd_vinho3
                
        if valor_total > 500:
            print(f'Você comprou {garrafas} garrafas, {qtd_vinho1} Chapinha, {qtd_vinho2} Pérgola e {qtd_vinho3} La Dorne. O preço total foi de R$: {valor_total}, você tem frete grátis!')
        else:
            print(f'Você comprou {garrafas} garrafas, {qtd_vinho1} Chapinha, {qtd_vinho2} Pérgola e {qtd_vinho3} La Dorne. O preço total com o valor do frete foi de R$: {valor_total + frete}.')
        break
    else:
        print('Você deve ter no mínimo 18 anos para poder comprar bebida!')
        break

# teste cp3

print('Bem vindos a Vinheria Agnello')

def solicitar_endereco():
    return input('Digite o seu endereço: ')

def verificar_idade():
    while True:
        ano = input('Digite o ano em que você nasceu: ')
        if ano.isnumeric():
            ano = int(ano)
            if ano < 2006:
                return True
            print('Você deve ter no mínimo 18 anos para poder comprar bebida!')
            return False
        print("Ano inválido, por favor digite apenas números.")

def listar_vinhos(lista_vinhos):
    print('Nós temos 3 opções de vinho:\n')
    for i in range(len(lista_vinhos)):
        print(f'{i + 1} - {lista_vinhos[i]}')

def validar_input_numerico(mensagem):
    while True:
        valor = input(mensagem)
        if valor.isnumeric():
            return int(valor)
        print('Por favor, digite um número válido.')

def escolher_vinho(lista_vinhos):
    while True:
        vinho_escolhido = validar_input_numerico('Informe qual vinho você quer escolher: ')
        if vinho_escolhido >= 1 and vinho_escolhido <= len(lista_vinhos):
            print(f'Você escolheu o vinho {lista_vinhos[vinho_escolhido-1]}')
            return vinho_escolhido - 1
        print('Opção inválida! Por favor escolha 1, 2 ou 3.')

def escolher_quantidade(nome_vinho):
    quantidade = validar_input_numerico(f'Digite a quantidade de garrafas que você quer comprar: ')
    print(f'Você escolheu {quantidade} {nome_vinho}')
    return quantidade

def calcular_valor(quantidade, preco):
    return quantidade * preco

def deseja_continuar():
    return input('Digite (S) para continuar ou (N) para sair: ').upper() != 'N'

def calcular_total_garrafas(quantidade_garrafas):
    total = 0
    for quantidade in quantidade_garrafas:
        total += quantidade
    return total

def mostrar_resumo_compra(lista_vinhos, quantidade_garrafas, valor_total, frete):
    total_garrafas = calcular_total_garrafas(quantidade_garrafas)
    
    if valor_total > 500:
        print(f'Você comprou {total_garrafas} garrafas, '
              f'{quantidade_garrafas[0]} {lista_vinhos[0]}, '
              f'{quantidade_garrafas[1]} {lista_vinhos[1]} e '
              f'{quantidade_garrafas[2]} {lista_vinhos[2]}. '
              f'O preço total foi de R$: {valor_total}, você tem frete grátis!')
    else:
        print(f'Você comprou {total_garrafas} garrafas, '
              f'{quantidade_garrafas[0]} {lista_vinhos[0]}, '
              f'{quantidade_garrafas[1]} {lista_vinhos[1]} e '
              f'{quantidade_garrafas[2]} {lista_vinhos[2]}. '
              f'O preço total com o valor do frete foi de R$: {valor_total + frete}.')

def realizar_compra(lista_vinhos, lista_precos, quantidade_garrafas):
    valor_total = 0
    
    while True:
        listar_vinhos(lista_vinhos)
        indice_vinho = escolher_vinho(lista_vinhos)
        quantidade = escolher_quantidade(lista_vinhos[indice_vinho])
        
        quantidade_garrafas[indice_vinho] = quantidade
        valor_total += calcular_valor(quantidade, lista_precos[indice_vinho])
        
        if not deseja_continuar():
            break
    
    return valor_total

def main():
    lista_vinhos = ["Chapinha", "Pérgola", "La Dorni"]
    lista_precos = [60, 80, 120]
    quantidade_garrafas = [0, 0, 0]
    endereco = solicitar_endereco()
    
    if verificar_idade():
        valor_total = realizar_compra(lista_vinhos, lista_precos, quantidade_garrafas)
        mostrar_resumo_compra(lista_vinhos, quantidade_garrafas, valor_total, frete=20)

if __name__ == "__main__":
    main()    
