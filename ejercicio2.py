# -Leer el nombre de 10 frutas para preparar un salpicón; el programa debe
# permitir mostrar las 10 frutas ingresadas al mismo tiempo en sentido
# inverso al ingresado+(1)

# -----Información al usuario------

print('')
print('Ingresar hasta 10 frutas!!!')
print('')


# ----- Crear variables necesarias ------

repeticiones = 1
frutas = []


# ------ inicio del ciclo -----------

while(repeticiones <= 10):
     
    repeticiones += 1
    ingreso = input('Ingresa una fruta :')
    frutas.append(ingreso)


print(f'La lista de frutas ingresadas {frutas}')
frutas.reverse()  
print('')
print(f'La lista de frutas al revez {frutas}')
    
 