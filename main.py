from tkinter import *
from tkinter import messagebox
import os

def restart():
    os.system("shutdown /r /t 1")
    messagebox.showinfo("GoToSleepzzz","Set the Bed We'll Go To Sleepzz")
    
def restart_time():
    os.system("shutdown /r /t 20")
    messagebox.showinfo("GoToSleepzzz","Set the Bed We'll Go To Sleepzz")
    
def logout():
     os.system("shutdown -l")
     messagebox.showinfo("GoToSleepzzz","Set the Bed We'll Go To Sleepzz")
    
def shutdown():
    os.system("shutdown /r /t 1")
    messagebox.showinfo("GoToSleepzzz","Set the Bed We'll Go To Sleepzz")
    
st=Tk()
st.title("ShutDown Application")
st.geometry("500x500")
st.config(bg="Black")

r_button=Button(st,text="Restart",activeforeground = "Orange",activebackground="Yellow",font=("Time New Roman",20,"bold"), relief=RAISED, cursor="plus",command=restart)
r_button.place(x=150,y=60,height=50,width=200)

rt_button=Button(st,text="Restart Time",activeforeground = "Orange",activebackground="Yellow",font=("Time New Roman",20,"bold"), relief=RAISED, cursor="plus",command=restart_time)
rt_button.place(x=150,y=170,height=50,width=200)

lg_button=Button(st,text="Log-Out",activeforeground = "Orange",activebackground="Yellow",font=("Time New Roman",20,"bold"), relief=RAISED, cursor="plus",command=logout)
lg_button.place(x=150,y=270,height=50,width=200)

st_button=Button(st,text="ShutDown",activeforeground = "Orange",activebackground="Yellow",font=("Time New Roman",20,"bold"), relief=RAISED, cursor="plus",command=shutdown)
st_button.place(x=150,y=370,height=50,width=200)

st.iconbitmap(r'yellow.ico.ico')
st.mainloop()
