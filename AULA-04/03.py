print("Digite números inteiros positivos (digite 0 para parar):")

soma = 0
quantidade = 0

while True:
    numero = int(input("Número: "))
    
    if numero == 0:
        break  # Sai do loop quando digitar 0
    
    if numero < 0:
        print("Por favor, digite apenas números positivos ou zero para encerrar.")
        continue  # Volta para o início do loop
    
    soma += numero
    quantidade += 1

if quantidade > 0:
    media = soma / quantidade
    print(f"\nMédia dos números digitados: {media:.2f}")
else:
    print("\nNenhum número positivo foi digitado.")