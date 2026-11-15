lista_numero= []
qt_vezes= int(input('quantos números vc quer digitar?'))
cont=0

while cont< qt_vezes:
    numero= int(input('Número:'))
    if numero <= 0: #esse if analisa o valor digitado e não contabiliza o contador, fazendo ele repetir o código
        print('Número inválido (menor ou igual a 0)')
    else:
        lista_numero.append(numero)
        cont=cont+1
print(f'lista: {lista_numero}') 