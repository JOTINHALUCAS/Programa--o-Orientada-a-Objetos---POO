def menu():
    print('=== MENU ===')
    print('1 - Depositar')
    print('2 - Sacar')
    print('3 - Ver saldo')
    print('4 - Ver histórico de transações')
    print('5 - Sair')
    print('==========')


saldo_inicial = 1000.00
transacoes = []
saldo_atual = saldo_inicial

parar = True
menu()

while parar:
    menu()
    op = input('Escolha uma das opções do menu:')
    if (op == '1'):
        depo = float(input('Quando que você deseja depositar?'))
        saldo_atual += depo
        transacoes.append(+depo)
        escolha = input("Você deseja parar?[S/N]").upper()
        if escolha == 'S':
            parar = False
            print('Parando...')
           

    if (op == '2'):
        sac = float(input('Quanto você deseja sacar?'))
        if sac > saldo_atual:
            print('Impossivél sacar esse valor')
            print('Tente novamente')
            if escolha == 'S':
                parar = False
                print('Parando...')
            
        else:
            saldo_atual -=  sac
            transacoes.append(-sac)
            escolha = input("Você deseja parar?[S/N]").upper()
            if escolha == 'S':
                parar = False
                print('Parando...')

    if (op == '3'):
        print(f'O saldo atual é: {saldo_atual:.2f}')
        escolha = input("Você deseja parar?[S/N]").upper()
        if escolha == 'S':
            parar = False
            print('Parando...')

    if (op == '4'):
        print(f'Você fez um total de {len(transacoes)} transações')
        print('TRANSAÇÕES')
        for t in transacoes:
            print(f'R${t:.2f}')
        escolha = input("Você deseja parar?[S/N]").upper()
        if escolha == 'S':
            parar = False
            print('Parando...')

    elif (op == '5'):

        print('Saindo...')
        parar = False
    
    else:
        print('Opção invalida, Tente novamente')

            


