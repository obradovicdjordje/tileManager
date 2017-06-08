from Tkinter import Tk
from Tkinter import ANCHOR, END, Listbox

import Xlib.display
from Xlib import X
import tkFont

import Xlib.display

disp = Xlib.display.Display()
root = disp.screen().root
NET_ACTIVE_WINDOW = disp.intern_atom('_NET_ACTIVE_WINDOW')

screen = Xlib.display.Display().screen()
root_win = screen.root

commands = ['0',
            '00',
            '0-',
            '0_',
            '1',
            '2',
            '3',
            '4']

display = Xlib.display.Display()
window = display.get_input_focus().focus
tt = window
win_id = root.get_full_property(NET_ACTIVE_WINDOW, Xlib.X.AnyPropertyType).value[0]

x = 0
y = 0
W = 0
H = 0
for i in range(2):
    tt = tt.query_tree().parent
    geom = tt.get_geometry()
    print geom.x, geom.y, geom.width, geom.height
    x += geom.x
    y += geom.y
    if(i==0):
        W = geom.width
        H = geom.height

WW1 = 1598
HH1 = 1173

WW2 = 1918
HH2 = 1173

def find_window():
    windowID = None
    windowIDs = root_win.get_full_property(display.intern_atom('_NET_CLIENT_LIST'), Xlib.X.AnyPropertyType).value
    for windowID in windowIDs:
        if(windowID == win_id):
            window1 = display.create_resource_object('window', windowID)
            return window1

def keyPressed(event):
    selection=tList.curselection()
    comm = tList.get(selection[0])
    print comm
    window = find_window()
    if(window != None):
        if(comm == '0'):
            window.configure(x=100, y=100, width=WW1-100, height=HH1-400)
        elif(comm == '00'):
            window.configure(x=100, y=HH1-270, width=WW1-100, height=250)
        elif(comm == '0-'):
            window.configure(x=WW1+100, y=100, width=WW2-100, height=HH2-400)
        elif(comm == '0_'):
            window.configure(x=WW1+100, y=HH1-270, width=WW2-100, height=250)
        elif(comm == '1'):
            window.configure(x=10, y=20, width=WW1/2-20, height=HH1/2-20)
        elif(comm == '2'):
            window.configure(x=WW1/2, y=20, width=WW1/2-20, height=HH1/2-20)
        elif(comm == '3'):
            window.configure(x=10, y=HH1/2, width=WW1/2-20, height=HH1/2-20)
        elif(comm == '4'):
            window.configure(x=WW1/2, y=HH1/2, width=WW1/2-20, height=HH1/2-20)

    window.set_input_focus(X.RevertToParent, X.CurrentTime)
    window.configure(stack_mode=X.Above)
    display.sync()
    top.destroy()

def finish(event):
    top.destroy()

top = Tk()
small_font = tkFont.Font(size=11)

w = 200
h = 200
top.geometry('%dx%d+%d+%d' % (w, h, x+W-w-30, y+50))

tList = Listbox(bd=1, height=10, font=small_font)
tList.bind("<Return>", keyPressed)
tList.bind("<Escape>", finish)
tList.pack()
tList.focus_set()

for item in commands:
    tList.insert(END, item)

top.mainloop()
