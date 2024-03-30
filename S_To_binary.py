from PIL import Image
import numpy as np

#Código para convertir una imagen en pillow a binario


def convertir_imagen(image_path, umbral=128):
    # Abre una imagen usando Pillow
    imagen = Image.open(image_path).convert('L')  # Convierte la imagen a escala de grises

    # Convierte la imagen a un array NumPy
    imagen_array = np.array(imagen)

    # Convierte la imagen a binario usando el umbral
    imagen_binaria = (imagen_array > umbral).astype(int)
    return imagen_binaria

# Ruta de la imagen
image_path = 'rectangulo_8.png'

# Llama a la función para convertir la imagen y obtener el array binario
Mi_test = convertir_imagen(image_path)

# Imprime el resultado
print("Resultado de la conversión:")
print(Mi_test)

#Segundo triunfo del día Alan ;)


