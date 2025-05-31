temperatura =  float(input("Digite a temperatura: "))
unidade = input("Digite a unidade, sendo C para Celsius e F para Fahrenheit: ")

if unidade == 'C':
    convertida = (temperatura * 9/5) + 32
    print(f"A {temperatura} em C° é igual a {convertida:.2f}")

elif unidade == 'F':
    convertida = (temperatura - 32 ) * 5/9
    print(f"A temperatura {temperatura} em F° é igual a {convertida:.2f}")

