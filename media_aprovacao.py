# gustavo baps 
"""Escrever um programa, na linguagem Python, para verificar se um aluno foi
aprovado ou não em uma disciplina. Devem ser lidos o nome do aluno, as suas
duas notas de prova obtidas e o número de aulas que ele assistiu. Sabe-se que
durante o semestre foram dadas 20 aulas e que a média é aritmética."""
nome = input("Informe o nome do aluno: ")
nota1 = int(input("Insira a nota da primeira prova: "))
nota2 = int(input("Insira a nota da segunda prova: "))
freq = int(input("Informe o número de aulas assistidas no semestre: "))
media = (nota1 + nota2) / 2
por_freq  = freq/20 * 100
if nota1 > 10 or nota2 > 10 or por_freq > 100:
    print("Insira valores válidos")
else:
    if media >= 8 and por_freq >= 75:
        media_final = media
        situacao = "Aprovado por média"
    elif media < 3 or por_freq < 75:
        media_final = media
        if media < 3:
            situacao = "Reprovado por média"
        else:
            situacao = "Reprovado por frequência"
    else:
        print("O aluno está em exame")
        nota_exame = int(input("Insira a nota obtida no exame: "))
        media_final = (nota_exame + media)/2
        if media_final >= 6:
            situacao = "Aprovado em exame"
        else:
            situacao = "Reprovado em exame"
    print("O aluno %s de frequência %.1f%% e média final %.1f se encontra na seguinte situação: %s" %(nome, por_freq, media_final, situacao))
