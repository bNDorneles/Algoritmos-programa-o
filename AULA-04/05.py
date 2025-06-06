print("Digite números inteiros (digite -1 para parar):")

soma_positivos = 0
quantidade_negativos = 0

while True:
    try:
        numero = int(input("Número: "))
        
        if numero == -1:
            break  # Encerra o loop quando digitar -1
        
        if numero > 0:
            soma_positivos += numero
        elif numero < 0:
            quantidade_negativos += 1
            
    except ValueError:
        print("Por favor, digite apenas números inteiros.")

# Exibe os resultados
print("\nResultados:")
print(f"Soma dos números positivos: {soma_positivos}")
print(f"Quantidade de números negativos: {quantidade_negativos}")