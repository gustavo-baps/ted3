"""exercicio 1

n1 = int(input("insira o primeiro valor: "))
n2 = int(input("insira o segundo valor: "))
print("a soma entre %d e %d é %d" %(n1, n2, n1 + n2))
print("a multiplicação de %d por %d é %d" %(n1, n2, n1 * n2))"""

""" exercicio 2

r = int (input("insira o raio da esfera para calcular seu volume: "))
vol = (4 * math.pi * (r ** 3))/3
print ("o volume da esfera é %.2f"  %vol)"""

"""n1 = int(input("insira a primeira nota do aluno: "))
n2 = int(input("insira a segunda nota do aluno: "))
n3 = int(input("insira a terceira nota do aluno: "))
media = (n1 + n2 + n3)/3
print("a média do aluno foi %.2f" %media)"""
import math
print("===calculadora de bhaskara===")
a = int(input("insira um valor para a: "))
b = int(input("insira um valor para b: "))
c = int(input("insira um valor para c: "))
delta = (b ** 2) -  (4 * a * c)
if delta < 0:
    print("é impossivel calcular as raízes da equação com os valores fornecidos (delta negativo)")
else:
    bhaskara1 = (-b + math.sqrt(delta))/(2*a)
    bhaskara2 = (-b - math.sqrt(delta))/(2*a)
    print("a primeira raiz da equação é %.2f" %bhaskara1)
    print("a segunda raiz da equação é %.2f" %bhaskara2)