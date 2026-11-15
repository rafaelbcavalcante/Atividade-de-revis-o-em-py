lista = [10, 5, 8, 20, 50, 10, 5, 8, 8, 60, 10, 5, 5, 3, 50] 
cont=0
listaA=[]
listab=[]
while cont < len(lista):
    if (lista[cont] % 2) == 0: #compara se o valor de lista no índice de cont é par e adiciona na lista A
        listaA.append(lista[cont])
    else: #se não for par adiciona na lista b
        listab.append(lista[cont])
    cont=cont+1
print(f'Par: {listaA}')
print(f'Impar: {listab}')