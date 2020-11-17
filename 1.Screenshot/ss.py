import time
from tkinter import *
import pyautogui

def ss():
    name = int(round(time.time() * 1000))  #4542157451212
    name = 'Image'+'{}.png'.format(name)   #Image232634212
    #time.sleep(2)
    img = pyautogui.screenshot(name)
    img.show()
    root.deiconify()

def delay():
    root.withdraw()
    root.after(1000,ss)

root = Tk()
root.title('Screenshot')
root['bg'] = 'black'
root.geometry('300x300')
root.resizable(0,0)
btn1 = Button(root,text='Take Screenshot',font=('Arial',10,'bold'),height = 2,width=18,fg='Blue',bg='black',command = delay).place(x = 85, y= 20)
btn2 = Button(root,text= "Quit",font=('Arial',10,'bold'),height = 2,width=18,fg='Blue',bg='black',command=quit).place(x=85,y=80)



root.mainloop()
