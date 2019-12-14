import cv2
import numpy as np

#Creamos el objetto de video
captura = cv2.VideoCapture(0)

while True:
        #Capturamos frame a frame
        (grabbed, imagen) = captura.read()
        # Si hemos llegado al final del vídeo salimos
        if not grabbed:
            break

        #----------------------------------------------
        #PASO_1: CONVERSION A ESCALA DE GRISES
        gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        #----------------------------------------------

        #Mostramos imagen  
        cv2.imshow('Video', gris)
        #Capturamos teclado
        tecla = cv2.waitKey(25) & 0xFF
        #Salimos si la tecla presionada es ESC
        if tecla == 27:
                 break
#Liberamos objeto                                                  
captura.release()
#Destruimos ventanas
cv2.destroyAllWindows()

