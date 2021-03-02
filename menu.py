# ===================Funciones
def bienvenida():
    text = '''
    Menu de opciones 
    =================
    1. Sumar 2 numeros
    2. Mayor de 3 numeros
    3. Menor de 3 numeros
    4.Ver la nota del Alumno A,B,C,AD
    5.Salio del programa

    Ingrese un opcion para continuar...
    '''
    print(text)


def seleleccionarOpcion():
    opcion = int(input("Ingrese la opcion: "))
    seleccionarOperacio(opcion)


def mayor3num():
    a = int(input("Ingrese a: "))
    b = int(input("Ingrese b: "))
    c = int(input("Ingrese c: "))
    mayor=0
    if a >= b and a >= c:
        mayor=a
    if b >= a and b >= c:
        mayor=b
    if c >= a and c >= b:
        mayor=c
    print("El mayor:" + str(mayor))
    inicio()


def menor3num():
    a = int(input("Ingrese a: "))
    b = int(input("Ingrese b: "))
    c = int(input("Ingrese c: "))
    menor = 0
    if a <= b and a <= c:
        menor = a
    if b <= a and b <= c:
        menor = b
    if c <= a and c <= b:
        menor = c
    print("El menor:" + str(menor))
    inicio()


def seleccionarOperacio(opcion):
    if opcion == 1:
        sumar()
    if opcion == 2:
        mayor3num()
    if opcion == 3:
        menor3num()
    if opcion == 4:
        nota()
    if opcion == 5:
        print("Salió del Programa")

def inicio():
    bienvenida()
    seleleccionarOpcion()

def nota():
    nota = (int(input("Ingrese nota1 : ")))

    if nota > 11 and nota < 14:
        print("la persona a aprovado con B")
    if nota > 14 and nota < 17:
        print("La persona a aprovado con A")
    if nota > 17 and nota < 20:
        print("La persona a aprovado con AD")
    else:
        print("La persona a desaprovado con c")
    inicio()
def sumar():
    a = int(input("Ingrese a: "))
    b = int(input("Ingrese b: "))
    resultado = a + b
    print(" El resultado de a + b es :" + str(resultado))
    inicio()



# ===================utilizo las funciones para jejcutar
inicio()