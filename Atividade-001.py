'''Uma bióloga marinha registra o comprimento do casco (em cm) das tartarugas que chegam à praia para desovar. Faça um programa que leia o comprimento de cada tartaruga, encerrando a leitura quando for digitado um valor negativo (flag), que não deve entrar nos cálculos. Ao final, apresente: 

a soma de todos os comprimentos; 

a média dos comprimentos; 

a quantidade de tartarugas com casco maior que 100 cm; 

o maior e o menor comprimento digitado. '''

comprimento=0
qt=0
qtmaior100=0
soma=0
maiorc=0
menorc=-1
casco= float(input('Digite o comprimento em cm do casco das tartarugas'))
while casco > -1:
    qt= qt+1
    soma= soma+casco
    if casco >100:
        qtmaior100=qtmaior100+1
    if casco > maiorc:
        maiorc= casco
    if (casco < menorc) or (menorc==-1):
        menorc= casco
    casco=float(input('Digite o comprimento em cm do casco'))
media= soma/qt
print(f'Soma:{soma}')
print(f'Media:{media}')
print(f'Quantidade de cascos maiores que 100:{qtmaior100}')
print(f'Maior casco:{maiorc}')
print(f'Menor casco:{menorc}')
