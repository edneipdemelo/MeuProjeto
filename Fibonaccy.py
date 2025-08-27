# Código de cálculo para Fibonaccy...

F1 = 0; F2 = 1; X = 0
while X <= 2000:
    X = F1 + F2
    F1 = F2
    F2 = X
    if X > 2000:
        break
    print(X, end=" ")
