import cv2
import numpy as np

#Creamos el objetto de video
captura = cv2.VideoCapture(0)

fondo = None

while True:
        #Capturamos frame a frame
        (grabbed, imagen) = captura.read()
        # Si hemos llegado al final del vÃ­deo salimos
        if not grabbed:
            break
        #----------------------------------------------
        #PASO_1: CONVERSION A ESCALA DE GRISES
        gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        #----------------------------------------------

        #----------------------------------------------
        # PASO_2: DEFINICION DE FONDO
        # Si todavía no hemos obtenido el fondo, lo obtenemos
        # Será el primer frame que obtengamos
        if fondo is None:
                fondo = gris            
                continue
        cv2.imshow('Fondo', fondo)
        #----------------------------------------------
        #----------------------------------------------
        # PASO_3: RESTA DE FRAME ACTUAL Y FONDO PREDEFINIDO
        resta = cv2.absdiff(gris,fondo)
        cv2.imshow('Resta', resta)
        #----------------------------------------------

        #Mostramos imagen  
        cv2.imshow('Video', imagen)
        #Capturamos teclado
        tecla = cv2.waitKey(25) & 0xFF
        #Salimos si la tecla presionada es ESC
        if tecla == 27:
                 break
        if tecla == ord('n'):#con N se defien nuevo fondo
                fondo = gris            
                continue
#Liberamos objeto                                                  
captura.release()
#Destruimos ventanas
cv2.destroyAllWindows()

