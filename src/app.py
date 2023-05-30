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
        
        # Layout
        img = CTkImage(Image.open('img\\banner\\main.png'), size=(302, 302))
        bg = CTkLabel(self, image=img, text='')
        bg.place(x=0, y=0)
        # self.attributes("-alpha", 0) disappear

        # Program starting
        self.name = self.lname = self.password = 'non'
        self.startup()

    def checkUse(self):
        '''
        Checks for first time use via an algorithm
        '''
        from xml.etree.ElementTree import parse
        logins = parse('data/logins.xml')
        # Extract 
        for item in logins.iterfind('logins'):
            self.name = item.findtext('name')

        if item[0] in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
            del parse
            return True
        else:
            del parse
            return False

    def startup(self):
        '''
        Starts the system
        '''
        match self.checkUse():
            case True:
                self.retrieveLogins()
                self.welcome(login='signin')
                self.eventListner()
            case False:
                try:
                    from ui.signup.main import Signup
                except:
                    from .ui.signup.main import Signup
                finally:
                    self.signup = Signup(self)
                    self.signup.pack(pady=43)

    def welcome(self, logins=tuple(), login='signin'):
        self.HEAD = CTkFont(family='Helvatica', size=16, weight="bold")
        if login == 'signin':
            welc = 'Welcome ' + self.name
            CTkLabel(self, text=welc, font=self.HEAD).pack(pady=13)
        else:
            self.signup.destroy()
            welc = 'Welcome ' + logins[0].title() + ' I am Aden'
            CTkLabel(self, text=welc, font=self.HEAD).pack(pady=13)

    def retrieveLogins(self):
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
