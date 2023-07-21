lista = ["Item: Celular"" ", "Valor: R$900,00 "   , "Quantidade: 5 "   , "Item: Tablet"" " , "Valor: R$800,00 "  , "Quantidade: 5", "Item: Computador"" ", "Valor: R$1500,00 " , "Quantidade: 10 "]
print("Seja bem-vindo")
usuario = input("Digite seu usuario para continuar: ")
print(f"Olá {usuario} esse é sue menu de opções")
while True:
    print("===== MENU DE OPÇÕES =====")
    print("1. Adicionar produtos")
    print("2. Atualizar produtos")
    print("3. Visualizar estoque")
    print("0. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        item = str(input("Digite o nome do item: "))
        valor = str(input("Digite o valor: "))
        quantidade = str(input("Digite a quantidade em estoque: "))
        lista.append("Item: " + item + " ")
        lista.append("valor: R$" + valor + " ")
        lista.append("Quantidade: " + quantidade + " ")
        
        
    elif escolha == "2":
        item_atualizar = str(input("Digite o nome do item: "))
        novo_valor = str(input("Digite o valor: "))
        novo_quantidade = str(input("Digite a quantidade em estoque: "))
        indice = lista.index ("Item: " + item_atualizar + " ")
        novo_indice = indice + 1
        novo_indice_quantidade = novo_indice
        
        valor_deletar = novo_indice
        quantidade_deletar = novo_indice_quantidade
        for i in range(len(lista)):
            if lista[novo_indice] == item_atualizar:
                lista[novo_indice] = novo_valor
                break
        del lista[valor_deletar]
        for i in range(len(lista)):
            if lista[novo_indice_quantidade] == item_atualizar:
                lista[novo_indice_quantidade] = novo_quantidade
                break

        del lista[quantidade_deletar]
        lista.insert(novo_indice_quantidade," " + "Quantidade: " + novo_quantidade)
        lista.insert(novo_indice," " +  "Valor: R$" + novo_valor)
        
        
        
        
    elif escolha == "3":
        for i, elemento in enumerate(lista, start=1):
            print(elemento, end="")
            if i % 3 == 0:
                print()
        
        
    elif escolha == "0":
        print("Saindo do programa...")
        break
    
    else:
        print("Opção inválida. Por favor, escolha novamente.\n")

    
    
    
   
    