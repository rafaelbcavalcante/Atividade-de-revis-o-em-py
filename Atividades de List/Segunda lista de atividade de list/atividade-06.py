listaDias = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb'] 
listaTemperaturas = [28, 31, 30, 30, 33, 29, 35] 
cont=0

while cont < len(listaDias):
    if cont == 0:
        print(f'temperatura domingo: {listaTemperaturas[cont]}, não tem dia anterior')#analisa se está no começo da lista pq não tem dia anterior
    elif cont> 0: 
        diferenca= listaTemperaturas[cont]- listaTemperaturas[cont-1]#calcula a diferença dos valores guardados nos itens da lista
        if diferenca >= 0: #analisa se subiu ou desceu a temperatura
            print(f'{listaDias[cont]} subiu {diferenca} em relação a {listaDias[cont-1]}')
        else:
            print(f'{listaDias[cont]} desceu {diferenca} em relação a {listaDias[cont-1]}')
            
    cont=cont+1