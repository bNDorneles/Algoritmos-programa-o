altura =  float(input("Digite a sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso/(altura * altura)

if imc < 18.5:
    print(f"A seu imc é: {imc:.2f}, você está abaixo do peso!")

elif imc >= 18.5 and imc <= 24.9:
    print(f"A seu imc é: {imc:.2f}, você está no peso normal!")

elif imc >= 25 and imc <= 29.9:
    print(f"A seu imc é: {imc:.2f}, você está acima do peso!")

elif imc >= 30 and imc <= 34.9:
    print(f"A seu imc é: {imc:.2f}, você está com obsidade grau 1!")

elif imc >= 35 and imc <= 39.9:
    print(f"A seu imc é: {imc:.2f}, você está com obsidade grau 2!")

elif imc >= 40:
    print(f"A seu imc é: {imc:.2f}, você está com obsidade grau 3!")
