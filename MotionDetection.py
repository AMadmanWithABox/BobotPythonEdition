import cv2, sys, numpy, os

def start_obj_detect():

    cap = cv2.VideoCapture(0);

    if (cap.isOpened() == False):
        print("Error opening video file")


    while(cap.isOpened()):
        ret, frame1 = cap.read()
        ret, frame2 = cap.read()
        frame1 = cv2.flip(frame1, flipCode=-1)
        frame2 = cv2.flip(frame2, flipCode=-1)

        dif = cv2.absdiff(frame1, frame2)
        dif_gray = cv2.cvtColor(dif, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(dif_gray, (5,5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        largestContour = None

        for contour in contours:
            (tempx, tempy, tempw, temph) = cv2.boundingRect(contour)
            (bigx, bigy, bigw, bigh) = cv2.boundingRect(largestContour)
            if(tempw + temph) > (bigw + bigh):
                largestContour = contour
            if(largestContour.any() != None):
                if(cv2.contourArea(largestContour) > 1000):
                    continue
                else:
                    largestContour = None;
        
        (x, y, w, h) = cv2.boundingRect(largestContour)
        center_x = int(x+(w/2))
        center_y = int(y+(h/2))
        cv2.rectangle(frame1, (center_x, center_y), (center_x + 3, center_y + 3), (255,0,0), 2)
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        

        if ret == True:
            cv2.imshow('Frame', frame1)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()

