

salario = float(input("Digite o salario: "))
aumento = int(input("Digite o aumento: "))

valor_aumento = salario * (aumento/100)
valor_final = salario + valor_aumento


print(f"Valor dos itens: {salario}")
print(f"Valor da gorjeta ({aumento}%): R$ {valor_aumento}")
print(f"Valor total a pagar: {valor_final}")