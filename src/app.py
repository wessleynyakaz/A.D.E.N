'''
Defines the UI and link user, os data to instructions.
Starts, monitor the program.
Decide to bring on the ui or go background
'''
from customtkinter import CTk, CTkLabel, TOP, BOTH, CTkFont, CTkImage
from PIL import Image, ImageTk


class Main(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("302x302")
        self.title('A.D.E.N')
        self.resizable(False, False)
        self.overrideredirect(1)
        # self.attributes("-alpha", 0) disappear
        bg = CTkImage(Image.open('img\\banner\\main.png'), size=(302, 302))
        bg = CTkLabel(self, image=bg, text='')
        bg.place(x=0, y=0)
        self.startup()


    def checkUse(self):
        '''
        Checks for first time use via an algorithm
        '''
        return False

    def startup(self):
        '''
        Starts the system
        '''
        match self.checkUse():
            case True:
                self.eventListner()
            case False:
                try:
                    from ui.signup.main import Signup
                except:
                    from .ui.signup.main import Signup
                finally:
                    head = CTkFont(family='Helvatica', size=16, weight="bold")
                    CTkLabel(self, text=" Welcome, i am A.D.E.N",  font=head).pack(pady=13)
                    x = Signup(self)
                    x.pack()

                    
                del Signup

    def eventListner(self):
        '''
        Define event listeners
        '''

    def display(self):
        '''
        Displays output
        '''
