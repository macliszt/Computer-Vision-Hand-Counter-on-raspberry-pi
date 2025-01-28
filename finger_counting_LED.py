import cv2
import time
import os
import HandTrackingModule as htm


heightCam = 480
widthCam = 640

cap = cv2.VideoCapture(0)
cap.set(3,widthCam)
cap.set(4,heightCam)


folderPath ="fingerImages"
# To loop round the images
myList = os.listdir(folderPath)
# print(myList)

# To create a list of images

overlaylist = []
for impath in myList:
    image = cv2.imread(f'{folderPath}/{impath}')
    # print(f'{folderPath}/{impath}')


    # To save it
    overlaylist.append(image)

print(len(overlaylist))
pTime = 0

detector = htm.handDetector(detectionCon=0.75)

# To create the finger tips for the thumb, index, middle, ring and pinky finger
tipIds = [4, 8, 12, 16, 20]
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    # a list of landmarks
    lmlist = detector.findPosition(img, draw=False)


    # from the tip of our fingers to know if it is open or closed

    if len(lmlist) != 0:
        fingers = []

        # Thumb
        if lmlist[tipIds[0]][1] > lmlist[tipIds[0] - 1][1]:
                fingers.append(1)

        else:
            fingers.append(0)

        #  4 Fingers
        for id in range(1, 5):
            # To loop and tell us the finger
            if lmlist[tipIds[id]][2] < lmlist[tipIds[id] - 2][2]:
                fingers.append(1)

            else:
                fingers.append(0)

        # print(fingers)

        # To Change the images
        totalFingers = fingers.count(1)
        print(totalFingers)

        # If the size of the image is greater than 200x200 pixels, o resize it
        h,w,c = overlaylist[totalFingers - 1].shape  # Note that h, w, c is for  height, width and channel
        # To overlay the finger image to the original image
        img[0:h, 0:w] = overlaylist[totalFingers - 1]  # note that for the images to be displayed on the screen, it must be 200x200 pixels
        

        # To add a rectangle to show the count
        cv2.rectangle(img, (20,225), (170, 425), (0,255, 0), cv2.FILLED)
        cv2.putText(img, str(totalFingers), (45,375), cv2.FONT_HERSHEY_PLAIN,10, (255, 0, 0), 25)
    # To display the frame rate cT is the current time and pTime is the previous time
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    # To dispay the fps
    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 2)


    # For a lateral inversion image
    # img = cv2.flip(img,1)
    cv2.imshow("Image",img)
    cv2.waitKey(1)




