def menu():
    escolha = input("""
        +============= Menu =============+
        | [d]   Depositar                |
        | [s]   Sacar                    |
        | [e]   Extrato                  |
        | [nc]  Nova conta               |
        | [lc]  Listar contas            |
        | [nu]  Novo Usuário             |
        | [q]   Sair                     |
        +================================+
        ==> """)
    return escolha

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
        print("\nDepósito realizado com sucesso")
    else:
        print("\nOperação falhou!")
      
    return saldo, extrato
  

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_limite_saques = numero_saques >= 3

    if excedeu_saldo:
        print("Valor de saque excedeu o saldo disponível em conta!")
    elif excedeu_limite:
        print("Valor de saque excedeu o limite de R${limite:.2f}!")
    elif excedeu_limite_saques:
        print("Excedeu limite diário de saques!")
    else:
        saldo -= valor
        extrato += f"Saque:   R${valor:.2f}\n"
    return saldo, extrato
    
    
def exibir_extrato(saldo, /, *, extrato): 
    print("+===========Extrato===========+")
    print("Não há transação" if not extrato else extrato)
    print(f"\nSaldo:  R${saldo:.2f}")
    print("+=============================+")


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Valor a ser depositado: R$"))
            
            saldo, extrato = deposito(saldo, valor, extrato)
            
        elif opcao == "s":
            valor = float(input("Valor a ser sacado: R$"))
            
            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
