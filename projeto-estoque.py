lista = ["celular - valor: 900,00 - quantidade - 3", "tablet - valor: 700,00 - quantidade - 5"]

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
        lista.extend([item, valor, quantidade])
        # Faça algo relacionado à opção 1
        
    elif escolha == "2":
        print("Você escolheu a opção 2.")
        # Faça algo relacionado à opção 2
        
    elif escolha == "3":
        print(lista)
        # Faça algo relacionado à opção 3
        
    elif escolha == "0":
        print("Saindo do programa...")
        break
    
    else:
        print("Opção inválida. Por favor, escolha novamente.\n")

    
    
    
   
    