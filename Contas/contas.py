v = int(input())
a = int(input())
f = int(input())
p = int(input())

x = v

lista = [a,f,p]
lista_m = sorted(lista)

soma = sum(lista)

num_p = 0

for i in range(3):
    if lista_m[i] <= v:
        v -= lista_m[i]
        num_p += 1
        continue

if soma == x:
    print(3)
else: print(num_p)

        