nome= input("Digite o seu nome:")
encontrar = input("Digite o que deseja encontrar:")

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')