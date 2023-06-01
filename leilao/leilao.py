leilao = {}

n = int(input())

nome = input()
valor = int(input())

leilao[nome] = valor

index = 0
Mvalor = valor
Mnome = nome

for i in range(n - 1):
    nome = input()
    valor = int(input())
    
    leilao[nome] = valor
    
    if valor > Mvalor:
        Mnome = nome
        Mvalor = valor
        index = i + 1
        
print(Mnome)
print(Mvalor)