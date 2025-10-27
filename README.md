# Programação Orientada a Objetos - POO
 - Sistema Bancário -
Esse sistema foi desenvolvido como atividade de Programação Orientada a Objetos com o principal objetivo simular um sistema bancário com a criação de contad e operções bancárias o sistema foi desenvolvido em python.

Estrtura de classes:
Classe conta: Respresenta uma conta bancária individual.
Possui atributos como "numero", "titular" e "saldo".
E os métodos para:
  creditar(valor)
  debitar (valor)
  mostrar_saldo()

Classe Banco:
Gerencia um conjunto de contas bancárias.
Tem a permissão de adicionar novas contas e realizar transferências entres elas.
Métodos:
  adicionar_conta()
  creditar(numero_conta, valor)
  transferir(conta_origem, conta_destino, valor)
  saldo()

O diagrama mostra a relação entre as classes Banco e Conta:
![Digrama UM](.imagens/diagrama.png)

Autor: João Lucas Pinto Taveira.
Universidade Federal do Ceará (UFC).
Disciplina: Programação Orientada a Objetos.
