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
    num_frames = 120;
    frame_width = int(video.get(3))
    frame_height = int(video.get(4))

    # Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
    out2 = cv2.VideoWriter('objectdetected.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10,(frame_width,frame_height))
    out1 = cv2.VideoWriter('capturedvideo.avi',cv2.VideoWriter_fourcc('M','J','P','G'),10, (frame_width,frame_height))
    print ("Capturing {0} frames".format(num_frames))
 
    # Start time
    start = time.time()
    framecounter=0;
   
    # Grab a few frames
    while(True):
  
        ret, frame = video.read()
        if ret == True: 
        
            
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # 0-10 hue
            redmin1 = np.array([0, 100, 100])
            redmax1 = np.array([10, 256, 256])
            red1 = cv2.inRange(hsv, redmin1, redmax1)
            
            # 170-180 hue
            redmin2 = np.array([160, 100, 100])
            redmax2 = np.array([180, 256, 256])
            red2 = cv2.inRange(hsv, redmin2, redmax2)
            
            mask = red1 + red2

            res = cv2.bitwise_and(frame,frame, mask= mask)
            
            cv2.imshow('frame',frame)
            cv2.imshow('mask',mask)
            out1.write(frame)
            out2.write(res)
            cv2.imshow('res',res)
            framecounter=framecounter+1
            if framecounter ==10:
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
    print ("Time taken : {0} seconds".format(seconds))
 
    # Calculate frames per second
    fps  = num_frames / seconds;
    print ("Estimated frames per second : {0}".format(fps))
 
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
    
            
    