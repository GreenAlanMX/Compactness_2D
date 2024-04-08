##Compactness

The compactness of an object can be measured by the ratio (perimeter2)/area, which is dimensionless and minimized by a disk [3]. The measure of compactness is an intrinsic property of objects [4]. Therefore, the measure of compactness is invariant under geometric transformations such as: translation, rotation, and scaling. In the digital domain, most shapes have no welldefined contours, that is due to the noise of the input devices used, such as: vidicons, CCD
cameras, scanners, sensors, or analog-to-digital converters.
#####Why is useful find the compacness?
The compactness of is useful to detect elements with differences between different 2D-3D images of objects that may present characteristics when tested.

#####1. Upload a image or make one.
Upload in the file an image 2D.

Image Pillow:

![Captura de pantalla 2024-04-03 211845](https://github.com/GreenAlanMX/Compactness_2D/assets/144835623/996b7900-0c6c-44ed-bb9d-01f6003e54e1)

####2.Convert the image to binary
-In the file “Compacidad2D.py” add the name of you file

```python
Ruta de la imagen
Matriz = convertir_imagen('rectangulo_8.png')
```
To binaty:

![Captura de pantalla 2024-04-03 212246](https://github.com/GreenAlanMX/Compactness_2D/assets/144835623/e1aa1716-1989-444e-9849-8d0d30d44ad7)

####Contact perimeter count

- The funtion "obtener_filas" count number of pixel that fond in the colum in the array, save the number of elements in each list from array.

```python
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
```
- Subtract all 1 to each value in the list.
![Captura de pantalla 2024-04-03 215050](https://github.com/GreenAlanMX/Compactness_2D/assets/144835623/64a565a7-3189-45f8-aaf2-bffa12d61d6e)

```python
#Recorrer la lista
 for i in range(len(conteo_por_fila)):
    if conteo_por_fila[i]!=0:
        #Restar un elemento y sumarlo a la sumatoria
        conteo_por_fila[i] -= 1
        sumatoria += conteo_por_fila[i]
```

- Sum all values in a summation to get the contact perimeter of this position object.
![Captura de pantalla 2024-04-03 215826](https://github.com/GreenAlanMX/Compactness_2D/assets/144835623/cb9e7db3-7037-47a8-9b10-57db94c2769b)

####Change of position of the binary object

To get the total value of the contact perimeter of the object inside the image, is necesary chage the position of the object to get a count to have the missing elements.

```python
 # Transponer la matriz para cambiar entre filas y columnas
    matriz_transpuesta = np.transpose(Matriz)
```

![Captura de pantalla 2024-04-03 220847](https://github.com/GreenAlanMX/Compactness_2D/assets/144835623/b411353a-1f3e-40aa-9543-e0aa2bed750c)


- The funtion "obtener_columnas" do the same that previous funtion.

![Captura de pantalla 2024-04-07 212342](https://github.com/GreenAlanMX/Compactness_2D/assets/144835623/d34bb0e3-5b7b-485d-abb3-2803043dfab9)

- Contact perimeter new position image:

![Captura de pantalla 2024-04-07 212844](https://github.com/GreenAlanMX/Compactness_2D/assets/144835623/236f98df-414b-4402-a179-ba66879c25ed)

####Sum both contact perimeter
- Sum the values of contact perimeter of both position of the object:

def sum_colum_row():
    # Llamar a las funciones obtener_filas() y obtener_columnas() y asignar los resultados a variables
    sumatoria_filas, _ = obtener_filas()
    sumatoria_columnas, _ = obtener_columnas()
    
    # Sumar las sumatorias obtenidas de las filas y las columnas
    pc = sumatoria_filas + sumatoria_columnas
    
    
    print("El perimetro de contacto es:",pc)
    # Devolver el resultado
    return pc

![Captura de pantalla 2024-04-07 213228](https://github.com/GreenAlanMX/Compactness_2D/assets/144835623/90f95abc-3528-48c6-b5bc-72272c9dcb72)

####Substitution of values

Sustitude the value "pc" in the formula to get the compactness in a object 2D.
```python
# Perímetro envolvente
    pe = (4 * area) - (2 * pc)

    # Compacidad discreta
    Cd = (area - (pe / 4)) / (area - np.sqrt(area))
```
####Compactness of the object

- Results of the calculus:

![Captura de pantalla 2024-04-07 214154](https://github.com/GreenAlanMX/Compactness_2D/assets/144835623/9ea7d0ce-3fcd-4246-8fe4-8ca790f690b8)


