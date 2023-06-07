'''
Defines the UI and link user, os data to instructions.
Starts, monitor the program.
Decide to bring on the ui or go background
'''
try:
    from ctypes import windll  # Only exists on Windows.
    myappid = "NacFIn.A_D_E_N.ai_assist.version"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError: pass
finally:
    from customtkinter import CTk
    REASONABLETIME = 5

class Main(CTk):
    def __init__(self) -> None:
        super().__init__()
        self.geometry("302x302")
        self.overrideredirect(True)
        self.disappear = lambda: self.attributes('-alpha', 0)
        self.appear = lambda: self.attributes('-alpha', 100)

        # Program starting
        self.uname = self.name = self.password = str
        self.startup()
        self.service_mode()

    def check_last_use(self) -> int:
        '''
        Checks for the time elaplicity after first use (in days)
        '''
        # get date
        from xml.etree.ElementTree import parse
        logins = parse('data/time.xml')
        root = logins.getroot()

        try:
            for item in logins.iterfind('time'): storedStart = item.findtext('then')
            _ = tuple(map(int, storedStart.split(', ')))
        except ValueError:
            return 0
        
        then = date(_[0], _[1], _[2])
        
        from datetime import datetime as d
        current = d.now()

        from datetime import date
        now = date(current.year, current.month, current.day)
        
        result = now - then
        time = result.days
        return time
    
    def check_login(self) -> bool:
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

    def retrieve_logins(self) -> None:
        from xml.etree.ElementTree import parse
        logins = parse('data/logins.xml')
        # Extract
        for item in logins.iterfind('logins'):
            self.uname = item.findtext('uname')
            self.name = item.findtext('name')
            self.password = item.findtext('password')
   
    def retrieve_personal_inf(self) -> None:...
   
    def set_time(self) -> None:
        from datetime import datetime as date
        current = date.now()
        now = str(current.year) + ', ' + \
            str(current.month) + ', ' + str(current.day)

        # Write data
        from xml.etree.ElementTree import parse
        path = 'data/time.xml'
        time = parse(path)
        root = time.getroot()

        for name in root.iter('then'):
            name.text = now
        time.write(path)
        del parse, time, root, path, now

    def startup(self) -> None:
        '''
        Starts the system
        '''
        match self.check_login(): # validation protocol
            case True: # if logged in
                if self.check_last_use() > REASONABLETIME:
                    try: from ui.signin import Signin
                    except:
                        try: from .ui.signin import Signin
                        except: from src.ui.signin import Signin
                    finally:
                        self.signin = Signin(self)
                        self.signin.pack(pady=63)
                        self.signin.pack_propagate(0)

                else:
                    self.retrieve_logins()
                    self.welcome('direct')

            case False:
                try:
                    from ui.signup import Signup
                except:
                    try:
                        from .ui.signup import Signup
                    except:
                        from src.ui.signup import Signup
                finally:
                    self.signup = Signup(self)
                    self.signup.pack(pady=43)

    def welcome(self, login) -> None:
        '''
        Welcomes the user.
        Decides to use either Audio or Visual depending on users' conditions
        And disappears the window
        '''  
        self.disappear()
        try:
            from ui.audio import speak
        except:
            try:
                from .ui.audio import speak
            except:
                from src.ui.audio import speak
        finally:
            match login:
                case 'direct':
                    speak(f'How are you {self.name}?')
                case 'signin':
                    speak(f'How have you been {self.name}?')
                case 'signup':
                    speak(f'Welcome {self.name}, i am Aden.')
        del speak
    def event_listener(self):
        '''
        Listens for commands from user
        '''
        SEARCH = {'look', 'find', 'search'}
        OPEN = {'open', }
        PLAY = {'play'}
        command : str
        if (command in SEARCH): pass
        elif ( command in OPEN): pass
        elif (command in PLAY): pass
        else: self.display('fail')


    def service_mode(self, service = 'optional'):
        '''
        Starts the service, and await for input
        '''

    def display(self, task): 
        '''
        Displays results from given tasks
        '''
        self.appear()