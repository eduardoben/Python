#Crear funcion para sumar valores de un arreglo

def SumarA(a):
    suma=0;
    for x in a:
        suma=suma+x
    return suma

array =[1,2,3,4,5,6,3,1,3]

print(SumarA(array))



