movimentacoes = []

def adicionar_receita():
    print("========================================")
    print("          ADICIONAR RECEITA")
    print("========================================")
    descricao = input("Descrição: ")
    categoria = input("Categoria: ")
    valor = float(input("Valor: R$"))

    receita = {
        "tipo": "Receita",
        "descricao": descricao,
        "categoria": categoria,
        "valor": valor
    }

    movimentacoes.append(receita)
    print("Receita cadastrada com sucesso!")

def adicionar_despesa():
    print("========================================")
    print("         ADICIONAR DESPESA")
    print("========================================")
    descricao = input("Descrição: ")
    categoria = input("Categoria: ")
    valor = float(input("Valor: R$"))

    despesa = {
        "tipo": "Despesa",
        "descricao": descricao,
        "categoria": categoria,
        "valor": valor
    }

    movimentacoes.append(despesa)
    print("Despesa cadastrada com sucesso!")

def listar_movimentacoes():
    print("========================================")
    print("             MOVIMENTAÇÕES")
    print("========================================")
    for movimentacao in movimentacoes:

        print(f"Tipo: {movimentacao['tipo']}")
        print(f"Descrição: {movimentacao['descricao']}")
        print(f"Categoria: {movimentacao['categoria']}")
        print(f"Valor: R$ {movimentacao['valor']:.2f}")
        print("----------------------------------------")

def resumo_financeiro():
    print("=========================================")
    print("          RESUMO FINANCEIRO")
    print("==========================================")

    total_receitas = 0
    total_despesas = 0

    for movimentacao in movimentacoes:

        if movimentacao["tipo"] == "Receita":
            total_receitas += movimentacao["valor"]
        elif movimentacao["tipo"] == "Despesa":
            total_despesas += movimentacao["valor"]

    saldo = total_receitas - total_despesas

    print(f"Total receitas: {total_receitas}")
    print(f"Total despesas: {total_despesas}")
    print(f"Saldo: {saldo:.2f}")


def menu():
    print("========================================")
    print("         CONTROLE FINANCEIRO")
    print("========================================")
    print("1 - Adicionar receita")
    print("2 - Adicionar despesa")
    print("3 - Listar movimentações")
    print("4 - Resumo financeiro")
    print("0 - Sair")

while True:
    menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_receita()

    elif opcao == "2":
        adicionar_despesa()

    elif opcao == "3":
        listar_movimentacoes()

    elif opcao == "4":
        resumo_financeiro()

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")