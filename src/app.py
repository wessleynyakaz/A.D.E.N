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
    REASONABLETIME = 5

class Main(CTk):
    def __init__(self) -> None:
        super().__init__()
        self.geometry("302x302")
        self.title('A.D.E.N')
        self.resizable(False, False)
        self.overrideredirect(True)
        self.iconbitmap('img/icons/icon_inverted.ico')
        self.TRANSPARENT = '#001a33'
        
        # Layout
        img = CTkImage(Image.open('img\\banner\\main.png'), size=(302, 302))
        bg = CTkLabel(self, image=img, text='')
        bg.place(x=0, y=0)

        # Program starting
        self.uname = self.name = self.password = 'non'
        self.startup()
        self.eventListner()

    def checkLastUse(self):
        '''
        Checks for the time elaplicity after first use (in days)
        '''
        # get date
        from xml.etree.ElementTree import parse
        logins = parse('data/time.xml')

        for item in logins.iterfind('time'): storedStart = item.findtext('start')
    
        from datetime import datetime as d
        current = d.now()

        from datetime import date
        end = date(current.year, current.month, current.day)
        _ = tuple(map(int, storedStart.split(', ')))

        start = date(_[0], _[1], _[2])

        result = end - start
        time = result.days
        return time
    
    def checkLogin(self) -> bool:
        '''
        Checks for the availabilty of logins
        '''
        _ : str
        from xml.etree.ElementTree import parse
        logins = parse('data/logins.xml')
        # Extract 
        for item in logins.iterfind('logins'):
            _ = item.findtext('name')
        try:
            _ = _[0]
            if _.lower() in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']: return True
            else: return False
        except IndexError: return False

    def retrieveLogins(self):
        from xml.etree.ElementTree import parse
        logins = parse('data/logins.xml')
        # Extract
        for item in logins.iterfind('logins'):
            self.uname = item.findtext('uname')
            self.name = item.findtext('name')
            self.password = item.findtext('password')

    def startup(self) -> None:
        '''
        Starts the system
        '''
        match self.checkLogin():
            case True: # if logged in
                if self.checkLastUse() >= REASONABLETIME:
                    try:
                        from ui.signin.main import Signin
                    except:
                        try:
                            from .ui.signin.main import Signin
                        except:
                            from src.ui.signin.main import Signin
                    finally:
                        self.signin = Signin(self)
                        self.signin.pack(pady=63)
                        self.signin.pack_propagate(0)

                else:
                    self.retrieveLogins()
                    self.welcome()

            case False:
                try:
                    from ui.signup.main import Signup
                except:
                    try:
                        from .ui.signup.main import Signup
                    except:
                        from src.ui.signup.main import Signup
                finally:
                    self.signup = Signup(self)
                    self.signup.pack(pady=43)

    def welcome(self, logins=tuple(), login='direct') -> None:
        self.HEAD = CTkFont(family='Helvatica', size=16, weight="bold")
        self.BANNNER = CTkFont(family='Sans', size=15, weight='bold')
        if login == 'signup':
            self.signup.destroy()
            self.setTime()
            welc = 'Welcome ' + logins[1].title() + ',  I am Aden'
            CTkLabel(self, text=welc, font=self.HEAD, fg_color=self.TRANSPARENT, corner_radius=12).pack(pady=13)
            CTkLabel(self, text="Thank you for choosing my pre-release.\nI am Comming...Soon", font=self.HEAD,fg_color=self.TRANSPARENT, corner_radius=4).pack(pady=20)
            
        else:
            if login == 'signin':
                self.signin.destroy()
                self.setTime()
            welc = 'Welcome ' + self.name
            CTkLabel(self, text=welc, font=self.HEAD, fg_color=self.TRANSPARENT, corner_radius=12).pack(pady=13)
            CTkLabel(self, text="I am Comming...Soon", font=self.HEAD, fg_color=self.TRANSPARENT, corner_radius=10).pack(pady=20)
        self.after(10000, lambda: self.destroy())
            
    def setTime(self) -> None:
        from datetime import datetime as date
        current = date.now()
        start = str(current.year) + ', ' + str(current.month) + ', ' + str(current.day)
        
        # Write data
        from xml.etree.ElementTree import parse
        path = 'data/time.xml'
        logins = parse(path)
        root = logins.getroot()

        for name in root.iter('start'): name.text = start
        logins.write(path)
        del parse, logins, root, path, start

    def eventListner(self):
        '''
        Define event listeners
        '''

    def display(self):
        '''
        Displays output
        '''