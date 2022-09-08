import math
# O limite deve ser maior ou igual a 2

Limite = int(input('Entre com o limite (>= 2): '))
N = 2  # Número de ordem de cada elemento da sequência
FibA = 1
FibB = 1
# Imprime os títulos da tabela

print(' N      Fib(N)          Razão')
# Imprime os dois primeiros

print('001     001')
print('002     001     1.0')

while FibB < Limite:
    Aux = FibA + FibB
    FibA = FibB
    FibB = Aux
    N = N+1

    print('00'+str(N) if N < 10 else '0'+str(N) if N < 100 else N,
          '   ', '00'+str(FibB) if FibB < 10 else
          '0'+str(FibB) if FibB < 100 else FibB, '   ', FibB/FibA)
    print('Compare com a razão áurea:\n', '            ', (1+math.sqrt(5))/2)

# o limite tem que ser 200
