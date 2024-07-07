#sequencia de numeros infinita, para quando for 0. exibir qual o menor valor e a media dos pares
cont = 0
menor = 0
pares = 0
seq_num = ""
cont_pares = 0
print("insira uma sequência de valores (0 termina):")
while True:
    num = int(input("insira um valor: "))
    if num == 0:
        break
    if cont == 0:
        menor = num
    else:
        if num < menor:
            menor = num
    if num % 2 == 0:
        cont_pares = cont_pares + 1
        pares = pares + num
    seq_num = seq_num + str(num) + " "
    cont = cont + 1
if cont == 0:
    print("nenhum numero foi inserido")
else:
    media = pares / cont_pares
    print("media dos valores pares: %.1f" %(media))
    print("menor valor inserido: %d" %(menor))
    print("sequencia numerica: ", seq_num)