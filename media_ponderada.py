n1 = int(input("insira a primeira nota: "))
n2 = int(input("insira a segunda nota: "))
n3 = int(input("insira a terceira nota: "))
if n1 > n2 and n1 > n3:
    maior = n1
else:
    if n2 > n3:
        maior = n2
    else:
        maior = n3
if n1 < n2 and n1 < n3:
    menor = n1
else:
    if n2 < n3:
        menor = n2
    else:
        menor = n3
meio = (n1 + n2 + n3) - maior - menor
if (n1 < n2 and n1 > n3) or (n1 > n2 and n1 < n3):
    meio = n1
else:
    if(n2 < n1 and n2 > n3) or (n2 > n1 and n2 < n3):
        meio = n2
    else:
        meio = n3
media = ((menor*2) + (meio * 3) + (maior * 5))/(2 + 3 + 5)
print("maior: %d   meio: %d   menor: %d" %(maior, meio,menor))
print("a media final foi %.2f" %media)