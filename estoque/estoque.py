x, y = input().split()

estoque = []
nVendas = 0

for i in range(int(x)):
    entrada = list(map(int, input().split()))
    
    estoque.append(entrada)
    
for i in range(int(input())):
    i, j = input().split()
    i, j = int(i), int(j)
    
    if estoque[i - 1][j - 1] > 0:
        estoque[i - 1][j - 1] -= 1
        nVendas += 1
    
print(nVendas)