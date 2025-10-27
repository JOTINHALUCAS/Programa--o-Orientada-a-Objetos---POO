# Sugerir as coordenadas dos 3 pontos que formam o tipo de triângulo escolhido pelo usuário.
largura = '-'*69
print(largura)
print("Bem vindo ao script de qual a cordenada do triangulo".center(len(largura)))
print(largura)

print('------------------ MENU ----------------------')
print('1 - Isosceles | 2 - Equilatero | 3 - Escaleno')
print('----------------------------------------------')

op = input('Escolha 1 ou 2 ou 3:')
if op == '1':
    print('Essas são as cordenadas de um triangulo Isosceles:')
    print('(0,0), (4,0), (2,3)')
    print('(1,1), (5,1), (3,4)')
    print('(2,0), (6,0), (4,3)')
elif op == '2':
    print('Essas são as cordenadas de um triangulo Equilatero:')
    print('(0,0), (2,0), (1,1.732)')
    print('(0,0), (1,0), (0.5,0.866)')
    print('(2,2), (4,2), (3,3.732)')
elif op == '3':
    print('Essas são as cordenadas de um triangulo Escaleno:')
    print('(0,0), (4,0), (1,3)')
    print('(0,0), (3,0), (1,2)')
    print('(0,0), (5,1), (2,3)')
