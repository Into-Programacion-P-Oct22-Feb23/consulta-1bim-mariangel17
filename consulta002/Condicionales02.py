print("Sistema para saber a que puesto eres apto según tu conocimiento para nuestra heladeria")
print("Menu\n")
print("1.Seguí una carrera relacionada a contabilidad")
print("2.Tengo conocimiento de mesero")
print("3.Tengo práctica en cuestiones de limpieza")
opcion_ingresada = int(input("Escoja una opción de menu segun su conocimiento: "))

if opcion_ingresada == 1:
    print("Usted es apto para el puesto de caja")
elif opcion_ingresada == 2:
    print ("Usted es apto para el puesto de mesero")
elif opcion_ingresada == 3:
    print ("Usted es apto para el puesto de limpieza")
else:
    print ("Le recomendamos que adquiera los conocimientos y vuelva a postular")
                


