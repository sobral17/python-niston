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
    
nume = int(input("Digite um numero:"))
for i in range(0, nume +1):
    if i % 2 == 0:
        print(i)

#Questão 4:
        
lista1 = [100, 50, 80, 140]
maior = max(lista1)
menor = min(lista1)
print(f"O maior numero da lista é {maior}, e o menor é {menor}")

#Questão 5:

numeros = [12, 15, 18, 21, 24]
pares = [num for num in numeros if num % 2 == 0 ]
if pares: 
    media_pares = sum(pares) / len(pares)
    print("A média dos numeros pares é ", media_pares)

#Questão 6:


#Questão 7:


#Questão 8:
def e_primo(nume):
    if nume <= 1:
        return False
    if nume == 2:
        return True
    if nume % 2 == 0:
        return False
    for i in range(3, int(nume**0.5) + 1, 2):
        if nume % i == 0:
            return False
    return True
nume = int(input("Digite um numero:" ))
if e_primo(nume):
        print(f"{e_primo} é um numero primo")
else:        print(f"{e_primo} não é um numero primo")
