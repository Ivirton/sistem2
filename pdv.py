import os

# Estoque inicial (exemplo)
estoque = {
    "1": {"nome": "Arroz", "preco": 5.50, "quantidade": 50},
    "2": {"nome": "Feijão", "preco": 7.20, "quantidade": 30},
    "3": {"nome": "Macarrão", "preco": 3.80, "quantidade": 40},
}

caixa = 0.0
vendas = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def listar_produtos():
    print("\n=== Produtos Disponíveis ===")
    for codigo, produto in estoque.items():
        print(f"Código: {codigo} | Produto: {produto['nome']} | Preço: R${produto['preco']:.2f} | Estoque: {produto['quantidade']} unidades")
    print("============================\n")

def registrar_venda():
    global caixa
    carrinho = []
    total = 0.0

    while True:
        listar_produtos()
        codigo = input("Digite o código do produto (ou '0' para finalizar): ")
        if codigo == "0":
            break
        if codigo not in estoque or estoque[codigo]["quantidade"] == 0:
            print("Produto inválido ou fora de estoque.")
            continue

        try:
            quantidade = int(input(f"Digite a quantidade de '{estoque[codigo]['nome']}' desejada: "))
        except ValueError:
            print("Quantidade inválida.")
            continue

        if quantidade > estoque[codigo]["quantidade"]:
            print("Quantidade insuficiente no estoque.")
            continue

        subtotal = quantidade * estoque[codigo]["preco"]
        carrinho.append((estoque[codigo]["nome"], quantidade, subtotal))
        total += subtotal
        estoque[codigo]["quantidade"] -= quantidade
        print(f"{estoque[codigo]['nome']} adicionado ao carrinho. Subtotal: R${subtotal:.2f}\n")

    if total > 0:
        print("\n=== Carrinho de Compras ===")
        for item in carrinho:
            print(f"Produto: {item[0]} | Quantidade: {item[1]} | Subtotal: R${item[2]:.2f}")
        print(f"Total da compra: R${total:.2f}")
        
        pagamento = float(input("Digite o valor pago pelo cliente: R$"))
        troco = pagamento - total
        if troco < 0:
            print("Valor insuficiente para realizar a compra.")
            return

        caixa += total
        vendas.append({"itens": carrinho, "total": total})
        print(f"Troco: R${troco:.2f}")
        print("Venda registrada com sucesso!")

def consultar_caixa():
    print("\n=== Resumo do Caixa ===")
    print(f"Total em caixa: R${caixa:.2f}")
    print("=======================\n")

def consultar_vendas():
    print("\n=== Histórico de Vendas ===")
    for i, venda in enumerate(vendas, 1):
        print(f"Venda #{i}:")
        for item in venda["itens"]:
            print(f"  Produto: {item[0]} | Quantidade: {item[1]} | Subtotal: R${item[2]:.2f}")
        print(f"  Total: R${venda['total']:.2f}")
    print("===========================")

def menu():
    while True:
        limpar_tela()
        print("=== Sistema PDV ===")
        print("1. Listar produtos")
        print("2. Registrar venda")
        print("3. Consultar caixa")
        print("4. Consultar histórico de vendas")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_produtos()
        elif opcao == "2":
            registrar_venda()
        elif opcao == "3":
            consultar_caixa()
        elif opcao == "4":
            consultar_vendas()
        elif opcao == "5":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida!")

        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    menu()
