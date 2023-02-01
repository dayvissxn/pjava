n1 = 0
n2 = 0

n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))

media = (n1 + n2) / 2

if media >= 7 and media < 10:
    print("Aprovado!")
elif media == 10:
    print("Aprovado com Distição!")
else:
    print("Reprovado!")