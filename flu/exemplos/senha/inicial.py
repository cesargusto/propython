print("Bem-Vindo ao Sistema")
users = ["juca","mara"]
admins = ["root","jota"]
while True:
    login = raw_input("Entre seu login: ")
    if login in admins:
        print("Ola administrador %s"%login)
        break
    elif login in users:
        print("Bem vindo usuario %s"%login)
        break
    else:
        print("Login Invalido")
print("estamos fora o while")

