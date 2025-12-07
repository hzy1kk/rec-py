senha_correta = "python123"

while True:
    senha = input("Digite a senha: ")

    if senha == senha_correta:
        print("Acesso permitido")
        break
    else:
        print("Senha incorreta, tente novamente")