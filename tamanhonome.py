nome = input('Qual é o seu nome? ')
tamanho__nome = len(nome)

if tamanho__nome >= 1: 
    if tamanho__nome <=4:
        print('Seu nome é curto')
    elif tamanho__nome >=5 and tamanho__nome<=6:
        print('Seu nome tem tamanho médio')
    else:
        print('Seu nome é longo')
else:
   print('Você precisa digitar mais de uma letra') 