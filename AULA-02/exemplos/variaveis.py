#variaveis 

# int: Números inteiros (ex: 10, -5, 0). 
#float: Números decimais (ex: 3.14, -0.5).
#str: Texto (ex: "Olá", "Python").
#bool: Verdadeiro ou falso (ex: True, False). 

# definição de função 
# onde estamos definindo a função, incluindo seus paramêtros, corpo e retorno

def minha_func (param1, param2):
    print(param1)
    print(param2)
    return param1 + param2 


# chamada de função 
# onde chamamos a função passando os paramêtros necessários

resultado = minha_func(3,5)
print(resultado) #saida esperada: 8 

# PRINT

print() # imprime uma linha em branco
print("") # imprime uma linha em branco
print("Olá Mundo") # imprime "Olá Mundo"

idade = 27 #atribui o valor 10 à variável
print("Tenho", idade, " Anos") # Imprime "Tenho 27 anos"

print("A soma de 3 e 5 é:" ,3+5) # Imprime: "A soma de 3 e 5 é 8"

# INPUT 

# Lê o nome do usuário e não armazena em nenhuma variável
input("Qual é o seu nome? ")
# Lê o nome do usuário e atribui à variável nome
nome = input("Qual é o seu nome? ")
# Lê uma entrada do usuário sem mostrar mensagem e sem armazenar em variável
input()

#TYPE

int("5")

#Converte o valor de seu argumento para inteiro.

float("5.3")
#Converte o valor de seu argumento para decimal
(float)

str(5)
#Converte o valor de seu argumento para string
#(texto)

bool(1)
#Converte o valor de seu argumento para booleano
#(True ou False)





