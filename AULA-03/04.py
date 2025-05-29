idade = int(input("Digite a sua idade: "))

if idade <= 12:
    print(f"A idade é {idade}, você é CRIANÇA!")

elif idade <= 17:
    print(f"A idade é {idade}, você é ADOLESCENTE!")

elif idade <= 60:
    print(f"A idade é {idade}, você é ADULTO!")

else :
    print(f"A idade é {idade}, você é IDOSO!")