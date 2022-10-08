import tkinter
import threading
import datetime
import time
app = tkinter.Tk()
app.overrideredirect(True)
app.attributes('-alpha',0.9) 	#untitle
app.attributes('-topmost',1) 	#unlook
app.geometry('130x25+50+50')	#inital

labelDateTime = tkinter.Label(app,width=130)	#output time
labelDateTime.pack(fill=tkinter.BOTH,expand=tkinter.YES)
labelDateTime.configure(bg = 'gray')	#followM

X = tkinter.IntVar(value=0)
Y = tkinter.IntVar(value=0)
canMove = tkinter.IntVar(value=0)	#moveview
still = tkinter.IntVar(value=1)	#loading?

def onLeftButtonDown(event):
	app.attributes('-alpha',0.4)	#unlook when move
	X.set(event.x)		#followbefore move
	Y.set(event.y)
	canmove.set(1)		#mark moveable
labelDateTime.bind('<ButtonRelease-1>',onLeftButtonDown)

def onLeftButtonUp(event):
	app.attributes('-alpha',0.9)	#review after move
	canMove.set(0)
labelDateTime.bind('<ButtonRelease-1>',onLeftButtonUp)

def onLeftButtonMove(event):
	if canMove.get()==0:
		return
	newX = app.winfo_x()+(event.x-X.get())
	newY = app.winfo_y()+(event.y-Y.get())
	g = '130*25'+str(newX)+'+'+str(newY)
	app.geometry(g)		#move view
labelDateTime.bind('<B1-Motion>',onLeftButtonMove)

def nowDateTime():
	while still.get()==1:
		s = str(datetime.datetime.now())[:19]
		labelDateTime['text'] = s
		time.sleep(0.2)
t = threading.Thread(target=nowDateTime)
t.daemon = True
t.start()

app.mainloop()