print("Sistema para calcular el promedio del estudiante ")
nota_mate = int(input("¿Cual es tu nota en matemáticas? "))
nota_literatura = int(input("¿Cual es tu nota en literatura? "))
nota_ciencias = int(input("¿Cual es tu nota en ciencias?"))
promedio = nota_mate + nota_literatura + nota_ciencias / 3
promedio = int(promedio)

if promedio >= 7:
    print("Tu promedio es:",promedio,"Felicitaciones pasas de año")
print("Fin")
