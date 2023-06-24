nome = str(input('Qual é o seu nome?'))
altura = float(input('Qual é a sua altura?(em M)'))
peso = float(input('Qual é seu peso?(em Kgs)'))
imc= peso / (altura *altura)

if imc < 18.5:
    print(f'{nome} tem {altura} de altura, pesa {peso} e seu IMC é de {imc} e está abaixo do peso normal')
elif 18.5 <= imc < 25:
    print(f'{nome} tem {altura} de altura, pesa {peso} e seu IMC é de {imc} e está na faixa de peso normal')
elif 25 <= imc < 30:
    print(f'{nome} tem {altura} de altura, pesa {peso} e seu IMC é de {imc} e está acima do peso')
elif 30 <= imc < 40:
    print(f'{nome} tem {altura} de altura, pesa {peso} e seu IMC é de {imc} e está com obesidade')
else:
    print(f'{nome} tem {altura} de altura, pesa {peso} e seu IMC é de {imc} e está com obesidade MÓRBIDA')
    
    

    