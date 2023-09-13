import cv2 as cv
import numpy as np


Bayer_Input = np.array([[100, 10, 110, 11],
                       [9,   50, 8,   49],
                       [105, 12, 112, 9 ],
                       [14,  52, 26,  54]])


#print(Bayer_Input)


#funktion til bayinput
#læser valgte pixel og dens naboer
# er der ikke nok naboer skal der ikke være noget ouput
#Gem så den valgte pixels værdi som dens egen farve
#find derefter de flade naboers gennemsnit indstil som rette værdi
#find derefter de diagonale naboers gennemsnit indstil som rette værdi


RGB = np.zeros((3,3,3))


def RGB_B(x, y):
    RGB[x, y, 0] = Bayer_Input[x+1, y+1]
    RGB[x, y, 1] = Bayer_Input[x, y+1]
    RGB[x, y, 2] = Bayer_Input[x, y]
    

def RGB_GB(x, y):
    RGB[x, y, 0] = Bayer_Input[x+1, y]
    RGB[x, y, 1] = Bayer_Input[x, y]
    RGB[x, y, 2] = Bayer_Input[x, y-1]



def RGB_GR(x, y):
    RGB[x, y, 0] = Bayer_Input[x, y+1]
    RGB[x, y, 1] = Bayer_Input[x, y]
    RGB[x, y, 2] = Bayer_Input[x-1, y]



def RGB_R(x, y):
    RGB[x, y, 0] = Bayer_Input[x, y]
    RGB[x, y, 1] = Bayer_Input[x, y-1]
    RGB[x, y, 2] = Bayer_Input[x-1, y-1]

    





def Bayer_Trans(Matrix):
    for i in range(3):
        for j in range(3):
            if i % 2 == 0 and j % 2 == 0: #Hvis h er 0 eller 2 og b er 0 eller 2
                RGB_B(i, j)
                print('RGB_B')
            elif i % 2 == 0 and j % 2 != 0: #Hvis h er 0 eller 2 og b er 1 eller 3
                RGB_GB(i, j)
                print('RGB_GB')
            elif i % 2 != 0 and j % 2 == 0: #Hvis h er 1 eller 3 og b er 0 eller 2
                RGB_GR(i, j)
                print('RGB_GR')
            elif i % 2 != 0 and j % 2 != 0: #Hvis h er 1 eller 3 og b er 1 eller 3
                RGB_R(i, j)
                print('RGB_')
    while True:
        cv.imshow("Bayer Image", RGB)
        key = cv.waitKey(1)
        if key == ord('q'):
            break
    return
            








Bayer_Trans(Bayer_Input)

print(RGB)



