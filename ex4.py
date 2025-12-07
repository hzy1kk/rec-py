soma = 0

while True:
    num = int(input("Digite um número (0 para parar): "))
    
    if num == 0:
        break

    if num > 0:
        soma += num

print("Soma dos números positivos:", soma)