from tkinter import *
import os

def restart():
    os.system('shutdown /r /t 5')
def restart_time():
    os.system('shutdown /r /t 50')
def shutdown():
    os.system('shutdown /s /t 5')
def logout():
    os.system('shutdown -l')

st = Tk()
st.title('help shutdown')
st.geometry('400x400')
st.config(background='#380352',)
r_button = Button(st,text='restart',font=('Times New Romain',20,'bold'),
relief='raised',cursor='plus',border=6,background='#1d1d34',command=restart)
r_button.place(x=118, y=20,height=50,width=200)
l_button = Button(st,text='shutdown',font=('Time New Romain',20,'bold'),
relief='raised',cursor='plus',border=6,background='#f10303',command=shutdown)
l_button.place(x=118,y=90,height=50,width=200)
d_button = Button(st,text='sleep',font=('Times New Romain',20,'bold'),
relief='raised',cursor='plus',border=6,background='#002e11',command=logout)
d_button.place(x=118,y=160,height=50,width=200)

e_button = Button(st,text='restart(long,T)',font=('Times New Romain',20,'bold'),
relief='raised',cursor='plus',border=6,background='#02233d',command=restart)
e_button.place(x=118, y=230,height=50,width=200)
st.mainloop()