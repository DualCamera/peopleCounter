#!/usr/bin/python3
import cv2

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

    while(True): 
        # Capture frame-by-frame
        ret, frame = cap.read()

        #Aplica substraccion de fondo
        fgmask = fgbg.apply(frame)

        # Display the resulting frame
        cv2.imshow('background',fgmask)

        #Waits for a user input to quit the application
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()

    print('bye')
