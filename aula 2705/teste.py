"""n = int(input("insira um numero entre 1 e 10: "))
i = 0
while(i == 0):
    n = int(input("erro, insira novamente: "))
    if n == 9:
        print("voce acertou!!!")
        i = 1"""
"""na = int(input("quantos alunos? "))
c = 1
s = 0
while (c<=na):
    n = float(input("nota do aluno %d: " %c))
    s = s + n
    c = c + 1
med = s/na
print("media dos alunos: %.1f" %med)"""
cont = 0
par = 0
num = int(input("informe um numero. 0 termina. "))
while num != 0:
    if num%2==0:
        print("numero par = ", num)
        par = par + 1
    cont = cont + 1
    num = int(input("informe um numero. 0 termina. "))
print("0 inserido. foram inseridos %d numeros" %cont)
perc = (par / cont) * 100
print("percentual de numeros pares inseridos: %.2f%%"%perc)




