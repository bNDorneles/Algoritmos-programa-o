while True:
    print("\nMenu da Calculadora:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")
    
    opcao = input("Digite a opção desejada: ")
    
    if opcao == '0':
        print("Calculadora encerrada. Até logo!")
        break
    
    if opcao not in ('1', '2', '3', '4'):
        print("Opção inválida. Por favor, escolha uma opção de 0 a 4.")
        continue
    
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: Por favor, digite números válidos.")
        continue
    
    if opcao == '1':
        resultado = num1 + num2
        print(f"Resultado: {num1} + {num2} = {resultado}")
    elif opcao == '2':
        resultado = num1 - num2
        print(f"Resultado: {num1} - {num2} = {resultado}")
    elif opcao == '3':
        resultado = num1 * num2
        print(f"Resultado: {num1} * {num2} = {resultado}")
    elif opcao == '4':
        if num2 == 0:
            print("Erro: Divisão por zero não é permitida.")
        else:
            resultado = num1 / num2
            print(f"Resultado: {num1} ÷ {num2} = {resultado}")