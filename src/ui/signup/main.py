try:
    from ..tools import BULLET
except:
    from src.ui.tools import BULLET
finally:
    from customtkinter import CTkFrame, CTkLabel, CTk, CTkEntry, CTkFont, CTkButton, DISABLED

class Signup(CTkFrame):
    '''
    Defines the signup page 
    '''

    def __init__(self, parent, **kwargs) -> None:
        super().__init__(parent, ** kwargs)
        self.parent = parent
        self.widgets()
        self.align()
        
    def widgets(self) -> None:
        
        # font
        h1 = CTkFont(family="sans", size=18)
        pcode = CTkFont(family="Helvatica", size=17)
        
        # Labels
        CTkLabel(self, text="\tSignup", font=h1, anchor='center').grid(row=0, column=0, pady=(0, 20))
        CTkLabel(self, text="Username :").grid(row=1, column=0, padx=10, pady=(0,10))
        CTkLabel(self, text="Name :").grid(row=2,column=0, padx=10, pady=(0,10))
        CTkLabel(self, text="Password :").grid( row=3, column=0, padx=10, pady=(0,10))
        self.pass_err = CTkLabel(self,text='test', height=1)

        # Textboxes
        self.capt_uname = CTkEntry(self, placeholder_text="e.g Evans34")
        self.capt_name = CTkEntry(self, placeholder_text="e.g Evans", validatecommand=self.validate, validate="focusout")
        self.capt_password = CTkEntry(self, show=BULLET, validatecommand=self.validate, validate="focusout")

        # Button
        self.submit = CTkButton(self, text="Submit",font=pcode, command=self.button_event, state=DISABLED, height=16)

    def align(self) -> None:

        #Labels
        self.pass_err.grid(row=4,  column=1, padx=10)
        # TextBoxes
        self.capt_uname.grid(row=1, column=1, padx=10, pady=(0,10))
        self.capt_name.grid(row=2,  column=1, padx=10, pady=(0,10))
        self.capt_password.grid(row=3,  column=1, padx=10, pady=(0,10))

        # Button
        self.submit.grid(row=5, column=1)

    def button_event(self): 
        self.submit.configure(text='Submitting...')
        uname,  name, password= self.capt_uname.get(),  self.capt_name.get(), self.capt_password.get()
        logins = uname, name, password
        self.saveCredentials(logins)
        self.parent.overrideredirect(False)
        self.parent.welcome(logins=logins, login='signup')
    
    def validate(self) -> bool:
        check = 0
        name, password= self.capt_name.get(), self.capt_password.get()
        ALPH = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        try:
            if name[0].lower() in ALPH:
                self.capt_name.configure(fg_color=('#424242'))
                self.capt_name.configure(text_color='green')
                check += 1
            else:
                self.capt_name.configure(text_color='red')
                if check >= 1:
                    check -= 1
                else:
                    check += 0
        except IndexError:
            self.capt_name.configure(fg_color='red')
            if check >= 1:
                check -= 1
            else:
                check += 0

        try:
            password[0]
        except IndexError:
            self.pass_err.configure(text='*Required', text_color='red')
            if check >= 1:
                check -= 1
            else:
                check += 0

        else:
            try:
                password[8]
                check += 1
            except IndexError:
                self.pass_err.configure(text='weak', text_color='blue')
                check += 1
            else:
                self.pass_err.configure(text='Good', text_color='green')
                check += 1

        if check == 2:
            self.submit.configure(state='normal')
            return True
        else:
            self.submit.configure(state=DISABLED)
            return False
        
    def saveCredentials(self, data: tuple):
        '''
        Code to save login data to xml
        '''
        from xml.etree.ElementTree import parse

        path = 'data/logins.xml'
        logins = parse(path)
        root = logins.getroot()

        for uname in root.iter('uname'): uname.text = str(data[0])
        for name in root.iter('name'): name.text = str(data[1])
        for password in root.iter('password'): password.text = str(data[2])

        logins.write(path)

    def saveToServer(self):
        '''
        Add code to go to the server and check for duplicates and save, return a value (OK) and enter app
        '''