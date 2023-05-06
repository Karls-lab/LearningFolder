# Dynamic Fib problem taken from The Algorithm Design Manual
# Coded in python by Karl Poulson

def dynamicFib(n):
    fibCache = [None] * n
    fibCache[0] = 0
    fibCache[1] = 1
    for i in range(2, n):
        fibCache[i] = fibCache[i-1] + fibCache[i-2]
    return fibCache

#print(dynamicFib(100))

def binomial_coefficient(n, k):
    i = 0
    j = 0
    bc = [ [0]*(n+100), [0]*(n+100) ]

    for i in range(0, n):
        print(i)
        bc[i][0] = 1;

    for j in range(0, n):
        bc[j][j] = 1;

    for i in range(2, n):
        for j in range(1, i):
            bc[i][j] = bc[i-1][j-1] + bc[i-1][j]

    return bc[n][k]

#print(binomial_coefficient(5, 4))
bc = [ [0]*(5+1), [0]*(5+1) ]
print(bc)
print(bc[1][1])