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
