import numpy as np
from S_To_binary import convertir_imagen

#Código que encuestra la compacidad de una imagen binaria

Matriz = convertir_imagen('rectangulo_8.png')#Usa una funcion para convertir una imagen a binario

def obtener_filas():
 # Obtener las dimensiones de la matriz
 filas, columnas = Matriz.shape
 
 # Inicializar una lista para almacenar los conteos de elementos mayores a cero por fila
 conteo_por_fila = []
  # Recorrer cada fila de la matriz
 for fila in range(filas):
    # Inicializar el conteo de elementos mayores a cero en cero para esta fila
    conteo = 0
    # Recorrer cada elemento de la fila
    for elemento in Matriz[fila]:
        # Verificar si el elemento es mayor a cero
        if elemento > 0:
            # Incrementar el conteo si el elemento es mayor a cero
            conteo += 1
    # Agregar el conteo de esta fila a la lista de conteos por fila
    conteo_por_fila.append(conteo)

  
 #Inicio de la variable sumatoria  de los valores verticales e horizontales
 sumatoria=0
 
 #imprime resultado
 print("Total de elementos por fila:", conteo_por_fila)
 
 #Recorrer la lista
 for i in range(len(conteo_por_fila)):
    if conteo_por_fila[i]!=0:
        #Restar un elemento y sumarlo a la sumatoria
        conteo_por_fila[i] -= 1
        sumatoria += conteo_por_fila[i]
        
    
        
       

 print("Total de elementos por fila:", conteo_por_fila)
 #Imprimir la sumatoria de los valores restados
 print("Sumatoria de valores restados:",sumatoria)
 
 
 return sumatoria, conteo_por_fila#Devuelve los valores obtenidos para que las demas funciones las puedan emplear


def obtener_columnas():
    # Transponer la matriz para cambiar entre filas y columnas
    matriz_transpuesta = np.transpose(Matriz)
    
    # Obtener las dimensiones de la matriz
    filas, columnas = matriz_transpuesta.shape
    
    # Inicializar una lista para almacenar los conteos de elementos diferentes de cero por fila
    conteo_por_fila = []
    
    # Recorrer cada fila de la matriz transpuesta
    for fila in range(filas):
        # Inicializar el conteo de elementos diferentes de cero en cero para esta fila
        conteo = 0
        # Recorrer cada elemento de la fila
        for elemento in matriz_transpuesta[fila]:
            # Verificar si el elemento es diferente de cero
            if elemento != 0:
                # Incrementar el conteo si el elemento es diferente de cero
                conteo += 1
        # Agregar el conteo de esta fila a la lista de conteos por fila
        conteo_por_fila.append(conteo)
    
    print("Matriz resultante:")#Imprime la matriz invertida
    print(matriz_transpuesta)
    #Lista antes de que sus elementos sean restados -1
    print("Total de elementos por columna:", conteo_por_fila)
    
    # Restar 1 a cada elemento de la lista que sea diferente de cero
    for i in range(len(conteo_por_fila)):
        if conteo_por_fila[i] != 0:
            conteo_por_fila[i] -= 1
    
    # Calcular la sumatoria de los valores restados
    sumatoria = sum(conteo_por_fila)
    
    # Imprimir la matriz transpuesta y los resultados
    print("Total de elementos por columa:", conteo_por_fila)
    print("Sumatoria de valores restados:", sumatoria)
    
    
    
    return sumatoria, conteo_por_fila#Devuelve los valores obtenidos para que las demas funciones las puedan emplear

def sum_colum_row():
    # Llamar a las funciones obtener_filas() y obtener_columnas() y asignar los resultados a variables
    sumatoria_filas, _ = obtener_filas()
    sumatoria_columnas, _ = obtener_columnas()
    
    # Sumar las sumatorias obtenidas de las filas y las columnas
    pc = sumatoria_filas + sumatoria_columnas
    
    
    print("El perimetro de contacto es:",pc)
    # Devolver el resultado
    return pc

    
def compacidad2D(Matriz):
    
    pc=sum_colum_row()
    area=np.count_nonzero(Matriz)
    
    # Perímetro envolvente
    pe = (4 * area) - (2 * pc)

    # Compacidad discreta
    Cd = (area - (pe / 4)) / (area - np.sqrt(area))
    
    # Devolver los resultados como una tupla
    print("Compacidad discreta es:",Cd)
    print("Perimetro envolvente es:",pe)
    print("El area es:",area)
    print("El perimetro de contacto es:",pc)
    

    return Cd, pe, area, pc

# Llama a la función con la matriz de prueba y guarda el resultado
resultado = compacidad2D(Matriz)

# Imprime el resultado
print("Resultado:", resultado)
