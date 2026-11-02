lista= []
qtmaiorquemedia=0
cont= 0 
soma=0
while cont < 4:
    lista.append(int(input('Digite o número')))
    soma= soma + lista[cont]
    cont=cont+1
media= soma/4
print(f'media {media}')

cont=0
while cont<4:
    if lista[cont]> media:
        qtmaiorquemedia= qtmaiorquemedia+1
    cont=cont+1
print(f'qt maiores q a media {qtmaiorquemedia}')