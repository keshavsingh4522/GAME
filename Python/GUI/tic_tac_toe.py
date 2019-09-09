from tkinter import *
from tkinter import messagebox
root=Tk()
root.title('tic tac toe')
root.config(bg='purple')
p=False
photo1=PhotoImage(file='o.png').subsample(4, 4)
photo2=PhotoImage(file='x_1.png').subsample(4, 4)
photo3=PhotoImage(file='xoox.png').subsample(4, 4)
pl1=set()
pl2=set()
def display(x):
    global p
    global lb
    global photo1
    global photo2
    k=x[0]*3+x[1]
    if p==False:
        lb[k]['image']=photo1
        p=True
        pl1.add(k+1)
        check(k)
    else:
        lb[k]['image']=photo2
        p=False
        pl2.add(k+1)
        check(k)
#     messagebox.showerror("Error","Error message")
#     messagebox.showwarning("Warning","Warning message")
#     messagebox.showinfo("Result", "player 1 win")
def start():
    global b
    global pl1
    global pl2
    global photo3
    global count
    count=0
    pl1.clear()
    pl2.clear()
    if b['text']=='restart_game':
        b['text']='start_game'
        for i in range(3):
            for j in range(3):
                lb[i*3+j]['state']='disabled'
                lb[i*3+j]['image']=photo3
    else:
        b['text']='restart_game'
        for i in range(3):
            for j in range(3):
                lb[i*3+j]['state']='active'
                lb[i*3+j]['image']=photo3
count=0
def check(k):
    global pl1
    global pl2
    global p
    global lb
    global count
    count+=1
    lb[k]['state']='disabled'
    win=[{1,2,3},{4,5,6},{7,8,9},{1,5,9},{3,5,7},{1,4,7},{2,5,8},{3,6,9}]
    if p==True:
        for s in win:
            if s<=pl1:
                messagebox.showinfo('result','player-1 win')
                start()
    else:
        for s in win:
            if s<=pl2:
                messagebox.showinfo('result','player-2 win')
                start()
    if count==9:
        messagebox.showinfo('result','game draw')
        start()
lb=[]
# photo=PhotoImage(file='o.png').subsample(4, 4)
for i in range(3):
    for j in range(3):
        lb.append(Button(root,state='disabled',image=photo3,command=lambda x=(i,j):display(x)))
        lb[-1].grid(row=i,column=j,sticky='nswe')
        root.rowconfigure(i,weight=1)
        root.columnconfigure(j,weight=1)
# lb[1]['image']=PhotoImage(file='x.png').subsample(4, 4)
b=Button(root,text='start_game',relief='flat',command=start)
b.grid(row=3,column=0,columnspan=3,sticky='nswe')
root.mainloop()
