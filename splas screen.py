from tkinter import *
import customtkinter
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

sr = Tk()
sr.title()
wid1 =sr.winfo_screenwidth()
hei1 = sr.winfo_screenheight()
sr.geometry(str(wid1)+"x" +str(hei1))

sr.overrideredirect(True)
sl = Label(sr, text="SPLASH SCREEN", font=("Sans-serif",18), bg="magenta", fg="black")
sl.pack()

def main():
    sr.destroy()
    root = Tk()
    wid =root.winfo_screenwidth()
    hei = root.winfo_screenheight()
    root.title("Main screen")
    root.geometry(str(wid)+"x"+str(hei))

#sr timer
sr.after(3000,main)


mainloop()