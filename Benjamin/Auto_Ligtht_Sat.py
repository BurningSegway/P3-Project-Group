import numpy as np
import cv2 as cv

#Funktion 1
    #Hvis kamera og centrum tjek
    #vælge farve tjek
    #Returner upper/lower bound hsv værdier af pixel tjek




def Get_HSV():
    cap = cv.VideoCapture(0)
    while True:
        size = 500
        x=0
        print('getting bounds')
        ret, frame = cap.read() #ret is checking if the function works, but if it is i will save the camera output from camera "0" as frame
        video_RS = cv.resize(frame, (size, size)) #Resize image


        pixel_bgr = video_RS[size//2][size//2] #Choose the middel pixel
    
        pixel_bgr_Array = np.array(pixel_bgr)  # seyup array for the pixel

        # Convert the chosen color to HSV
        pixel_hsv = cv.cvtColor(np.uint8([[pixel_bgr_Array]]), cv.COLOR_BGR2HSV)[0][0]

        x=x+1
        print('UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU',)
        print('Pixel ', x)
        print('Pixel color BGR:', pixel_bgr) #Print the pixel in
        print('Pixel color HSV:', pixel_hsv) #Print the pixel in

        img = cv.rectangle(video_RS, ((size//2)-size//100*2,(size//2)-size//100*2), ((size//2)+size//100*2, (size//2)+size//100*2), (0, 0, 255), 1)
        img = cv.line(img, ((size//2), (size//2)-size//100*2), ((size//2),(size//2)-1), (0, 0, 255), 1)

        cv.imshow("Video", img) #Here we create a window which shows the video/image




        # Define a range for varying hue values (e.g., -30 to +30 degrees)
        hue_range = 5

        # Calculate lower and upper bounds for the hue
        lower_hue = (pixel_hsv[0] - hue_range) % 180  # Hue values wrap around 0-179
        upper_hue = (pixel_hsv[0] + hue_range) % 180

        # Define constant values for saturation and value (you can adjust these as needed)
        constant_saturation = 255
        constant_value = 255

        # Create lower and upper bounds for the color range in HSV
        lower_bound = np.array([lower_hue, constant_saturation, constant_value], dtype=np.uint8)
        upper_bound = np.array([upper_hue, constant_saturation, constant_value], dtype=np.uint8)

        print("Lower HSV Bound:", lower_bound)
        print("Upper HSV Bound:", upper_bound)

        if cv.waitKey(1) == ord('q'): #If q is pressed while this is running, break the while loop
            break
    
    cap.release() #make the camera available again
    cv.destroyAllWindows() # close all windows
    return(lower_bound[0], upper_bound[0])


#Funktion 2 
    #Hvis billedet med pre instillede værdier
    #Ændre værdier i terminal
    #Når værdier er valgt returner dem med knap

LS = 0
LV = 0
US = 255
UV = 255

def set_SV(low, high, LS, LV, US, UV):
    cap = cv.VideoCapture(0)
    while True:
        size = 500

        ret, frame = cap.read() #ret is checking if the function works, but if it is i will save the camera output from camera "0" as frame
        video_RS = cv.resize(frame, (size, size)) #Resize image

        if not ret:
            print('no image found')
            break

        frame_hsv = cv.cvtColor(video_RS, cv.COLOR_BGR2HSV)


        lower_HSV_Bound = np.array([low, LS, LV])  # Adjust these values
        upper_HSV_Bound = np.array([high, US, UV])  # Adjust these values
        

            
        mask = cv.inRange(frame_hsv, lower_HSV_Bound, upper_HSV_Bound)

        result = cv.bitwise_and(video_RS, video_RS, mask=mask)

        cv.imshow("Video", result) #Here we create a window which shows the video/image


        key = cv.waitKey(1)
        if key == ord('q'):

            break
        elif key == ord('a'):
            LS += 16
            print('LS =', LS)
        elif key == ord('s'):
            LV += 16
            print('LV =', LV)
        elif key == ord('d'):
            US -= 16
            print('US =', US)
        elif key == ord('f'):
            UV -= 16
            print('UV =', UV)


        
    cap.release() #make the camera available again
    cv.destroyAllWindows() # close all windows
    return low, LS, LV, high, US, UV









def main():
    print('hello world')
    low, high = Get_HSV()
    print('getting bounds')
    set_SV(low, high, LS, LV, US, UV)

main()














