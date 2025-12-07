qtd = int(input("Quantos alunos serão cadastrados? "))

nomes = []
notas = []

for _ in range(qtd):
    nome = input("Nome do aluno: ")
    nota = float(input("Nota do aluno: "))

    nomes.append(nome)
    notas.append(nota)

print("\n--- BOLETIM COMPLETO ---")
for i in range(qtd):
    print(f"{nomes[i]} - Nota: {notas[i]}")

print("\n--- ALUNOS COM NOTA ≥ 7 ---")
for i in range(qtd):
    if notas[i] >= 7:
        print(f"{nomes[i]} - Nota: {notas[i]}")