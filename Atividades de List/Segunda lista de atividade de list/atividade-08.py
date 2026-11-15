G = ['E', 'A', 'B', 'C', 'C', 'D', 'E', 'A', 'C', 'D'] 
R = ['A', 'A', 'B', 'D', 'C', 'D', 'E', 'F', 'C', 'E']
cont=0
erro=0
acerto=[]

while cont < len(G):
    if R[cont] != G[cont]:
        erro= erro+1
    else:
        acerto.append(cont+1)
    cont=cont+1

print(f'quesões corretas: {acerto}')

if len(acerto) >= 6:
    print(f'Aprovado, {len(acerto)} acertos')    
else:
    print('Reprovado')