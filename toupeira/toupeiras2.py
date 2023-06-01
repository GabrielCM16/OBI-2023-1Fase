s, t = input().split()

tuneis = []

for i in range(int(t)):
    x = input().split()
    
    abc = list(reversed(x))
    
    if x not in tuneis:
        tuneis.append(x)
    if abc not in tuneis:
        tuneis.append(abc)
    
nTuneis = 0
ntest = 0
    
for i in range(int(input())):
    ntest = 0
    lista = input().split()
    
    
    for i in range(int(lista[0]) - 1):

        if list([lista[i + 1], lista[i + 2]]) in tuneis:
            ntest += 1
        else: 
            break
            
    if ntest == int(lista[0]) - 1:
        nTuneis += 1
    
print(nTuneis)