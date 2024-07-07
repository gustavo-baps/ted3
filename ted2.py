maisJovem = None
sexoLista = ['M', 'F']
totalSalarios = 0
pessoasEmpregadas = 0
capMaxima = 135
criancas = 0
homens = 0
mulheres = 0
totalPessoas = 0

continuar = 'S'

while continuar.upper() == 'S' and totalPessoas < capMaxima:

    nome = input("Informe o nome da pessoa: ").strip()
    if not all(part.isalpha() for part in nome.split()):
        print("Por favor, insira um nome válido (apenas letras).")
        continue


    while True:
        idade_input = input("Informe a idade da pessoa: ").strip()
        if idade_input.isdigit():
            idade = int(idade_input)
            if idade > 0:
                break
            else:
                print("Por favor, insira uma idade válida.")
        else:
            print("Por favor, insira uma idade válida.")

    # Coletar sexo
    sexo = input("Informe o sexo da pessoa (M/F): ").strip().upper()
    if sexo not in sexoLista:
        print("Sexo inválido. Por favor, insira 'M' ou 'F'.")
        continue

    if idade > 12:
        emprego = input("A pessoa está empregada? (S/N): ").strip().upper()
        if emprego not in ['S', 'N']:
            print("Resposta inválida. Por favor, insira 'S' ou 'N'.")
            continue
        if emprego == 'S':
            while True:
                try:
                    salario = float(input("Qual a sua média salarial(em R$)? "))
                    if salario >= 0:
                        break
                    else:
                        print("Por favor, insira um valor válido para a média salarial.")
                except ValueError:
                    print("Por favor, insira um valor válido para a média salarial.")
        
        totalSalarios += salario
        pessoasEmpregadas += 1


    if idade < 12:
        criancas += 1

    if sexo == 'M':
        homens += 1
    elif sexo == 'F':
        mulheres += 1


    if maisJovem is None or idade < maisJovem[2]:
        maisJovem = (nome, sexo, idade)

    totalPessoas += 1
    continuar = input("Deseja continuar a pesquisa? (S/N): ").strip().upper()


mediaSal = totalSalarios / pessoasEmpregadas if pessoasEmpregadas > 0 else 0
if homens > mulheres:
    maisEntrevistado = "Homens"
elif mulheres > homens:
    maisEntrevistado = "Mulheres"
else:
    maisEntrevistado = "Homens e mulheres com número igual de entrevistados"

percentualCrianca = (criancas / totalPessoas) * 100
if percentualCrianca == 0:
    print("Não há crianças no abrigo ou nenhuma criança foi entrevistada.")

if maisJovem:
    print(f"| Pessoa mais jovem: Nome: {maisJovem[0]}, Sexo: {maisJovem[1]}, Idade: {maisJovem[2]} |")
print(f"| Média salarial das pessoas com emprego: R${mediaSal:.2f} |")
print(f"| Quem foi mais entrevistado: {maisEntrevistado} |")
print(f"| Percentual de crianças no abrigo: {percentualCrianca:.2f}% |")