

def kilometros_millas(a):
    return a * 1.60

def millas_kilometros (a):
    return a*0.62

def kilogramos_libras (a):
    return a * 0.45

def libras_kilogramos (a):
    return a * 2.20

def celsius_fahrenheit(a):
    return ((a-32)*5/9)

def fahrenheit_cesius(a):
    return ((a*9/5)+32)

def main():
        mensaje =""" 
        opciones
       1-kilometros -> millas
       2-millas -> kilometros
       3-kilogramos -> libras
       4-libras -> kilogramos
       5-celsius -> fahrenheit
       6-fahrenheit -> celsius
       7-salir
       """ 
        print(mensaje)

        numero = int (input("ingrese una opcion: "))

        while numero != 7 :

            valor_a=int(input("ingrese valor a cambiar: "))
            
            if numero==1:
                resultado = kilometros_millas(valor_a)
            elif numero==2:
                resultado = millas_kilometros(valor_a)    
            elif numero==3:
                resultado = kilogramos_libras(valor_a) 
            elif numero==4:
                resultado = libras_kilogramos(valor_a)
            elif numero==5:
                resultado = celsius_fahrenheit(valor_a)
            elif numero==5:
                resultado = fahrenheit_cesius (valor_a)        
            else:
                resultado= ""
                print("vuelva a intentar ingresar un valor (solo numeros)")    

            print(f"el resultado del cambio es : {resultado}") 

            numero = int (input("ingrese una opcion: ")) 

            print(mensaje)    #repito   


if __name__=="__main__":
    main()









    