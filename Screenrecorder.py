import cv2
import numpy as np
import pyautogui
screen_size=(1920,1080)#setting recording window size
fourcc=cv2.VideoWriter_fourcc(*"XVID")#for encoding video (*XVID for avi format)
out=cv2.VideoWriter("output.avi",fourcc,20.0,screen_size)#creating output for saving the video
while True:
    img=pyautogui.screenshot()#store pixel intensity
    frame=np.array(img)#converting image variable into numpy array
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)#converting it into image
    out.write(frame)#for checking output
    cv2.imshow("show",frame)
    if(cv2.waitKey(1)==ord("q")):
        break
                           
