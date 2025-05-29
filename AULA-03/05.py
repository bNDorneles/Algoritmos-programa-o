def calcular_aumento(salario):
    if salario <= 1000:
        aumento = salario * 0.20
    elif 1000.01 <= salario <= 2000:
        aumento = salario * 0.15
    elif 2000.01 <= salario <= 3000:
        aumento = salario * 0.10
    else:
        aumento = salario * 0.05
    return aumento

# Entrada do salário
salario = float(input("Digite o salário do funcionário: R$ "))

# Cálculo do aumento
aumento = calcular_aumento(salario)
novo_salario = salario + aumento

# Saída dos resultados
print(f"Salário atual: R$ {salario:.2f}")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")