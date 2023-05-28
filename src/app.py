'''
Defines the UI and link user, os data to instructions.
Starts, monitor the program.
Decide to bring on the ui or go background
'''

try:
    from ctypes import windll  # Only exists on Windows.
    myappid = "NacFIn.A_D_E_N.ai_assist.version"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass
finally:
    from customtkinter import CTk, CTkLabel,  CTkFont, CTkImage
    from PIL import Image

class Main(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("302x302")
        self.title('A.D.E.N')
        self.resizable(False, False)
        # self.overrideredirect(1)
        self.iconbitmap('img/icons/icon_inverted.ico')
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
