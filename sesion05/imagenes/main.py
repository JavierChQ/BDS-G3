from PIL import Image, ImageFont, ImageDraw
image = Image.open('messi.jpg')
print(image.size)
print(image.mode)
print(image.format)

# # Convertir imagen a blanco y negro
# image_blackwhite = image.convert('L')
# image_blackwhite.show()

# Redimensionar una imagen
width = image.size[0]
height = image.size[1]
print(f'Ancho: {width}')
print(f'Alto: {height}')

new_width = width // 5
new_height = height // 5 # "//": para que la division sea un entero

print(f'Nuevo ancho: {new_width}')
print(f'Nuevo alto: {new_height}')

new_size = (new_width,new_height)

image_short = image.resize(new_size)
#image_short.show()
image_short.save('messi_short.jpg','JPEG',quality=90)

# Incrustar texto en la imagen
font = ImageFont.truetype('Roboto-Bold.ttf',120)
draw = ImageDraw.Draw(image)
draw.text(
    (10,0),
    "Javier chacnama",
    (255,255,255),
    font
)
image.show()
