def funcion3():
    print('Estos números representarán el estado en la torre de tortitas')
    numtort = input('Dame el conjunto de números (separados por un espacio cada uno)\n')
    list = numtort.split(' ')
    print('Estos serán los movimientos que ha hecho el chef')
    movchef = input('Dame otro conjunto de números (separados por un espacio cada uno)\n')
    list2 = movchef.split(' ')

    list.reverse()
    print(list)
    def correcion():
        for x in list2:
            a = int(x)
            a1 = list[:a]
            a1.reverse()
            list[0:a] = a1
            print(list)
    result = correcion()
    print(result)