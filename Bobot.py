import cv2, sys, numpy, os

cap = cv2.VideoCapture(0);

if (cap.isOpened() == False):
    print("Error opening video file")

while(cap.isOpened()):
    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    dif = cv2.absdiff(frame1, frame2)
    dif_gray = cv2.cvtColor(dif, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(dif_gray, (5,5), 0)
    _, 

    if ret == True:
        cv2.imshow('Frame', blur)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()