num = input("Digite um número inteiro: ")

if num.isdigit():
    num_int = int(num)
    par_impar = num_int % 2 ==0 
    par_impar_texto = 'impar'
    if par_impar:
        par_impar_texto = 'par'
    print(f' O número {num_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')

