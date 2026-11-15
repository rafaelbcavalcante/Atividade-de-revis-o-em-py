listaProdutos = ['Caderno', 'Caneta', 'Lápis', 'Borracha', 'Mochila', 'Régua'] 
listaPrecos = [18.0, 2.5, 1.5, 3.0, 120.0, 4.5] 

cont=0

while cont < len(listaPrecos):
    listaPrecos[cont]= listaPrecos[cont]+1 #adiciona um em todos os itens
    cont=cont+1
print(listaPrecos)

cont=0
soma=0
while cont < len(listaPrecos):
    soma= soma + listaPrecos[cont] #soma os itens

    cont=cont+1
media= soma/len(listaPrecos)
print(f'media: {media}')
listaPrecos.append(15)
listaProdutos.append('estojo')
print(listaProdutos)
print(listaPrecos)