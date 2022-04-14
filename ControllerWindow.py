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

    btn1.place(x=50, y=25)
    btn2.place(x=25, y=75)
    btn3.place(x=100, y=75)
    btn4.place(x=50, y=125)

    control_win.bind('w', lambda event: DirectionSend.forward())
    control_win.bind('a', lambda event: DirectionSend.left())
    control_win.bind('d', lambda event: DirectionSend.right())
    control_win.bind('s', lambda event: DirectionSend.reverse())

    try:
        control_win.mainloop()
    except:
        print("control_win did not main loop")