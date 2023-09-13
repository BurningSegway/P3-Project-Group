import numpy as np
import cv2 as cv






#Funktion 1
#Hvis RGB component værdier af video i et vindue delt i fire

def RGB_Component():
    cap = cv.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        width = int(cap.get(3))
        height = int(cap.get(4))

        smallerImage = cv.resize(frame, (0, 0), fx=0.5, fy=0.5)
        image_Blue, image_Green, image_Red = cv.split(smallerImage)

        # Create a larger black frame to contain all color channels
        combined_image = np.zeros((height, width, 3), dtype=np.uint8)

        # Place the color channels in their respective quadrants
        combined_image[ :height//2, :width//2, 0] = image_Blue
        combined_image[ :height//2, width//2:, 1] = image_Green
        combined_image[ height//2:, :width//2, 2] = image_Red

        # Resize the smaller image to match the quadrant size
        smallerImage = cv.resize(smallerImage, (width // 2, height // 2))

        # Place the smaller image in the last available quadrant (RGB channels)
        combined_image[ height//2:, width//2:] = smallerImage

        cv.imshow("Video", combined_image)

        if cv.waitKey(1) == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()


def RGB_Component_Real():
    cap = cv.VideoCapture(0)
    while True:
        #size = 500

        #ret, frame = cap.read() #ret is checking if the function works, but if it is i will save the camera output from camera "0" as frame
        #video_RS = cv.resize(frame, (size, size)) #Resize image
        #input_image = video_RS


        input_image = cv.imread('C:/Users/bebj2/Downloads/letter.png', 1)



        red = input_image[:, :, 2]
        green = input_image[:, :, 1]
        blue = input_image[:, :, 0]


        #lower_red_Bound = np.array([200, 200, 200])  # Adjust these values
        #upper_red_Bound = np.array([255, 255, 255])  # Adjust these values
        
        green = cv.bitwise_not(green)    

        mask = cv.inRange(red, 190, 230)

        result = cv.bitwise_and(red, red, mask=mask)


        #cv.imshow("Input image", input_image)
        cv.imshow("Red channel", red)
        cv.imshow("result", result)
        cv.imshow("Green channel", green)
        #cv.imshow("Blue channel", blue)
        #cv.waitKey(0)

        key = cv.waitKey(1)
        if key == ord('q'):
            break
    
    cap.release()
    cv.destroyAllWindows()
    return

RGB_Component_Real()

#def main():
    


#main()



