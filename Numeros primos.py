#Decir si un numero es numero primo 

entrada=None
a="Es primo"
try:
    entrada=int(input("Ingresa el numero a evaluar\n"))
    if(entrada!=2):
        for i in range(2,entrada):
            if(entrada%i==0 ):
                a="No es primo"
                break
            else:
                a="Es primo"
                break
    
    print(a)

    
except Exception:
    print("Solo agrega numeros")
