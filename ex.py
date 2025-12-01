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