lista = ["celular", "900.00, 5", "tablet", "800.00, 5"]

while True:
    print("===== MENU DE OPÇÕES =====")
    print("1. Adicionar produtos")
    print("2. Atualizar produtos")
    print("3. Visualizar estoque")
    print("0. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        item = str(input("Digite item desejado: "))
        valor = float(input("Digite o valor desejado: "))
        quantidade = int(input("Digite a quantidade desejada: "))
        valor_quantidade = [valor , quantidade]
        lista.append(item)
        lista.append(valor_quantidade)
        # Faça algo relacionado à opção 1
        
    elif escolha == "2":
        item_atualizar = input("item desejado")
        
        indice = lista.index(item_atualizar)
        novo_indice = indice + 1
        novo_valor = input("digite o valor desejado")
        valor_deletar = novo_indice
        for i in range(len(lista)):
            if lista[novo_indice] == item_atualizar:
                lista[novo_indice] = novo_valor
                break
        
        del lista[valor_deletar]
        
        
        
        
        lista.insert(novo_indice, novo_valor)
        
    elif escolha == "3":
        print(lista)
        
        
    elif escolha == "0":
        print("Saindo do programa...")
        break
    
    else:
        print("Opção inválida. Por favor, escolha novamente.\n")

    
    
    
   
    