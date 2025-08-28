nota1= float(input("Digite a nota do aluno: "))
nota2= float(input("Digite a segunda nota do aluno: "))
media = (nota1+nota2)/2
if media < 7:
    print("reprovado".upper())
elif media >= 7 and  media <= 9:
    print("aprovado".upper())
elif media == 10:
    print("aprovado com distinção".upper())        