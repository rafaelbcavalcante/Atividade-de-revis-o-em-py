'''Uma loja deseja analisar as vendas do dia. Faça um programa que leia, para cada venda realizada, o valor da venda, o nome do vendedor e o tipo de pagamento (pix, cartão de crédito ou cartão de débito), encerrando a leitura quando for digitado o valor 0 (flag) para a venda, que não deve entrar nos cálculos. Ao final, apresente: 

o valor total vendido no dia; 

o valor médio das vendas realizadas com cartão de crédito; 

a quantidade de vendas acima de R$ 1000.00 pagas com pix; 

o nome do vendedor que fez a maior venda (considere que não há empate). '''


valor= float(input('Qual o valor da venda?:'))
qtmais_1000=0
qt_vendas=0
valor_total=0
maior_venda=0
vendas_pix=0

while valor>0:
    nome=input('Nome do comprador:')
    forma_pagamento= input('Qual a forma de pagamento? (pix,débito ou crédito?)')
    print('******************************')
    qt_vendas= qt_vendas+1
    valor_total= valor_total+valor
    if valor > 1000:
        qtmais_1000= qtmais_1000 +1
    if valor > maior_venda:
        maior_venda= valor
        nome_maior= nome
    if forma_pagamento == 'pix':
        vendas_pix=vendas_pix+1
    valor= float(input('Qual o valor da venda?:'))
media= valor_total/qt_vendas
print(f'Valor total vendido: {valor_total}')
print(f'valor médio: {media}')
print(f'Quantidade de vendas acima de R$1000: {qtmais_1000}')
print(f'Vendedor com o maior venda: {maior_venda}')
print(f'Quantidade de pessoas que pagaram com pix: {vendas_pix}')