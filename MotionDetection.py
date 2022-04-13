import cv2, sys, numpy, os, DirectionSend



class DirectionAverager:
    directions = []

    def get_average_dir(self):
        dir_avg_arr = [self.directions.count(0),self.directions.count(1),self.directions.count(2)]
        dir_avg_ind = 1
        for i in range(3):
            if dir_avg_arr[i] > dir_avg_arr[dir_avg_ind]:
                dir_avg_ind = i
        self.directions.clear()
        dir_avg_arr.clear()
        if dir_avg_ind == 0:
            DirectionSend.left()
        elif dir_avg_ind == 1:
            DirectionSend.forward()
        elif dir_avg_ind == 2:
            DirectionSend.right()


dir_avg = DirectionAverager()

def start_obj_detect():
    global count
    count = 1
    

    cap = cv2.VideoCapture("http://192.168.8.211:8080/?action=stream");

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
        
        count = send_directions(center_x, center_y, 640, 480, count)

        

        if ret == True:
            cv2.imshow('Frame', frame1)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()

def send_directions(center_x, center_y, frame_w, frame_h, count):
    count += 1
    first_third = frame_w * (1/3)
    second_third = frame_w *(2/3)
    if center_x >= 0 and center_x < first_third:
        dir_avg.directions.append(0)
    elif center_x >= first_third and center_x < second_third:
        dir_avg.directions.append(1)
    elif center_x >= second_third and center_x <= frame_w:
        dir_avg.directions.append(2)
    else:
        raise ArithmeticError("center_x can't be greater than")
    if count >= 51:
        dir_avg.get_average_dir()
        count = 1
        return count
    else:
        return count

