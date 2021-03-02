nota1=(int(input("Ingrese nota1 : ")))
nota2=(int(input("Ingrese nota2 : ")))
nota3=(int(input("Ingrese nota3 : ")))
nota4=(int(input("Ingrese nota4 : ")))
nota5=(int(input("Ingrese nota5 : ")))
nota6=(int(input("Ingrese nota6 : ")))
nota7=(int(input("Ingrese nota7 : ")))
nota8=(int(input("Ingrese nota8 : ")))
nota9=(int(input("Ingrese nota9 : ")))

promedio= (nota1 + nota2 + nota3 + nota4 + nota5 + nota6 + nota7 + nota8 + nota9 )/ 9
if promedio >5 and promedio  <11:
    print("La persona a aprovado con C")
if promedio >11 and promedio <14:
    print("la persona a aprovado con B")
if promedio >14 and promedio <17:
    print("La persona a aprovado con A")
if promedio >17 and promedio <20:
    print("La persona a aprovado con AD")
else:
    print("La persona a desaprovado con F")