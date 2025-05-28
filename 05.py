VT = float(input("Digite o valor total de itens: "))
PG = int(input("Digite a porcentagem de gorjeta: "))

VG = VT * (PG/100)
VFC = VT + VG


print(f"Valor dos itens: {VT}")
print(f"Valor da gorjeta ({PG}%): R$ {VG}")
print(f"Valor total a pagar: {VFC}")