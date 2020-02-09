
#este es un comentario
'''
este es otro comentario
mayusculas = .upper()  minusculas .lower()
'''
num = 5
exponente = 2
potencia = num**exponente  #el doble asterisco significa exponieciacion

print (potencia)
nombre = "gabriel".upper()
edad = 21
# dos formas de imprimir
print (f"Hola {nombre} tienes {edad} anios")
print ("Hola",nombre,"tienes",edad,"anios")

#entradas de datos
entrada = input("escribe algo:   \n")
print(entrada)
entero = int(input("escribe un entero:   \n"))
print(entero+5)

#funciones integradas (convertir tipos de datos)
#convertir flotante en cadena
n = str(10.5)
#convertir cadena en entero
n = int("10")
#convertir decimal en binario
n = bin(10)
#convertir  decimal a hexa
n = hex(10)
#binario a entero
n = int("0b1010",2)
#hexa a entero
n = int("0xa",16)
#longitud de una cadena
n = len("Alex")
#recorte de decimales
numero = 5.12345678
print(f"el numero recortado es: {numero:.2f}")
#condicionales
if numero>0:
    print("es positivo")
elif numero == 0:
    print("es cero")
else:
    print("Es negativo")
#rango en condicionales
if numero>0 and numero<10:
    print("numero entre 1 y 9")
#rango de condicionales de otra forma
if 0<numero<10:
    print("numero entre 1 y 9")
#calcular si un numero es par:
par = int(input("escribe un numero: "))
if par%2 == 0:
    print(f"el numero {par} es par")

#------------LISTAS-----------

lista = ["lunes", "martes", "miercoles","jueves","viernes"]
print (lista)
print(len(lista))  #longitud de la lista
lista.append("sabadaba") #agregar dato al final de la lista
lista.insert(2, "hola") #agregar dato en la posicion 2
print(lista[1:4])   #imprimir un rango de valores
lista.extend(["domingo", "LUNES", "MARTES"])  #insertar varios elementos al final de la lista
#concatenar listas:
lista1 = [1,2,3,4]
lista2 = [5,6,7]
lista3 = lista1 + lista2
#modificar un valor de la lista
lista3[3] = 34
#Saber si existe un dato en la lista
print("LUNES" in lista)   #imprimira un true o false segun sea el caso
#buscar un dato en especifico
print(lista.index("MARTES"))
#cantidad de veces que aparece un dato en una lista:
print(lista.count("viernes"))

#Eliminar un dato de la lista
lista.pop()  #para eliminar el ultimo elemento
lista.pop(0) #elimina un dato especifico con el indice del dato
lista.remove("jueves")   #elimina a un dato dependiendo del dato, no del indice
#Limpiar la lista
lista.clear()
#invertir la lista
lista.reverse()
#ordenar una lista
lista_num = [5, 2, 1, -9, 3]
lista_num.sort()         #de menor a mayor
lista_num.sort(reverse=True)   #de mayor a menor