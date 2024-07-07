#ler 2 numeros inteiros e calcular a media dos multiplos de 5 existentes entre eles (sem contar os proprios numeros)
n1 = int(input("insira o primeiro numero: "))
n2 = int(input("insira o segundo numero: "))
if n1 > n2:
    lim = n1
    cont = n2
else:
    lim = n2
    cont = n1
mult = 0
lista = ""
cont_mult = 0
while cont < lim:
    if cont % 5 == 0 :
        mult = mult + cont
        cont_mult = cont_mult + 1
        lista = lista + str(cont) + " "
    cont = cont + 1
print("lista dos multiplos de 5 entre %d e %d: %s"%(n1, n2, lista))
media = mult / cont_mult
print("media dos multiplos de 5: %.2f" %(media))