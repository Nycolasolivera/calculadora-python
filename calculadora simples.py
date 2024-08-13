import os

def titulo_programa():
    print('='*51)
    print('=============== calculadora simples ===============')
    print('='*51)

def retorna_menu():
    input('aperte ENTER para voltar ao menu: ')
    main()

def calculo_soma():
    os.system('cls')
    titulo_programa()
    valor_a = int(input('Digite o Primero Valor: '))
    valor_b = int(input('Digite o Segundo Valor: '))
    resultado = valor_a + valor_b
    print(f'{valor_a} + {valor_b} = {resultado}')
    retorna_menu()

def calculo_subtracao():
    os.system('cls')
    titulo_programa()
    valor_a = int(input('Digite o Primero Valor: '))
    valor_b = int(input('Digite o Segundo Valor: '))
    resultado = valor_a - valor_b
    print(f'{valor_a} - {valor_b} = {resultado}')
    retorna_menu()

def calculo_multiplicacao():
    os.system('cls')
    titulo_programa()
    valor_a = int(input('Digite o Primero Valor: '))
    valor_b = int(input('Digite o Segundo Valor: '))
    resultado = valor_a * valor_b
    print(f'{valor_a} x {valor_b} = {resultado}')
    retorna_menu()

def calculo_divisao():
    os.system('cls')
    titulo_programa()
    valor_a = int(input('Digite o Primeiro Valor: '))
    valor_b = int(input('Digite o Segundo Valor: '))
    if valor_b == 0:
        print('Erro: Divisão por zero não é permitida!')
    else:
        resultado = valor_a / valor_b
        print(f'{valor_a} ÷ {valor_b} = {resultado}')
    retorna_menu()

def finalizar_app():
    os.system('cls')
    print('Encerrando o programa...')
    exit()

def menu():
    while True:
        os.system('cls')
        titulo_programa()
        print('1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Fechar Programa')
        opcao = int(input('Digite o número da opção escolhida: '))

        if opcao == 1:
            calculo_soma()
        elif opcao == 2:
            calculo_subtracao()
        elif opcao == 3:
            calculo_multiplicacao()
        elif opcao == 4:
            calculo_divisao()
        elif opcao == 5:
            finalizar_app()
        else:
            print('Opção inválida! Tente novamente.')


def main():
    os.system('cls')
    titulo_programa()
    menu()

if __name__ == '__main__':
    main()

 