# Identificar o tipo de geometria a partir de 4 coordenadas inseridas pelo usuário,
# seja quadrado ou retângulo;

# Importação da biblioteca math para utilizar o sqrt.
import math

x1 = int(input('Digite um ponto para X1:'))
y1 = int(input('Digite um ponto para Y1:'))
print('---------------------')

x2 = int(input('Digite um ponto para X2:'))
y2 = int(input('Digite um ponto para Y2:'))
print('---------------------')

x3 = int(input('Digite um ponto para X3:'))
y3 = int(input('Digite um ponto para Y3:'))
print('---------------------')

x4 = int(input('Digite um ponto para X4:'))
y4 = int(input('Digite um ponto para Y4:'))
print('---------------------')

l1 = math.sqrt((x2-x1)**2 + (y2-y1)**2)
l2 = math.sqrt((x3-x2)**2 + (y3-y2)**2)
l3 = math.sqrt((x4-x3)**2 + (y4-y3)**2)
l4 = math.sqrt((x1-x4)**2 + (y1-y4)**2)

lado1 = round(l1,3)
lado2 = round(l2,3)
lado3 = round(l3,3)
lado4 = round(l4,3)

# Verifica os angulos retos através de produto escalar.
a1 = (x2-x1)*(x4-x1) + (y2-y1)*(y4-y1)  
a2 = (x1-x2)*(x3-x2) + (y1-y2)*(y3-y2)  
a3 = (x2-x3)*(x4-x3) + (y2-y3)*(y4-y3)   
a4 = (x3-x4)*(x1-x4) + (y3-y4)*(y1-y4) 
tem_reto = (a1 == 0) and (a2 == 0) and (a3 == 0) and (a4 == 0)


if tem_reto and lado1 == lado2 == lado3 == lado4: # Confere se é um quadrado
    print('É um quadrado')
elif tem_reto and lado1 == lado3 and lado2 == lado4:
    print('É um retangulo') # (0,0) (4,0) (4,2) (0,2)
else:
    print('Não é quadrado e tbm não é retangulo') 