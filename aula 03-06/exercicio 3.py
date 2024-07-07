#ler n pessoas, nome, sexo, altura e peso
#media das alturas dos homens e peso das mulheres
#nome do homem mais alto e da mulher mais magra
media_alt = 0
media_pes = 0
maior_altura = 0
menor_peso = 0
maior = ""
magra = ""
contm = 0
contf = 0
np = int(input("quantas pessoas serão entrevistadas? "))
while np <= 0:
    np = int(input("quantas pessoas serão entrevistadas? "))
cont = 0
while cont < np:
    nome = input("qual o nome da pessoa %d?" %(cont + 1))
    sexo = input("qual o sexo da pessoa? (M/F) ")
    sexo = sexo.upper()
    while sexo != "M" and sexo != "F":
        sexo = input("qual o sexo da pessoa? (M/F) ")
        sexo = sexo.upper()
    altura = float(input("qual a altura da pessoa? "))
    while altura <= 0:
        altura = float(input("qual a altura da pessoa? "))
    peso = float(input("qual o peso da pessoa? "))
    while peso <=0:
        peso = float(input("qual o peso da pessoa? "))
    if sexo == "M":
        contm = contm + 1
        media_alt = media_alt + altura
        if contm == 1:
            maior = nome
            maior_altura = altura
        else:
            if altura > maior_altura:
                maior = nome
                maior_altura = altura
    else:
        contf = contf + 1
        media_pes = media_pes + peso
        if contf == 1:
            magra = nome
            menor_peso = peso
        else:
            if peso < menor_peso:
                magra = nome
                menor_peso = peso
    cont = cont + 1
if contf == 0:
    media_altura = media_alt/contm
    print("nenhuma mulher entrevistada")
    print("media das alturas dos homens: %.2fm" %(media_altura))
    print("homem mais alto: %s, com %.2fm de altura" %(maior, maior_altura))
elif contm == 0:
    media_peso = media_pes/contf
    print("nenhum homem entrevistado")
    print("media dos pesos das mulheres: %.2fkg" %(media_peso))
    print("mulher mais magra: %s, com %.2fkg"%(magra, menor_peso))
else:
    media_peso = media_pes/contf
    media_altura = media_alt/contm
    print("media das alturas dos homens: %.2fm" %(media_altura))
    print("media dos pesos das mulheres: %.2fkg" %(media_peso))
    print("homem mais alto: %s, com %.2fm de altura" %(maior, maior_altura))
    print("mulher mais magra: %s, com %.2fkg" %(magra, menor_peso))