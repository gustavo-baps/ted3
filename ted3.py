#gustavo baps - ted 3

candidatos = []
votos_validos = 0
votos = 0
votos_nulos = 0
resp = "S"
cand = 0
def codigo_existente(codigo, candidatos):
    for candidato in candidatos:
        if codigo == candidato[1]:
            return True
    return False
def nome_existente(nome, candidatos):
    for candidato in candidatos:
        if nome == candidato[0]:
            return True
    return False

while cand < 5:
    nome = input("Qual o nome do candidato nº %d? (nomes não podem ser repetidos) "%(cand + 1))
    while nome_existente(nome, candidatos):
        nome = input("Já há um candidato com esse nome, insira outro: ")
    while True:
        try:
            cod = float(input("Qual o código do candidato %d? (número inteiro) "%(cand + 1)))
            if cod >= 0 and not codigo_existente(cod, candidatos):
                break
            else:
                print("Por favor, insira um código válido: ")
        except ValueError:
            print("Por favor, insira um código válido: ")
    candidato = (nome, cod, 0)
    candidatos.append(candidato)
    cand += 1
print("Candidatos: ")
for candidato in candidatos:
    print(f"Candidato: {candidato[0]}, Código: {int(candidato[1])}")
while votos < 245 and resp == "S":
    try:
        codigo_voto = int(input("Em qual candidato deseja votar? "))
        encontrado = False
        for i in range(len(candidatos)):
            if codigo_voto == candidatos[i][1]:
                votos_validos += 1
                candidatos[i] = (candidatos[i][0], candidatos[i][1], candidatos[i][2] + 1)
                encontrado = True
                break
        if not encontrado:
            print("Voto nulo")
            votos_nulos += 1
    except ValueError:
        print("Voto nulo")
        votos_nulos +=1
    resp = input("Deseja continuar? (S/N): ").upper()
    while resp not in ["S", "N"]:
        resp = input("Resposta inválida, tente novamente: ").upper()
    votos += 1
print("Resultados da votação: ")
for candidato in candidatos:
    print(f"Candidato: {candidato[0]}, Código: {candidato[1]}, Votos: {candidato[2]}")
nome_vencedor = ""
cod_vencedor = 0
maior_votos = 0
print("Total de votos: %d" %votos)
for candidato in candidatos:
    if candidato[2] > maior_votos:
        maior_votos = candidato[2]
        nome_vencedor = candidato[0]
        cod_vencedor = candidato[1]
percentual_vencedor = maior_votos/votos_validos * 100
print("Candidato vencedor: %s   Código: %d   Porcentagem de votos: %.2f%%   Número de votos: %d" %(nome_vencedor, int(cod_vencedor), percentual_vencedor, maior_votos))
if votos_nulos > 0:
    percentual_nulos = votos_nulos / votos * 100
    print("Percentual de votos nulos: %.2f%% (%d votos)" %(percentual_nulos, votos_nulos))
else:
    print("Nao houveram votos nulos")
