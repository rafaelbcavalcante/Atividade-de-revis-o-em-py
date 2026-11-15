numeros = [10, 20, 30, 20, 30, 30, 10, 40, 50, 10, 60, 10, 10]
cont=0
qtaparece=0
num=int(input('Qual item da lista?'))

#dentro desse while, ele analisa cada item e compara com o if se é igual ou não 
while cont < len(numeros): 
    if num == numeros[cont]:
        qtaparece=qtaparece+1
    cont=cont+1
#esse if é o responsável por mostrar se o item aparece e quantas vezes ou se não aparece
if qtaparece>0:
    print(f'Quantidade de vezes q o número aparece: {qtaparece}')  
else:
    print('O número não aparece')
