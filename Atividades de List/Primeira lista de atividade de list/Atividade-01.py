lista= []
qtmaiorquemedia=0
cont= 0 
soma=0
while cont < 4: #vai loopar 4 vezes 
    lista.append(int(input('Digite o número'))) #vai adicionar um número na lista que o usuário digitar
    soma= soma + lista[cont] #soma o valor guardado no índice 'cont' q no primeiro loop é 0
    cont=cont+1
media= soma/4
print(f'media {media}')

cont=0
while cont<4:
    if lista[cont]> media: #compara o valor no indice de cont se é maior doq o valor em média
        qtmaiorquemedia= qtmaiorquemedia+1
    cont=cont+1
print(f'qt maiores q a media {qtmaiorquemedia}')