
while True:
    print()
    print('*='*33)
    print('   Por favor, inserir 2 valores de números binário com 8 digitos')
    print('      Lembrando que o número binário é composto de 0 e 1.')
    print('*='*33)
    print()

    operadores = str(input('''Escolha o tipo de operação de deseja fazer: + - * / %\n'''))

    if operadores in '/' or operadores in '-' or operadores in '+' or operadores in '*' or operadores in '%':
            a = str(input('Digite a 1º valor binário:'))
            lista = [int(d) for d in (a)]

            # lista
            if len(lista) == 8:

                    #lista = [int(d) for d in (a)]
                    soma = 0
                    p = 7
                    for i in range(8):
                       soma = soma + (lista[i] * (2 ** p))
                       p = p - 1

            # lista1
                    b = str(input('Digite o 2º valor binário:'))
                    lista1 = [int(d) for d in (b)]
                    #while len(lista1)==8:
                    soma1 = 0
                    p = 7
                    if len(lista1) == 8:

                            for i in range(8):
                                soma1 = soma1 + (lista1[i] * (2 ** p))
                                p = p - 1

                        # Operadores
                            if operadores == '+':
                                soma3 = soma + soma1
                            elif operadores == '-':
                                soma3 = soma - soma1
                            elif operadores == '*':
                                soma3 = soma * soma1
                            elif operadores == '/':
                                soma3 = int(soma / soma1)
                            elif operadores == '%':
                                soma3 = int(soma % soma1)
                        # converte decimal para binário
                            soma3 = bin(soma3)[2:].zfill(8)
                            print(f'{soma3}')
                            #break


                    cont = str(input('Deseja continuar S ou N? '))

                    if cont not in "Ss" and cont not in "Nn":
                        print('Por favor digitar uma opção válida:')
                        cont = str(input('Deseja continuar S para sim ou N para não? '))
                    if cont in 'Nn':
                        break
    else:

        print('Por favor, inserir um operador válido\nVamos tentar novamente!!!')
        print()




