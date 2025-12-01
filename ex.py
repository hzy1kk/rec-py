n = int(input("Digite um número inteiro: "))

if n % 2 == 0:
    print(f"{n} é par")
else:
    print(f"{n} é ímpar")

    idade = int(input("Digite a idade: "))

if idade < 12:
    print("criança")
elif idade <= 17:
    print("adolescente")
elif idade <= 59:
    print("adulto")
else:
    print("idoso")

    n = int(input("Digite um número positivo: "))

for i in range(n, -1, -1):
    print(i)

    soma = 0

while True:
    x = float(input("Digite um número (0 para parar): "))
    if x == 0:
        break
    if x > 0:
        soma += x

print(f"Soma total: {soma}")


senha_correta = "python123"

while True:
    s = input("Digite a senha: ")
    if s == senha_correta:
        print("Acesso permitido")
        break
    else:
        print("Senha incorreta, tente novamente")

        frase = input("Digite uma frase: ").lower()
vogais = "aeiou"
cont = 0

for letra in frase:
    if letra in vogais:
        cont += 1

print(f"Número de vogais: {cont}")

itens = []

print("Digite itens (digite 'fim' para encerrar):")

while True:
    item = input("> ")
    if item.lower() == "fim":
        break
    itens.append(item)

print("\nLista completa:")
for i, item in enumerate(itens, 1):
    print(f"{i}. {item}")

    qtd = int(input("Quantos números quer informar? "))
numeros = []

for i in range(qtd):
    x = float(input(f"Digite o {i+1}º número: "))
    numeros.append(x)

print("Maior número:", max(numeros))
print("Menor número:", min(numeros))

frase = input("Digite uma frase: ")

palavras = frase.split()

print(f"Quantidade de palavras: {len(palavras)}")
print("Lista de palavras:", palavras)

n = int(input("Quantos alunos serão cadastrados? "))

nomes = []
notas = []

for i in range(n):
    nome = input(f"Nome do aluno {i+1}: ")
    nota = float(input(f"Nota do aluno {nome}: "))
    nomes.append(nome)
    notas.append(nota)

print("\nBoletim completo:")
for nome, nota in zip(nomes, notas):
    print(f"{nome}: {nota}")

print("\nAlunos com nota >= 7:")
for nome, nota in zip(nomes, notas):
    if nota >= 7:
        print(f"{nome}: {nota}")