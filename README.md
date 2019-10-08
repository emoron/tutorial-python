import cv2 as cv
import numpy as np

def Filtro (name_image):
    #Lee imagen
    imagen_original = cv.imread(name_image)
    #Convertimos a escala de grises
    grayScale = cv.cvtColor(imagen_original, cv.COLOR_BGR2GRAY)
    #Recortamos
    crop_imagen = grayScale[50:100 , 50:163]
    cv.imshow('ImagenRecortada',crop_imagen)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return 'ok'
Filtro('C:/Users/danil/Desktop/Proyecto/imagenes_png/1.jpg')
