qtd = int(input("Quantos números deseja informar? "))

numeros = []

for _ in range(qtd):
    n = float(input("Digite um número: "))
    numeros.append(n)

print("Maior número:", max(numeros))
print("Menor número:", min(numeros))
print("Quantidade informada:", len(numeros))