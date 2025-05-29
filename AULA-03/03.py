nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    print(f"A nota do aluno é {nota} e ele esta APROVADO!")

elif nota >= 5:
    print(f"A nota do aluno é {nota} e ele esta RECUPERÇÃO!")

elif nota <= 5:
    print(f"A nota do aluno é {nota} e ele esta REPROVADO!")