lista = [10, 5, 8, 20, 50, 10, 5, 8, 8, 60, 10, 5, 5, 3, 50] 
cont=0

while cont < 5: #mostra os 5 primeiros elementos
    print(f'posição - {cont} num- {lista[cont]}')
    cont=cont+1

cont=3

while cont < 8: #mostra do índice 3 ao 7
    print(f'num pos {cont}: {lista[cont]}')
    cont=cont+1

ultimo= len(lista)- 3 #recebe o antepenúltimo índice da lista

while ultimo < len(lista): #esse código faz com que idependente do tamanho da lista, sempre pegue os 3 últimos
    print(f'item {ultimo} num: {lista[ultimo]}')
    ultimo = ultimo+1