print("Sistema para calcular si pasa todas las materias")
nota_matematica_basica = int(input("¿Cual es su nota en matemática básica?"))
nota_matematicaa_avanzada = int(input("¿Cual es su nota en matemática avanzada?"))
promedio = nota_matematica_basica + nota_matematicaa_avanzada / 2
promedio = int(promedio)

if promedio > 7:
    print ("Tu promedio es de: ",promedio,"Felicidades pasaste todas las materias")
else:
    print ("Tu promedio es de: ",promedio,"No pasas todas las materias")
