import cv2
import time
import numpy as np
import SaltandPepperNoiseAdditionandRemoval as sp
 



def videcapture_objectdetect():
    """
   Captures the video and will detect the object(redapple).
   Saves the capture video on capturedvideo.avi file and the object detection in objectdetected.avi file
   also calulates the frames per second
    """
    video = cv2.VideoCapture(0);
    # Number of frames to capture
    
    frame_width = int(video.get(3))
    frame_height = int(video.get(4))

    # Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
    out2 = cv2.VideoWriter('objectdetected.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10,(frame_width,frame_height))
    out1 = cv2.VideoWriter('capturedvideo.avi',cv2.VideoWriter_fourcc('M','J','P','G'),10, (frame_width,frame_height))

 
    # Start time
    start = time.time()
    framecounter=0;
    totalframes=200
   
    # Grab a few frames
    while(True):
  
        ret, frame = video.read()
        if ret == True: 
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            redmin1 = np.array([27,120,52])
            redmin2 = np.array([179,255,185])
                
            mask = cv2.inRange(hsv, redmin1, redmin2)
            res = cv2.bitwise_and(frame,frame, mask= mask)
            
            kernel = np.ones((5,5),np.uint8)
            erosion = cv2.erode(mask,kernel,iterations = 1)
            dilation = cv2.dilate(mask,kernel,iterations = 1)
            
            cv2.imshow('Original',frame)
            cv2.imshow('Mask',mask)
            cv2.imshow('Erosion',erosion)
            cv2.imshow('Dilation',dilation)
            cv2.imshow('res',res)
            
            cv2.imwrite('grabbedmask.png',mask)
            
            
            cv2.imwrite('grabbedresult.png',res)
            
            out1.write(frame)
            out2.write(res)
            
            framecounter=framecounter+1
            if framecounter ==totalframes:
                break
            # Press Q on keyboard to stop recording
            if cv2.waitKey(1) & 0xFF == ord('q'):
              break
        
          # Break the loop
        else:
          break  
        # Convert BGR to HSV
    
    
    # End time
    end = time.time()
 
    # Time elapsed
    seconds = end - start
    print ("Total Time taken : {0} seconds".format(seconds))
 
    # Calculate frames per second
    fps  = totalframes / seconds;
    print ("Total frames per second : {0}".format(fps))
 
    # When everything done, release the video capture and video write objects
    video.release()
    out1.release()
    out2.release()
    
    # Closes all the frames
    cv2.destroyAllWindows()
    

def selectFrame():
    """
    Select one frame from the captured video for adding noise and removal.
    """
    cap = cv2.VideoCapture('capturedvideo.avi')
    count = 0
    img =[]
    while cap.isOpened():
        ret,frame = cap.read()
        if ret == True: 
            img=frame.copy()
            count = count + 1
            if count ==1:
              break
        else:
         break     
    cap.release()
    cv2.destroyAllWindows()
    return img


def doTask():
    """
    Task 1: Video capture and object Detection
    Task 2: Salt and pepper noise addition and removal
    """
    isVideoCaptured= False
    user_choice1 = input('Enter 1 for video capture and object detection \n' )

    if int(user_choice1) == 1:
         videcapture_objectdetect()
         isVideoCaptured= True
         user_choice2  =input ('Enter 2 - for salt and pepper noise  addition and removal \n ') 
         if int(user_choice2)==2:
              if isVideoCaptured:
                imgFile=selectFrame()
                noise_img = sp.sp_noise(imgFile,0.05)
                cv2.imwrite("noiseImage.png",noise_img)
                fin=sp.medianFilter(noise_img)
                cv2.imwrite('filteredImage.png',fin) 
             
    else:
        print ('Please follow the instructions')
        doTask()
            

    
#main method
if __name__ == '__main__' :
    doTask()
    
            
    