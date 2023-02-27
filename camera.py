import cv2
#initilizing web cab using VideoCapture(0) method
cam=cv2.VideoCapture(0)
img_counter=0
while True:
    ret,frame=cam.read()
    if not ret:
        print("Failed to capture a picture")
        break
    cv2.imshow("test",frame)
    #close the application
    k=cv2.waitkey(1)
    #27==escape key,32==space key
    if k%256==27:
        print("escape hit,closing the app")
        break
    elif k%256==32:
        img_name="opencv+frame_{}.png".format(img_counter)
        cv2.imwrite(img_name,frame)
        print("screenshoot taken")
        img_counter+=1
cam.release()
cam.destoryAllWindows()