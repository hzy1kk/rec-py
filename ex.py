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