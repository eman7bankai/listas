#questionario do batman
from time import sleep
pontos = 0
pergunta1 = input("telefonou pra vitima?")
if pergunta1 == 's':
    pontos +=1
pergunta2 = input("esteve no local do crime?")
if pergunta2 == 's':
    pontos +=1
pergunta3 = input("mora perto da vitima?")
if pergunta3 == 's':
    pontos +=1
pergunta4 = input("devia pra vitima?")
if pergunta4 == 's':
    pontos +=1
pergunta5 = input("ja trabalhou pra vitima?")
if pergunta5 == 's':
    pontos +=1

print("você é...")
sleep(1)
if pontos < 2:
    print("inocente")
elif pontos == 2:
    print("suspeito")
elif pontos >= 3 and pontos <=4:
    print("cumplice")  
elif pontos == 5:
    print("assasino".upper())          
