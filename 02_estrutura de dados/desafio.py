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


def verifica_cpf(cpf):
    if not cpf.isdigit() or len(cpf) != 11:
        print("CPF inválido! Deve conter 11 números.")
        return False
    return True


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_limite_saques = numero_saques >= 3

    if excedeu_saldo:
        print("Valor de saque excedeu o saldo disponível em conta!")
    elif excedeu_limite:
        print(f"Valor de saque excedeu o limite de R${limite:.2f}!")
    elif excedeu_limite_saques:
        print("Excedeu limite diário de saques!")
    else:
        saldo -= valor
        extrato += f"Saque:   R${valor:.2f}\n"
        numero_saques += 1
    return saldo, extrato, numero_saques

def criar_usuario(usuarios):
    cpf = input("Digite seu cpf (somente números): ").strip()
    if not verifica_cpf(cpf):
        return
    existe_usuario = verificar_usuarios(cpf, usuarios)
    if existe_usuario:
        print("Já existe usuário com esse CPF!")
        return
    
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco, "cpf": cpf})


def criar_conta(agencia, usuarios, contas):
    cpf = input("Digite o CPF: ")
    if not verifica_cpf(cpf):
        return
    usuario_verificado = verificar_usuarios(cpf, usuarios)
    if not usuario_verificado:
        print("Não há usuário com esse CPF!")
        return
    conta = len(contas) + 1
    contas.append({"AGENCIA": agencia, "conta": conta, "usuario": usuario_verificado})
    print("Conta Criada com sucesso!")


def verificar_usuarios(cpf, usuarios):
    usuario_verificado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_verificado[0] if usuario_verificado else None

def listar_contas(contas):
    for conta in contas:
        print(f"""
            Agencia: {conta["AGENCIA"]}\n
            Conta: {conta["conta"]}\n
            Usuário: {conta["usuario"]["nome"]}\n
            """)
    
    
def exibir_extrato(saldo, /, *, extrato): 
    print("+===========Extrato===========+")
    print("Não há transação" if not extrato else extrato)
    print(f"\nSaldo:  R${saldo:.2f}")
    print("+=============================+")


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Valor a ser depositado: R$"))
            
            saldo, extrato = deposito(saldo, valor, extrato)
            
        elif opcao == "s":
            valor = float(input("Valor a ser sacado: R$"))
            
            saldo, extrato, numero_saques = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "nc":
            criar_conta(AGENCIA, usuarios, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()

