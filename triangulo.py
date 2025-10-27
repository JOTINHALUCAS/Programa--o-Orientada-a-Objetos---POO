# Validar e refinar o algoritmo para identificar o tipo de triângulo (escaleno, isósceles ou equilátero), 
# a partir das coordenadas de 3 pontos no plano cartesiano (X, Y);
import math

# Pega os pontos 

x1 = float(input('Digite um ponto para x1:'))
y1 = float(input('Digite um ponto para x2:'))

x2 = float(input('Digite um ponto para x2:'))
y2 = float(input('Digite um ponto para y2:'))

x3 = float(input('Digite um ponto para x3:'))
y3 = float(input('Digite um ponto para y3:'))

# Faz todo os calculos das distancias

l1 = math.sqrt((x2 - x1)**2 + (y2-y1)**2)
l2 = math.sqrt((x3 - x2)**2 + (y3-y2)**2)
l3 = math.sqrt((x1-x3)**2 + (y1-y3)**2)

# Arrendonda para três casas decimais

lado1 = round(l1, 3)
lado2 = round(l2,3)
lado3 = round(l3,3)

if (lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado1 + lado3 > lado2):
    print('Forma um triangulo')
    if lado1 == lado2 == lado3: # Se todos os lados foram iguais -> Saida: 'O triangulo é equilatero.'
        print('O triangulo é equilatero.')
    elif (lado1 != lado2) and (lado2!= lado3) and (lado1 != lado3): # Se todos os lados forem diferentes -> Saida: 'Triangulo escaleno.'
        print('Triangulo escaleno.')
    else:
        print('Triangulo Isosceles.')
else:
    print('Não os pontos nao forma um triangulo')


