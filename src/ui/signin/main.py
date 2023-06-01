try:
    from ..tools import BULLET
except:
    from src.ui.tools import BULLET
finally:
    from customtkinter import CTkFrame, CTkLabel, CTk, CTkEntry, CTkFont, CTkButton, DISABLED


class Signin(CTkFrame):
    '''
    Defines logging in
    '''
    def __init__(self, parent, **kwargs ):
        super().__init__(parent, ** kwargs)
        self.parent = parent
        self.widgets()
        self.align()

    def widgets(self) -> None:
        
        # font
        h1 = CTkFont(family="sans", size=18)
        pcode = CTkFont(family="Helvatica", size=17)
        
        # Labels
        CTkLabel(self, text="\tLogin", font=h1, anchor='center').grid(row=0, column=1, pady=3)
        CTkLabel(self, text="Username :").grid(row=1, column=1, padx=6, pady=12)
        CTkLabel(self, text="Password :").grid( row=2, column=1, padx=10, pady=12)

        # Textboxes
        self.capt_uname = CTkEntry(self, validatecommand=self.realtimeValidate, validate="focusout")
        self.capt_password = CTkEntry(self, show=BULLET, validatecommand=self.realtimeValidate, validate="focusout")

        # Button
        self.submit = CTkButton(self, text="Login",font=pcode, command=self.button_event, state=DISABLED)
    
    def align(self) -> None:

        # TextBoxes
        self.capt_uname.grid(row=1, column=2)
        self.capt_password.grid(row=2, column=2)

        # Button
        self.submit.grid(row=3, column=2)

    def button_event(self) -> None:
        self.submit.configure(text='Logging in...')
        uname, password = self.capt_uname.get(), self.capt_password.get()
        if self.finalValidate(uname, password):
            self.parent.overrideredirect(False)
            self.parent.welcome(login='signin')
        else:
            self.submit.configure(text='Invalid Details')

    def realtimeValidate(self) -> None:
        check = 0 
        # get the password
        uname, password = self.capt_uname.get(), self.capt_password.get()
        
        # check if empty
        self.capt_uname.configure(text_color='white' if uname else 'red')
        self.capt_password.configure(text_color='white' if password else 'red')

        # results
        check += 1 if self.capt_uname.cget('text_color') == 'white' else 0
        check += 1 if self.capt_uname.cget('text_color') == 'white' else 0

        if check == 2:
            self.submit.configure(state='normal')
        else:
            self.submit.configure(state=DISABLED)
    def finalValidate(self, uname, password) -> bool:
        self.parent.retrieveLogins()
        if  (uname == self.parent.name) and (password == self.parent.password):
            return True
        else:
            return False
    def getCredintials(self):...

    def saveToServer(self):...
