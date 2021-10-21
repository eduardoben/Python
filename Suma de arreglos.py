#Ingresar 10 numeros a un arreglo y utilizando punteros indicar numeros pares y su posicion en memoria

array=[]
Newarray=[]

for i in range(0,10):    
    array.append(int(input("Agrega un numero al array \n")))
    if(array[i]%2==0 and array[i]!=0):
        Newarray.append(array[i])
    
print("Estos numeros son pares",Newarray)
