import Foulhaber
import Multiplo3
import Padel
import Tortitas

print('MENÚ PRINCIPAL\n')
print('===============\n')

print ("A. Fórmula de Foulhaber")
print ("B. Múltiplo de 3")
print ("C. Tortitas")
print ("D. Liga de Pádel\n")

elegible = input("Elige cual quieres(A-D o FIN) \n")
elegible = elegible.lower()


while (elegible):
  if (elegible == 'a'):
    Foulhaber.funcion1()
    elegible = input("Elige cual quieres(A-D o FIN) \n")
  elif (elegible == 'b'):
    Multiplo3.funcion2()
    elegible = input("Elige cual quieres(A-D o FIN) \n")
  elif (elegible == 'c'):
    Tortitas.funcion3()
    elegible = input("Elige cual quieres(A-D o FIN) \n")
  elif (elegible == 'd'):
    Padel.funcion4()
    elegible = input("Elige cual quieres(A-D o FIN) \n")
  elif (elegible == 'fin'):
    break

