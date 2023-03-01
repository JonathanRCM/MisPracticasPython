#Ejercicio funcional 1 , calcula promedios o no hace nada.
def adios():
    print("Eso fue todo, hasta luego. jsjsjs")

nombre = input("Por favor ingresa tu nombre : -> ")
print(  )
print("Hola "+nombre+" este programa es de opcion multiple, dependiendo de tu eleccion se hara lo que solicites.")
print(  )
print("""A continuacion se te presentaran tus opciones y tendras que elegir lo que hara el programa :D
-------------------------------------------------------------------
--->  Opcion 1: Calcular tu promedio final de tu semestre          |
--->  Opcion 2: Calcular el promedio de una sola materia           |
--->  Opcion 3: Nada xd                                            |
-------------------------------------------------------------------""")                                        
print(  )
print("Si deseas seleccionar la opcion 1 teclea (1), si deseas escoger la opcion 2 teclea (2) y lo mismo con la opcion 3")
Respuesta = int(input())
if Respuesta==3 :
    print("F")
    adios()
elif Respuesta==2:
    materia =input("¿De que materia deseas calcular tu promedio? -> ")
    print(  )
    print("Bien, calculemos tu promedio final de "+materia)
    print(  )
    print("Por favor ingresa la calificacion de tus 4 parciales ")
    print("Introduce numeros enteros, ejemplo : 9.5 = 95 :) ")
    print("-----------------")
    print(  )
    suma=0
    num=0
    for i in range (1,5):
     num = int (input("-> "))
     suma=suma+num
     prom=suma//4
     promstring = f"{prom}"
    print("tu promedio final de "+materia+ " es "+promstring)
    adios()
else :
    print("Muy bien " +nombre+" vamos a calcular el promedio final de tu segundo semestre de ISIC.")
    print(  )
    print("""Por favor ingresa la calificacion de tus 4 parciales de calculo
    (Introduce numeros enteros, ejemplo : 9.5 = 95 :)) """)
    print("-----------------")
    print(  )
    suma1=0
    for i in range (1,5):
        num = int (input("-> "))
        suma1=suma1+num
    prom1=suma1//4
    prom1string = f"{prom1}"
    print("tu promedio final de Calculo es "+prom1string)
    print(  )
    print("Muy bien, ahora pasemos a la siguiente materia.")
    print(  )
    print("""Por favor ingresa la calificacion de tus 4 parciales de Probabilidad y estadistica.
    (Introduce numeros enteros, ejemplo : 9.5 = 95 :D ) """)
    print("-----------------")
    print(  )
    suma2=0
    for i in range (1,5):
     num = int (input("-> "))
     suma2=suma2+num
    prom2=suma2//4
    prom2string = f"{prom2}"
    print("tu promedio final de Probabilidad es "+prom2string)
    print(  )
    print("Okey, ahora vamos con Programacion Orientada a Objetos.")
    print(  )
    print("""Por favor ingresa la calificacion de tus 4 parciales de POO.
    (Introduce numeros enteros, ejemplo : 9.5 = 95 :D ) """)
    print("-----------------")
    print(  )
    suma3=0
    for i in range (1,5):
     num = int (input("-> "))
     suma3=suma3+num
    prom3=suma3//4
    prom3string = f"{prom3}"
    print("tu promedio final de POO es "+prom3string)
    print(  )
    print("Bien, ahora pasemos a Contabilidad.")
    print(  )
    print("""Por favor ingresa la calificacion de tus 4 parciales de Contabilidad.
    (Introduce numeros enteros, ejemplo : 9.5 = 95 :D ) """)
    print("-----------------")
    print(  )
    suma4=0
    for i in range (1,5):
     num = int (input("-> "))
     suma4=suma4+num
    prom4=suma4//4
    prom4string = f"{prom4}"
    print("tu promedio final de Contabilidad es "+prom4string)
    print(  )
    print("Okey, ahora calculemos el de Química.")
    print(  )
    print("""Por favor ingresa la calificacion de tus 4 parciales de Química.
    (Introduce numeros enteros, ejemplo : 9.5 = 95 :D ) """)
    print("-----------------")
    print(  )
    suma5=0
    for i in range (1,5):
     num = int (input("-> "))
     suma5=suma5+num
    prom5=suma5//4
    prom5string = f"{prom5}"
    print("tu promedio final de Química es "+prom5string)
    print(  )
    print("ahora vamos con Álgebra.")
    print(  )
    print("""Por favor ingresa la calificacion de tus 4 parciales de Álgebra.
    (Introduce numeros enteros, ejemplo : 9.5 = 95 :D ) """)
    print("-----------------")
    print(  )
    suma6=0
    for i in range (1,5):
      num = int (input("-> "))
      suma6=suma6+num
    prom6=suma6//4
    prom6string = f"{prom6}"
    print("tu promedio final de Álgebra es "+prom6string)
    print(  )
    print("Okey, ahora calculemos el de Formación integral.")
    print(  )
    print("""Por favor ingresa la calificacion de tus 4 parciales Formación.
    (Introduce numeros enteros, ejemplo : 9.5 = 95 :D ) """)
    print("------------------")
    print(  )
    suma7=0
    for i in range (1,5):
     num = int (input("-> "))
     suma7=suma7+num
    prom7=suma7//4
    prom7string = f"{prom7}"
    print("tu promedio final de Formación es "+prom7string)
    print(  )
    print("Por ultimo calculemos el de Inglés")
    print(  )
    print("""Por favor ingresa la calificacion de tus 4 parciales de inglés.
    (Introduce numeros enteros, ejemplo : 9.5 = 95 :D ) """)
    print("------------------")
    print(  )
    suma8=0
    for i in range (1,5):
       num = int (input("-> "))
       suma8=suma8+num
    prom8=suma8//4
    prom8string = f"{prom8}"
    print("tu promedio final de Inglés es "+prom8string)
    print(  )
    prom_final = (prom1+prom2+prom3+prom4+prom5+prom6+prom7+prom8)//8
    prom_final_string = f"{prom_final}"
    print("Tomando en cuenta el promedio de tus materias, tu promedio final del curso es de: "+prom_final_string)
    print(  )
    adios()
    