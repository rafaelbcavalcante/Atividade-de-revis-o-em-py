lista=[]
cont=0

while cont < 10:
    num=int(input('Digite o número'))
    lista.append(num)
    cont=cont+1
print(f'{lista}')

cont=0

while cont < 10:
    if cont < 5:
        lista[cont]= lista[cont]*2
    else:
        lista[cont]=lista[cont]/2
    cont=cont+1
print(lista)