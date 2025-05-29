produto =  float(input("Digite o valor do produto: "))
quantidade = float(input("Digite a quantidade de produtos: "))

total_sem_desconto = produto * quantidade

if quantidade <= 10:
   desconto = 0
elif 11 <= quantidade <=20:
   desconto = total_sem_desconto * 0.10
else:
   desconto = total_sem_desconto * 0.20

total_com_desconto = total_sem_desconto - desconto

print(f"Valor sem desconto: R$ {total_sem_desconto:.2f}")
print(f"Desconto aplicado: R$ {desconto:.2f}")
print(f"Valor total a pagar: R$ {total_com_desconto:.2f}")
    