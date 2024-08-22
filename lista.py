#Questão 1:
n1 = int(input("Digite um numero"))
n2 = int(input("Digite outro numero"))
n3 = int(input("Digite mais um numero"))
media = (n1 + n2 + n3 ) /3
print(media)

#Questão 2:
numero =int(input("Digite um numero:"))
if numero % 2 == 0:
    print(f"O número, {numero}, é par.")
else:
    print(f"O número{numero} é impar")

#Questão 3:
    
num = int(input("Digite um numero:"))
for i in range(0, num +1):
    if i % 2 == 0:
        print(i)

#Questão 4:
        
lista1 = [100, 50, 80, 140]
maior = max(lista1)
menor = min(lista1)
print(f"O maior numero da lista é {maior}, e o menor é {menor}")
    
