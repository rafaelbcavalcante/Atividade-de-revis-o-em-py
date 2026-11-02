'''Foi feita uma pesquisa para determinar o índice de mortalidade infantil em um certo período. Fazer um programa que:  

Leia inicialmente o número de crianças nascidas no período; 

Leia, em seguida, um número indeterminado de linhas, contendo, cada uma, o sexo de uma criança morta (feminino ou masculino) e o número de meses de vida da criança. A última linha, que não entrará nos cálculos, contém um sexo inválido; 

 

Determine e imprima: 

a porcentagem de crianças mortas no período, em relação ao total de nascidos;  

a quantidade de crianças que não chegou a completar um ano de vida; 

a quantidade de crianças do sexo masculino mortas no período, que viveu um ano ou mais.  '''

qt_mortas_mais_um_ano=0
qt_menos_um_ano=0
qt_mortas=0
crianca_nasc=int(input('Quantidade de crianças nascidas:'))
sexo= input('Qual o sexo da criança?')
while (sexo == 'feminino') or (sexo == 'masculino'):
    qt_mortas=qt_mortas+1
    perc_mortas= (qt_mortas*100)/crianca_nasc
    meses_vida= float(input('Meses de vida:'))
    if meses_vida < 12:
        qt_menos_um_ano= qt_menos_um_ano+1
    if (sexo == 'masculino') and (meses_vida >= 12):
        qt_mortas_mais_um_ano= qt_mortas_mais_um_ano+1
    print("************************************")
    sexo= input('Qual o sexo da criança?')
print(f'a porcentagem de crianças mortas no período, em relação ao total de nascidos: {perc_mortas}')
print(f'a quantidade de crianças que não chegou a completar um ano de vida: {qt_menos_um_ano}')
print(f'a quantidade de crianças do sexo masculino mortas no período, que viveu um ano ou mais: {qt_mortas_mais_um_ano}')