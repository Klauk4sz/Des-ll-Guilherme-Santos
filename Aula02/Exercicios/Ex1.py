#Exercicios de Notas

nota1 = float(input ("Digite a primeira nota: "))
print(nota1)

nota2 = float(input ("Digite a segunda nota: "))
print(nota2)

nota3 = float(input ("Digite a terceira nota: "))
print(nota3)

nota4 = float(input ("Digite a quarta nota: "))
print(nota4)

soma = nota1 + nota2 + nota3 + nota4
print(soma)

media=soma/4
print(media)

if media >= 7:
    print("Aprovado")
elif media <=8:
    print("Aprovado")
else:
    print("Reprovado")