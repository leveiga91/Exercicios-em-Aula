<<<<<<< HEAD
usuario_correto = 'admin'
senha_correta = 'senai2026'

max_tentativa = 3

tentativa = 0

while tentativa < max_tentativa:
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Acesso liberado!")
        break
    else:
        tentativa += 1
        restante = max_tentativa -  tentativa
        print(f"Credenciais inválidas. Tentativas restantes: {restante}")
else:
=======
usuario_correto = 'admin'
senha_correta = 'senai2026'

max_tentativa = 3

tentativa = 0

while tentativa < max_tentativa:
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Acesso liberado!")
        break
    else:
        tentativa += 1
        restante = max_tentativa -  tentativa
        print(f"Credenciais inválidas. Tentativas restantes: {restante}")
else:
>>>>>>> d2bd66742168fa7ce420d714a321d36f923db085
    print("Conta bloqueada! Contate o suporte.")