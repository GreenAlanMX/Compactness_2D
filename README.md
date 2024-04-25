##Compactness

A new perimeter for shapes composed of cells is defined. This perimeter is called 
the contact perimeter, which corresponds to the sum of the boundaries of neighboring cells of the 
shape. Also, a relation between the perimeter of the shape and the contact perimeter is presented. 
The contact perimeter corresponds to the measure of compactness proposed here called discrete 
compactness. In this case, the term compactness does not refer to point-set topology, but is related 
to intrinsic properties of objects.[1]. 

The measure of discrete compactness should be an intrinsic property of objects. Therefore, it 
should be invariant under translation, rotation, and scaling. In the digital domain, the measure 
here proposed of discrete compactness depends on the number of the pixels used to the shape. 
In order to make the measure of discrete compactness invariant under scaling.[1]


#####Why is useful find the compacness?


The compactness of is useful to detect elements with differences between different 2D-3D images of objects that may present characteristics when tested.
image analysis and corresponding morphometric data play a crucial role in the classification of elements; The transfer of mathematical and logical methods to find real values to calculate metrics that would be almost impossible to calculate manually leads to the use of different computational methods and the use of programming language tools.
This approach is useful in various fields, including medicine, where it helps study images of organs and detect abnormalities using digital and quantitative tools that rely on intrinsic metrics such as unobtrusive compassion. Access to such data can improve the accuracy of image analysis in digital environments and lead to more effective results.[2]

#####1. Upload a image or make one.

- Upload in the file an image an image ".png" with color of object white.

- Make one use the file "img_Black_and_grey.py"


##### Image:

![Estrella_5](https://github.com/GreenAlanMX/Compactness_2D/assets/144835623/1dce12a8-202d-4000-a328-3f139289dc8e)

####2.Convert the image to binary
-In the file “Compacidad2D_2.py” add the name of you img".png"


```python
Ruta de la imagen
Matriz = convertir_imagen('IMG_8.png')
```

##### To binaty:

![Estrella_Jk](https://github.com/GreenAlanMX/Compactness_2D/assets/144835623/b04d2943-01ae-4c54-99f7-81dcae624ffd)

####2.Contact perimeter count

- This function calculates the sum of adjacent elements in each row of a matrix. It iterates over each row and, for each element in the row, checks whether the element is zero or is the last one in the row. If so, add adjacent elements equal to 1 and add this sum to the list. It then calculates the total sum of all rows and returns the list of sums per row and the total sum.

```python
def obtener_filas(Matriz):
    Caso_2_pc = [] # Función para calcular la suma de elementos adyacentes en cada fila de la matriz
    for fila in Matriz:
        suma_fila = 0
        contador_unos = 0
        for i, elemento in enumerate(fila):
            if elemento == 0 or i == len(fila) - 1: # Contar elementos adyacentes mayores que cero
                if contador_unos > 0:
                    suma_fila += contador_unos
                    contador_unos = 0
                continue
            if elemento > 0 and fila[i + 1] == 0:
                continue
            if elemento > 0 and fila[i + 1] == 1:
                contador_unos += 1
                elemento -= 1
                suma_fila += elemento
        Caso_2_pc.append(suma_fila)
    total_original = sum(Caso_2_pc)
    return Caso_2_pc, total_original
```
- Subtract all to each value in the list.


- Sum all values in a summation to get the contact perimeter of this position object.

![Captura de pantalla 2024-04-24 222200](https://github.com/GreenAlanMX/Compactness_2D/assets/144835623/3c16fdf7-5463-443a-a85d-4b920d6f4c09)

####Change of position of the binary object

To get the total value of the contact perimeter of the object inside the image, is necesary chage the position of the object to get a count to have the missing elements, call the funtion "obtener_matriz_transpuesta" in  "impresion_resultados".


```python
 # Transponer la matriz para cambiar entre filas y columnas
    def obtener_matriz_transpuesta(Matriz):
    return np.transpose(Matriz)
```

![Captura de pantalla 2024-04-20 180334](https://github.com/GreenAlanMX/Compactness_2D/assets/144835623/f6206cb4-98d2-495a-906c-ca23a0cbba6f)

- The funtion "Imprimir_resultados" do the same that previous funtion.

- Contact perimeter new position image:

![Captura de pantalla 2024-04-24 222417](https://github.com/GreenAlanMX/Compactness_2D/assets/144835623/171f6c27-094e-461e-8187-2ec038d9a457)

####Sum both contact perimeter:
- Sum the values of contact perimeter of both position of the object:

```python
def sumar_totales(Matriz):
    # Función para sumar los totales originales y transpuestos
    total_original, total_transpuesta = impresion_resultados(Matriz)
    suma_total = total_original + total_transpuesta
    return suma_total


```
![Captura de pantalla 2024-04-24 223040](https://github.com/GreenAlanMX/Compactness_2D/assets/144835623/ad0c87d2-490e-4968-98a4-db1a5b986c28)
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

![Captura de pantalla 2024-04-20 181959](https://github.com/GreenAlanMX/Compactness_2D/assets/144835623/bac93730-489a-4255-8dfd-285f6978b8f5)

Sources:

1.[E. Bribiesca, Measuring 2-D shape compactness using the contact perimeter, Comput. Math. Appl. 33 (1997) 1–9](https://www.sciencedirect.com/science/article/pii/S0898122197000825)

2.[E. Bribiesca, J.R. Jimenez, V. Medina, R. Valdes, O. Yanez, "A voxel-based measure of discrete compactness for brain imaging," en: Twenty-fifth Annual International Conference of the IEEE Engineering in Medicine and Biology Society, Silver Anniversary, Cancún, México, 2003, pp. 910–913.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4478878/)

