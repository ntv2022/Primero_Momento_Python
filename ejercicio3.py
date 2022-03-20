# -Construir un programa para ir de compras en un supermercado que
# permita la construcción del siguiente MENU:
    
    
# 1. Digitar 1 para recibir {código, nombre, precio} de un producto (+0.4)
# 2. Digitar 2 para mostrar todos los productos registrados (+0.4)
# 3. Digitar 3 para permitir buscar por código un producto y editar el precio
# de este (+0.4)
# 4. Digitar 4 para permitir buscar por código un producto y eliminar el
# producto (+0.4)
# 5. Digitar 0 para SALIR

# --------------- Crear los diccionarios base ----------------------

arroz = { 
    'codigo': 'a1',
    'nombre': 'Arroz',
    'precio': 3000
}

panela = {
    'codigo': 'a2',
    'nombre': 'Panela',
    'precio': 2500
}

maiz = {
    'codigo': 'a3',
    'nombre': 'Maiz',
    'precio': 5000
}

# ----------Crear la lista vacia y agregarle los diccionarios-----------

productos = []
 
productos.append(arroz)
productos.append(panela)
productos.append(maiz)
 
# ---------- Mostrar menú al usuario -----------------

print('Menu de compras en supermercado : ')
print('')
 

print('Digitar 1 para recibir {código, nombre, precio} de un producto')
print('Digitar 2 para mostrar todos los productos registrados')
print('Digitar 3 para permitir buscar por código un producto y editar el precio de este')
print('Digitar 4 para permitir buscar por código un producto y eliminar el producto')
print('Digitar 0 para SALIR')
print('')



# ---------- Crear nuevo producto vacio ------------

nuevoProducto = {}
num =''

# ---------- Ingreso del usuario y bucle ------------
     
while(num != 0):
    num = int(input('Digita la opción que deseas :'))
    
    if (num == 0 ):
        print('')
        print('Vuelve pronto!!!')
        break            
    
    elif( num == 1):
         nuevoProducto["codigo"]= input('Ingresa en codigo del producto :')
         nuevoProducto["nombre"]= input('Ingresa en nombre del producto :')
         nuevoProducto["precio"]=int(input('Ingresa en precio del producto :'))
         productos.append(nuevoProducto)
         print('')
         print('Producto agregado correctamente.')

        
    elif (num == 2 ):
           for k in productos:
                     print(' ')
                     print('Producto:')
                     print('\t Código:', k['codigo'])
                     print('\t Nombre:', k['nombre'])
                     print('\t Precio:', k['precio'])
           print('')
            
                                    
                     
    elif (num == 3 ):
        buscar = input('¿Digita el código del producto que buscas? :')
        nuevoPrecio = int(input('Digita el nuevo precio :'))
        
        
        for item in productos:
            if buscar == item['codigo']:
                print(' ')
                
                item.update({'precio': nuevoPrecio}) 
        print('El precio del producto fue actualizado correctamente.')  
    
    elif (num == 4 ):
        buscar = input('¿Digita el código del producto que buscas? :')
        for clave in productos:
            if buscar == clave['codigo']:
                print(' ')
                
                
              
                productos.remove(clave)
                
        print('Producto Eliminado correctamente.')
        print('')
         
    
      
                     
                     
                     
     
  