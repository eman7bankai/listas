maior = 0
for c in range(1,4):
    numero = int(input("Digite um numero:"))
    if c == 1:
        maior = numero
    if numero> maior:
        maior = numero    
print(f"o maior é {maior}")