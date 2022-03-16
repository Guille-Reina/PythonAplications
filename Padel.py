def funcion4():


    partido = input("Ingrese los dos equipos y su resultado respectivamente(FIN para acabar): ")
    equipo1, puntos1, equipo2, puntos2 = partido.split(' ')

    todoequip = [equipo1, equipo2]

    if puntos1 > puntos2:
        puntuacionequipo1 = 3
        puntuacionequipo2 = 0
        equipoganador = equipo1

    if puntos1 < puntos2:
        puntuacionequipo2 = 3
        puntuacionequipo1 = 0
        equipoganador = equipo2

    else:
        puntuacionequipo2 = 0
        puntuacionequipo1 = 0

    equipo1re = [equipo1, puntuacionequipo1]
    equipo2re = [equipo2, puntuacionequipo2]

    resultado = [equipo1re, equipo2re]


    while partido != 'fin':
        partido = input("Ingrese los otros dos equipos y su resultado respectivamente(FIN para acabar): ")

        if(partido != 'fin'):
            equipo1, puntos1, equipo2, puntos2 = partido.split(' ')

            if puntos1 > puntos2:
                puntuacionequipo1 = 3
                puntuacionequipo2 = 0
                equipoganador = equipo1

            if puntos1 < puntos2:
                puntuacionequipo2 = 3
                puntuacionequipo1 = 0
                equipoganador = equipo2

            else:
                puntuacionequipo2 = 0
                puntuacionequipo1 = 0


            if equipo1 in todoequip:
                print(resultado)
                x = resultado.index(equipo1)
                d = x +1
                puntosanteriores = resultado[d]
                nuevospuntos = puntosanteriores + puntuacionequipo1
                resultado[x:d] = [equipo1,nuevospuntos]

            else:

                equipo1re = [equipo1, puntuacionequipo1]
                resultado += [equipo1re]
                todoequip += [equipo1]

            if equipo2 in todoequip:

                x = resultado.index(equipo2)
                d = x +1
                puntosanteriores = resultado[d]
                nuevospuntos = puntosanteriores + puntuacionequipo2
                resultado[x:d] = [equipo1,nuevospuntos]

            else:

                equipo2re = [equipo2, puntuacionequipo2]
                resultado += [equipo2re]
                todoequip += [equipo2]

    else:
        print(resultado)

        print(todoequip)
        print("Equipo ganador:", equipoganador)
        print("Resultados de la liga:")



        for equipo, punto in resultado:

            print(equipo, " -- ", punto)
