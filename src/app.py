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
        self.overrideredirect(1)
        self.iconbitmap('img/icons/icon_inverted.ico')
        # self.attributes("-alpha", 0) disappear
        bg = CTkImage(Image.open('img\\banner\\main.png'), size=(302, 302))
        bg = CTkLabel(self, image=bg, text='')
        bg.place(x=0, y=0)
        self.HEAD = CTkFont(family='Helvatica', size=16, weight="bold")
        self.name = self.lname = self.password = ''
        self.startup()

    def welcome(self):
        welc = 'Welcome ' + self.name + ', i am A.D.E.N'
        CTkLabel(self, text=welc,font=self.HEAD).pack(pady=13)

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
                self.welcome()
                self.eventListner()
            case False:
                try:
                    from ui.signup.main import Signup
                except:
                    from .ui.signup.main import Signup
                finally:
                    _ =  CTkLabel(self, text=" Welcome, i am A.D.E.N",  font=self.HEAD)
                    _.pack(pady=13)
                    x = Signup(self)
                    x.pack()
                    self.logins = x.credentials()
                    if self.logins:
                        _.destroy()
                        self.welcome()
                del Signup

    def retrieveData(self):
        from xml.etree.ElementTree import parse
        logins = parse('data/logins.xml')
        # Extract 
        for item in logins.iterfind('logins'):
            self.name = item.findtext('name')
            self.lname = item.findtext('lname')
            self.password = item.findtext('password')


    def eventListner(self):
        '''
        Define event listeners
        '''

    def display(self):
        '''
        Displays output
        '''
