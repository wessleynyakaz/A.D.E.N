try:
    from src.app import Main
except:
    from .src.app import Main
    
def banner():
    from tkinter import Tk, Label
    from PIL import ImageTk, Image
    banner = Tk()
    banner.geometry("753x753")
    banner.overrideredirect(1)
    bg = Image.open('img\\banner\\main.png')
    bg = ImageTk.PhotoImage(bg)
    label1 = Label(banner, image=bg)
    label1.place(x=0, y=0)
    from time import sleep
    sleep(5)
    banner.destroy()
    banner.mainloop()

if __name__ == '__main__':
    banner()
    system = Main()
    system.mainloop()