
# here intuition of the code is first we will capture the first instance of the video i.e. wihtout cloakand 
# then we will identify the cloak and color of cloak and delete it from frame and after the color of cloak 
# we will replace that part of frame with first captured frame of video (without cloak).

import cv2
import numpy

#initial  function for the calling of trackbar
# whenever the value of trackbar changes it calls for a function and that function we provide in createtrackbar
# as we need nothing to do with the changed value so pe only print ""
def hello(x):
    print("")

# initialization of camera and window
# here bar is the color bar and it is generated for 6 value upper and lower for each saturation and hue
cap=cv2.VideoCapture(0)
bars=cv2.namedWindow("bars")

# trackbar create a bar for color picker
# hue take max 180 and value and saturation takes 255 value

## for blue
cv2.createTrackbar("upper_hue","bars",110,180,hello)
cv2.createTrackbar("upper_saturation","bars",255,255,hello)
cv2.createTrackbar("upper_value","bars",255,255,hello)
cv2.createTrackbar("lower_hue","bars",68,180,hello)
cv2.createTrackbar("lower_saturation","bars",55,255,hello)
cv2.createTrackbar("lower_value","bars",54,255,hello)

## for green

# cv2.createTrackbar("upper_hue","bars",111,180,hello)
# cv2.createTrackbar("upper_saturation","bars",255,255,hello)
# cv2.createTrackbar("upper_value","bars",255,255,hello)
# cv2.createTrackbar("lower_hue","bars",31,180,hello)
# cv2.createTrackbar("lower_saturation","bars",0,255,hello)
# cv2.createTrackbar("lower_value","bars",65,255,hello)


#now choosing our first frame
# capturing the initial frame for creation of background

# here we are running infifnite loop until we get our frame
while(True):
    cv2.waitKey(1000)
    ret,init_frame=cap.read()
    #check if the frame is returned then break
    if(ret):
        break

# start capturing the frames

while(True):
    # reading the frame and convert the color of frame from bgr to hsv
    ret,frame=cap.read()
    inspect=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # getTrackbarpos() gives the current position  number of track bar (from frame)
    #getting the hsv values for masking the cloak

    upper_hue=cv2.getTrackbarPos("upper_hue","bars")
    upper_saturation=cv2.getTrackbarPos("upper_saturation","bars")
    upper_value=cv2.getTrackbarPos("upper_value","bars")
    lower_value=cv2.getTrackbarPos("lower_value","bars")
    lower_hue=cv2.getTrackbarPos("lower_hue","bars")
    lower_saturation=cv2.getTrackbarPos("lower_saturation","bars")

    # kernel is a matrix
    # kernel to be used for dialation
    # dialation is the process of removing small small impurities from frame

    # this line create a 3x3 unit matrix which will apply on whole frame to make it average 
    kernel=numpy.ones((3,3),numpy.uint8)
    # now we make two small tuples of upper and lower values
    upper_hsv=numpy.array([upper_hue,upper_saturation,upper_value])
    lower_hsv=numpy.array([lower_hue,lower_saturation,lower_value])

    # now from inspect take out the frame which consists of color from upper and lower hsv and 
    # subtract it from frame and make it mask
    mask=cv2.inRange(inspect,lower_hsv,upper_hsv)

    # now mask will contain impurities so first we invert the mask and dialate it
    mask=cv2.medianBlur(mask,3)
    mask_inv=255-mask
    mask=cv2.dilate(mask,kernel,5)

    # now we get the area of cloak in mask and now compare with frames to delete the mask and replace it initial frame
    # the mixing of frames in a combination to achieve the required frame

    # now we are separating bgr channels from frame
    b=frame[:,:,0]
    g=frame[:,:,1]
    r=frame[:,:,2]

    # we do and with mask inverse and channels 
    # on doing this mask area will go black and remaining background will remain same becoz 
    # remaining background is there in mask_inv(and mask area is not present)
    # so when we do and only present(true) will result to 1 otherwise 0
    b=cv2.bitwise_and(mask_inv,b)
    g=cv2.bitwise_and(mask_inv,g)
    r=cv2.bitwise_and(mask_inv,r)
    frame_inv=cv2.merge((b,g,r))

    # now we are separating channels from initial frame
    b=init_frame[:,:,0]
    g=init_frame[:,:,1]
    r=init_frame[:,:,2]
    # now we are taking out area equal to only mask area 
    # mask is present and mask_inv is not present so background will go black
    b=cv2.bitwise_and(b,mask)
    g=cv2.bitwise_and(g,mask)
    r=cv2.bitwise_and(r,mask)
    blanket_area=cv2.merge((b,g,r))

    # final merging of both the frames in one frame
    final=cv2.bitwise_or(frame_inv,blanket_area)

    cv2.imshow("Harry's Cloak",final)
    #cv2.imshow("original",frame)


    if(cv2.waitKey(3)==ord('q')):
        break

cv2.destroyAllWindows()
cap.release()
