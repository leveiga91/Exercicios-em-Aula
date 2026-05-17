#ENTRADA

print("="*30)
print(" "*10 + "BOLETIM")
print("="*30)

nome_aluno = input("Informe o nome do aluno: ")
media = 7

#notas do aluno:
portugues = float(input("Nota em Portugues: "))
matematica = float(input("Nota em Matemática: "))
geografia = float(input("Nota em Geografia: "))
artes = float(input("Nota em Artes: "))

#PROCESSAMENTO

situacao = (portugues + matematica + geografia + artes) / 4

print(f"Nota final do aluno(a): {situacao}")

if situacao >= media:
    print("Aprovado!")
elif situacao >= 5.0:
    print("Recuperação!")
else:
    print("Reprovado!")