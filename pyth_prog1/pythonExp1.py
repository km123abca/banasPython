from tkinter import *
from tkinter import ttk 



def calc(n1,n2,operr='+'):
	if operr=='+':
		return n1+n2
	elif operr=='-':
		return n1-n2
	elif operr=='x':
		return n1*n2
	elif operr=='/':
		return n1/n2

def butpressed(num=1):
	global firstnum,secondnum,opercomplete,minuspressed
	if opercomplete:
		firstnum=0
		opercomplete=False
	if minuspressed:
		num*=-1
		minuspressed=False
	if firstactive and not(secondactive):
		firstnum=firstnum*10+num
		outputdisp.delete(0,"end")
		outputdisp.insert(0,firstnum)
	elif secondactive:
		secondnum=secondnum*10+num
		outputdisp.delete(0,"end")
		outputdisp.insert(0,secondnum)

def operpressed(oper):
	global operstored,firstactive,secondactive,firstnum,secondnum,opercomplete,minuspressed
	print(oper+" pressed")
	if opercomplete:
		if(oper=='-'):
			minuspressed=True
		opercomplete=False
	if(oper=='=') or secondactive:
		if not(secondactive):
			opercomplete=True
			return False
		resnum=calc(firstnum,secondnum,operstored)
		if oper!='=':
			operstored=oper
		else:
			operstored='p'
		outputdisp.delete(0,"end")
		outputdisp.insert(0,resnum)
		#print(resnum)
		firstactive=True
		secondactive=False
		firstnum,secondnum=resnum,0
		opercomplete=True
	else:
		if firstnum==0 and oper=='-':
			minuspressed=True
			return True
		secondactive=True
		operstored=oper
		print(operstored+' was stored')

def clearallz():
	firstnum=0
	secondnum=0
	operstored='p'
	firstactive=True
	secondactive=False
	opercomplete=False
	minuspressed=False
	outputdisp.delete(0,"end")
	outputdisp.insert(0,0)
##########Global Variables################
firstnum=0
secondnum=0
operstored='p'
firstactive=True
secondactive=False
opercomplete=False
minuspressed=False
##########Global Variables################


root=Tk()
root.title("Calculator")
root.geometry("400x350")
root.resizable(height=False,width=False)

frame1=Frame(root)
frame2=Frame(root)



outputdisp=Entry(frame1,width=60)
outputdisp.grid(row=0, column=1,sticky=W, pady=10)


###################  ROW 1 ###################################################
sevbutton=Button(frame2, text="7",width=10,height=3,command=lambda:butpressed(7))
sevbutton.grid(row=0,column=1,sticky=W)

eigbutton=Button(frame2, text="8",width=10,height=3,command=lambda:butpressed(8))
eigbutton.grid(row=0,column=2,sticky=W,padx=12,pady=8)

ninbutton=Button(frame2, text="9",width=10,height=3,command=lambda:butpressed(9))
ninbutton.grid(row=0,column=3,sticky=W,padx=12,pady=8)

divbutton=Button(frame2, text="/",width=10,height=3,command=lambda:operpressed('/'))
divbutton.grid(row=0,column=4,sticky=W)
###################  ROW 1 ###################################################



###################  ROW 1 ###################################################
fourbutton=Button(frame2, text="4",width=10,height=3,command=lambda:butpressed(4))
fourbutton.grid(row=1,column=1,sticky=W)

fivbutton=Button(frame2, text="5",width=10,height=3,command=lambda:butpressed(5))
fivbutton.grid(row=1,column=2,sticky=W,padx=12,pady=8)

sixbutton=Button(frame2, text="6",width=10,height=3,command=lambda:butpressed(6))
sixbutton.grid(row=1,column=3,sticky=W,padx=12,pady=8)

mulbutton=Button(frame2, text="X",width=10,height=3,command=lambda:operpressed('x'))
mulbutton.grid(row=1,column=4,sticky=W)
###################  ROW 1 ###################################################

###################  ROW 1 ###################################################
onebutton=Button(frame2, text="1",width=10,height=3,command=lambda:butpressed(1))
onebutton.grid(row=2,column=1,sticky=W)

twobutton=Button(frame2, text="2",width=10,height=3,command=lambda:butpressed(2))
twobutton.grid(row=2,column=2,sticky=W,padx=12,pady=8)

thrbutton=Button(frame2, text="3",width=10,height=3,command=lambda:butpressed(3))
thrbutton.grid(row=2,column=3,sticky=W,padx=12,pady=8)

plubutton=Button(frame2, text="+",width=10,height=3,command=lambda:operpressed('+'))
plubutton.grid(row=2,column=4,sticky=W)
###################  ROW 1 ###################################################


###################  ROW 1 ###################################################
acbutton=Button(frame2, text="AC",width=10,height=3,command=lambda:clearallz())
acbutton.grid(row=4,column=1,sticky=W)

zrbutton=Button(frame2, text="0",width=10,height=3,command=lambda:butpressed(0))
zrbutton.grid(row=4,column=2,sticky=W,padx=12,pady=8)

eqbutton=Button(frame2, text="=",width=10,height=3,command=lambda:operpressed('='))
eqbutton.grid(row=4,column=3,sticky=W,padx=12,pady=8)

minbutton=Button(frame2, text="-",width=10,height=3,command=lambda:operpressed('-'))
minbutton.grid(row=4,column=4,sticky=W)
###################  ROW 1 ###################################################





frame1.grid(row=0,sticky=W)
frame2.grid(row=1,sticky=W)







root.mainloop()
