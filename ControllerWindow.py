from tkinter import *
import DirectionSend

def controller():
    global control_win
    control_win = Tk()

    control_win.geometry('150x200')

    btn1 = Button(control_win, text = 'Forward', bd = '5', command = DirectionSend.forward)
    btn2 = Button(control_win, text = 'Left', bd = '5', command = DirectionSend.left)
    btn3 = Button(control_win, text = 'Right', bd = '5', command = DirectionSend.right)
    btn4 = Button(control_win, text = 'Reverse', bd = '5', command = DirectionSend.reverse)

    btn1.pack(side = 'top')
    btn2.pack(side = 'left')
    btn3.pack(side = 'right')
    btn4.pack(side = 'bottom')

    try:
        control_win.mainloop()
    except:
        print("control_win did not main loop")