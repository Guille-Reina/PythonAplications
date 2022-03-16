def funcion1():
    val = input('Dame dos numeros enteros (separados por un espacio)\n')
    list = val.split(' ')

    N = int(list[0])
    P = int(list[1])


    def correcion(N, P):
        result = 0
        for i in range(1, N+1):
            result += i**P
        return result
    result = correcion(N, P)
    print("El resultado es: ", result)
