import cv2
import numpy as np

image = cv2.imread("C:/Users/jccol/OneDrive/estudos/python/IniciandoNovamente/logoIDVL.png")

image_rgba = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)

lower_white = np.array([200, 200, 200, 255], dtype=np.uint8)
upper_white = np.array([255, 255, 255, 255], dtype=np.uint8)

# Cria uma máscara para pixels brancos
mask = cv2.inRange(image_rgba, lower_white, upper_white)

image_rgba[mask == 255] = [0, 0, 0, 0]

cv2.imwrite("image_transparent.png", image_rgba)

print("Imagem com fundo transparente salva como 'image_transparent.png'")
