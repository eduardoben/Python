#Rellenar un arreglo con n números, posteriormente utilizando punteros determinar el menor elemento del vector.

arreglo=[]
i=0
minimo=None
while(True):
    try:
        arreglo.append(int(input("Agrega un numero\n")))
    except Exception:  
        break

    if(i==0) or (arreglo[i]< minimo):
        minimo=arreglo[i]
    i+=1

print(arreglo)
print("El menor valor es: ", minimo)

