texto = input("Digite uma string: ")

print("Caracteres da string com suas posições:")
for indice, caractere in enumerate(texto, start=1):
    print(f"Posição {indice}: '{caractere}'")