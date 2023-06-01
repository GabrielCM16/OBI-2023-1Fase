s, t = input().split()

tuneis = []

for i in range(int(t)):
    x = input().split()
    
    tuneis.append(x)
    

nTuneis = 0
ntest = 0
    
for i in range(int(input())):
    ntest = 0
    lista = input().split()
    
    
    for i in range(int(lista[0]) - 1):
            
        index = i + 1
            
        li = [lista[index], lista[index + 1]]
       
        lii = list(reversed(li))
            
        if li in tuneis or lii in tuneis:
            ntest += 1
            
    if ntest == int(lista[0]) - 1:
        nTuneis += 1
    
print(nTuneis)