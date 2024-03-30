from PIL import Image, ImageDraw

#Código para crear una imagen

# Dimensiones de la imagen
width = 15
height = 15

# Crea una nueva imagen en blanco
image = Image.new("RGB", (width, height), color="black")

# Crea un objeto ImageDraw para dibujar en la imagen
draw = ImageDraw.Draw(image)

# Coordenadas del rectángulo (start_point_rect, end_point_rect)
start_point_rect = (4, 4)
end_point_rect = (7, 9)

# Dibuja un rectángulo blanco en la imagen
draw.rectangle([start_point_rect, end_point_rect], fill="white")

# Guarda la imagen en el formato deseado
image.save("rectangulo_7.png")

# Muestra la imagen
image.show()
