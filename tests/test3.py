#!/usr/bin/python3
import cv2
import numpy as np

print("CV version", cv2.__version__)

def main():
    cap = cv2.VideoCapture(0)
    if not (cap.isOpened()):
        print("Could not open video device")
        exit()

    print("Done")

    #To set the resolution 
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    #Substractor de fondo
    fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows = True)

    #Elementos estructurantes para filtros morfoogicos
    kernelOp = np.ones((3,3),np.uint8)
    kernelCl = np.ones((11,11),np.uint8)

    while(True): 
        # Capture frame-by-frame
        ret, frame = cap.read()

        #Aplica substraccion de fondo
        fgmask = fgbg.apply(frame)

        #Binarizacion para eliminar sombras (color gris)
        try:
            ret,imBin= cv2.threshold(fgmask,200,255,cv2.THRESH_BINARY)
            #Opening (erode->dilate) para quitar ruido.
            mask = cv2.morphologyEx(imBin, cv2.MORPH_OPEN, kernelOp)
            #Closing (dilate -> erode) para juntar regiones blancas.
            mask =  cv2.morphologyEx(mask , cv2.MORPH_CLOSE, kernelCl)
        except:
            print('EOF')
            break

        # Display the resulting frame
        cv2.imshow('original',frame)
        cv2.imshow('background',fgmask)
        cv2.imshow('shadow less',mask)

        #Waits for a user input to quit the application
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()

    print('bye')
