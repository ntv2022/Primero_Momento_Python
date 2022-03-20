# -Construir un programa que permita ingresar N (cantidad digitada por el
# usuario) números enteros y cuente cuantos múltiplos de 2 y de 3 fueron
# ingresados (+1)




# ----- Crear variables necesarias ------

listaNumeros = []

numerosMultiplosDeDos = 0
numerosMultiplosDeTres = 0

print('')

# ------Ingreso de datos por el usuarios------

tamañoLista = int(input('Ingrese la cantidad de números a registrar :'))

for k in range(tamañoLista):
     
     numeroIngresado = int(input('Ingresa el número :'))
     listaNumeros.append(numeroIngresado)

  

for numero in listaNumeros:
    
    if numero % 2 == 0:
         numerosMultiplosDeDos += 1
    elif numero % 3 == 0:
        numerosMultiplosDeTres += 1

print('')
print(f'De la lista de números de número son multiplos de 2 : {numerosMultiplosDeDos}')
print(f'De la lista de números son multiplos de 3 : {numerosMultiplosDeTres}')
print('')
 
 
        


        
        
 