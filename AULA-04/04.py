print("Digite números inteiros positivos (digite 0 para parar):")

soma_pares = 0
produto_impares = 1  # Inicializado com 1 para o produto
quantidade = 0
tem_impares = False  # Flag para verificar se houve números ímpares

while True:
    numero = int(input("Número: "))
    
    if numero == 0:
        break  # Sai do loop quando digitar 0
    
    if numero < 0:
        print("Por favor, digite apenas números positivos ou zero para encerrar.")
        continue  # Ignora números negativos
    
    quantidade += 1
    
    if numero % 2 == 0:  # Número par
        soma_pares += numero
    else:  # Número ímpar
        produto_impares *= numero
        tem_impares = True

# Exibe os resultados
print(f"\nQuantidade de números lidos: {quantidade}")
print(f"Soma dos números pares: {soma_pares}")

if tem_impares:
    print(f"Produto dos números ímpares: {produto_impares}")
elif quantidade > 0:  # Caso tenha números, mas nenhum ímpar
    print("Não foram digitados números ímpares.")
else:
    print("Nenhum número positivo foi digitado.")