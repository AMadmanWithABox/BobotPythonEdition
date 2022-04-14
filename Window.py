from tkinter import *
import threading, MotionDetection, DirectionSend, ControllerWindow

root = Tk()
t1 = threading.Thread(target = MotionDetection.start_obj_detect)
t2 = threading.Thread(target = ControllerWindow.controller)

DirectionSend.connect()

root.geometry('150x200')

btn1 = Button(root, text = 'Start object detection', bd = '5', command = t1.start)
#btn2 = Button(root, text = 'Start motion following', bd = '5', command = exit)
btn3 = Button(root, text = 'Start controller', bd = '5', command = t2.start)
btn4 = Button(root, text = 'Exit', bd = '5', command = exit)

btn1.pack(side = 'top')
#btn2.pack(side = 'top')
btn3.pack(side = 'top')
btn4.pack(side = 'top')

try:
    root.mainloop()
except:
    print("root did not main loop")

def exit():
    DirectionSend.client.close()
    root.destroy()
    try:
        ControllerWindow.control_win.destroy()
    except:
        print("ControllerWindow does not exist")