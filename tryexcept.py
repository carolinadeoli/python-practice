"""
Try/Except
try--> tentar executar o código
except --> ocorreu erro ao tentar executar
If/else --> faz checagem de condições, não evita exceções
try/except --> se erro em try executa except - fail fast-
"""
numero_str = input('Irei dobrar o número que você digitar: ')

try:
    numero_float = float(numero_str)
    print('FLOAT: ', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2}')
except:
    print('Isso não é um número')