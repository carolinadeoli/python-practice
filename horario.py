hora = input('Digite a hora em números inteiros: ')

try:
    horario = int(hora)

    if horario >= 0 and horario <= 4:
        print('Boa madrugada!')
    elif horario >= 5 and horario <= 12:
        print('Bom dia!')
    elif horario >=13 and horario <= 18:
        print('Boa tarde!')
    elif horario >=19 and horario <=23:
        print('Boa noite!')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')
