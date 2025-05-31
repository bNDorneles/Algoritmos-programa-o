#Escrever um programa que lê um inteiro positivo n e calcula a soma de 1 + 2 + … + n usando for. Ao final, mostrar o valor total.

numero = int(input("Digite um número inteiro positivo: "))

if numero <= 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    soma = 0
    for i in range(1, numero + 1):
        soma += i
    
    print(f"A soma de 1 até {numero} é: {soma}")