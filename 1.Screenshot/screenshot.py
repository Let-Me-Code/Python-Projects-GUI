import time
import pyautogui
import tkinter as tk

def Screenshot():
    name = int(round(time.time() * 1000))
    name = 'Image'+'{}.png'.format(name)
    #time.sleep(2)
    img = pyautogui.screenshot(name)
    img.show()
    root.deiconify()

def delay():
    root.withdraw()
    root.after(1000,Screenshot)

root = tk.Tk()
root.title("Screenshot")
root.iconbitmap(r'screen.ico')
root.geometry("300x300") #You want the size of the app to be 300x300
root.resizable(0, 0)
#frame = tk.Frame(root)
#frame.pack()
root["bg"] = "black"
#titleLabel = tk.Label(root,text="Take screenshot",height = 0,width = 30,font = ('Helvetica', 18, 'bold'),fg="green",bg="white")
#titleLabel.pack()#grid(row = 1,column = 26)
l = tk.Label(text = "",bg = 'black')
l.pack()
l = tk.Label(text = '',bg = 'black')
l.pack()
button = tk.Button(root,text = 'Take Screenshot', height=1, width=20,font = ('Helvetica', 15, 'bold'),fg="green",bg="black",command = delay)
button.pack()#grid(row = 8,column = 22)
l = tk.Label(text = '',bg = 'black')
l.pack()
close = tk.Button(root,text = 'Quit',height=1, width=20,font = ('Helvetica', 15, 'bold'),fg="green",bg="black",command = quit)
close.pack()#grid(row = 16,column = 22)

root.mainloop()
