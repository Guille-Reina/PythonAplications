def funcion2():
    a = input('Dame un número entero\n')
    N = int(a)

    def correcion(N):
        result = 0
        for i in range(1, N+1):
            result += i
        return result


    result = correcion(N)

    if (result % 3 == 0):
        print('Si')
    else:
        print('No')