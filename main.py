import os
from datetime import date

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    menu = f"""
    ===================================
    Bem-vindo(a) ao FUNAY BANK!
    ===================================
    Saldo atual: R$ {saldo:.2f}
    ===================================
    Escolha uma das opções abaixo:

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair

    ===================================

    => """

    os.system('clear')
    opcao = input(menu)

    if opcao == "1":
        os.system('clear')
        print('=============================================================')
        valor_deposito = input("digite o valor que deseja depositar em seu fundinho: ")

        if valor_deposito.isdigit():
            
            valor_deposito = float(valor_deposito)
            print(valor_deposito)

            if valor_deposito > 0:

                saldo += valor_deposito
                extrato += f"Depósito: R$ {valor_deposito:.2f}\n"

                os.system('clear')
                print('=============================================================')
                print(f'Deposito no valor de R${valor_deposito:.2f} feito com sucesso')
                print('=============================================================')
                print(saldo)
                qualquer_valor = input("Aperte qualquer tecla para continuar: ")

            else:
                os.system('clear')
                print('=============================================================')
                print("Operação falhou! O valor informado é inválido.")
                print('=============================================================')
                qualquer_valor = input("Aperte qualquer tecla para continuar: ")

        else:
            os.system('clear')
            print('=============================================================')
            print("Operação falhou! Digite apenas números.")
            print('=============================================================')
            qualquer_valor = input("Aperte qualquer tecla para continuar: ")

    elif opcao == "2":
        os.system('clear')
        print('=============================================================')
        valor_saque = input("digite o valor que deseja sacar do seu fundinho: ")

        if valor_saque.isdigit():

            valor_saque = float(valor_saque)

            excedeu_saldo = valor_saque > saldo

            excedeu_limite = valor_saque > limite

            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                os.system('clear')
                print('=============================================================')
                print("Operação falhou! Você não tem saldo suficiente.")
                print('=============================================================')
                qualquer_valor = input("Aperte qualquer tecla para continuar: ")

            elif excedeu_limite:
                os.system('clear')
                print('=============================================================')
                print("Operação falhou! O valor do saque excede o limite.")
                print('=============================================================')
                qualquer_valor = input("Aperte qualquer tecla para continuar: ")

            elif excedeu_saques:
                os.system('clear')
                print('=============================================================')
                print("Operação falhou! Número máximo de saques excedido.")
                print('=============================================================')
                qualquer_valor = input("Aperte qualquer tecla para continuar: ")
                

            elif valor_saque > 0:
                saldo -= valor_saque
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                numero_saques += 1

            else:
                os.system('clear')
                print('=============================================================')
                print("Operação falhou! O valor informado é inválido.")
                print('=============================================================')
                qualquer_valor = input("Aperte qualquer tecla para continuar: ")
                
        else:
            os.system('clear')
            print('=============================================================')
            print("Operação falhou! Digite apenas números.")
            print('=============================================================')
            qualquer_valor = input("Aperte qualquer tecla para continuar: ")

      
    elif opcao == "3":
        os.system('clear')
        print("\n================= EXTRATO ===================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================================")
        qualquer_valor = input("Aperte qualquer tecla para continuar: ")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")