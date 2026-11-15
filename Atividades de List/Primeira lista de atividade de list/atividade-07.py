lista_numero= []
qt_vezes= int(input('quantos números vc quer digitar?'))
cont=0

while cont< qt_vezes:
    numero= int(input('Número:'))
    lista_numero.append(numero)
    cont=cont+1
print(f'lista: {lista_numero}')