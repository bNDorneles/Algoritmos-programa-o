n1 =  int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numeuro: "))

# Recebe cada numero e armazena em suas variaveis


if n1 > n2 and n1 > n3:
    print(f"O primeiro numero é o maior, sendo ele {n1}: ")
elif n2 > n1 and n2 >n3:
    print(f"O Segundo numero é o maior, sendo ele {n2}: ")
elif n3 > n1 and n3 > n2:
    print(f"O terceiro numero é o maior, sendo ele {n3}: ")
elif n1 == n2 == n3:
    print("Os números são iguais")


