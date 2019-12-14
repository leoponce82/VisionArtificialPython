import cv2
import numpy as np
import os
import datetime
import pyttsx3

#config para voz speech
engine = pyttsx3.init()
engine.setProperty('voice', voices[3].id)#existen indices 0 y 1 y 2 y 3

#Creamos el objetto de video
captura = cv2.VideoCapture(0)

fondo = None
# crear una carpeta en C: para guardar registro de actividad
carpeta = r'Registro_mov'

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
        #----------------------------------------------
        # PASO_4: UMBRALIZACION
        _,MASCARA = cv2.threshold(resta,100,255,cv2.THRESH_BINARY)
        cv2.imshow('Mascara', MASCARA)
        #----------------------------------------------
        #----------------------------------------------
        # PASO_5: CONTEO DE PIXELES BLANCOS
        pixeles_blancos = cv2.countNonZero(MASCARA)
        #print ("Numero de pixeles blancos: ", pixeles_blancos) 
        #----------------------------------------------
        #----------------------------------------------
        # PASO_6: REGISTRO LOCAL
        if pixeles_blancos > 50:
                                
                # --- definir formato para guardar 18h-5m-12s
                ahora = datetime.datetime.now()
                hora = str(ahora.hour)
                minuto = str(ahora.minute)
                segundo = str(ahora.second)
                nombre_imagen = hora+'h-'+minuto+'m-'+segundo+'s'+'.jpg'
                os.chdir(r'D:\Personal\Academic\CursoVisionArtificialPython\DETECTOR_MOVIMIENTO\DETECTOR_MOVIMIENTO\Registro_mov')
                #cv2.imwrite(os.path.join(carpeta , nombre_imagen), imagen)
                cv2.imwrite(nombre_imagen, imagen)
                #se envia el speech
                #engine.say('Movimiento detectado')
                #engine.runAndWait()
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

