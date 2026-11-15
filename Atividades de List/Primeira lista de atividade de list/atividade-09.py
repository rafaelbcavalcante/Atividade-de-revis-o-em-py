lista_num=[]
cont=0
maior=0
menor=0
while cont < 10:
    num= int(input('digite o número'))
    lista_num.append(num)
    if num > maior: 
        maior= num
        maior_lista= len(lista_num)-1 #guarda o índice do valor dentro da lista
    cont= cont+1
print(f'o maior número da lista é: {maior} no índice {maior_lista}')
