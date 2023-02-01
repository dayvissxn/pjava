nome = ""

senha = ""

while nome == senha:
    nome = input("Informe o nome de usuario: ")
    senha = input("Informe a senha de usuario: ")
    if senha == nome:
        print("Invalido")
    else:
        print("Valido")