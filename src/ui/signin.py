try:
    from .tools import BULLET
except:
    from src.ui.tools import BULLET
finally:
    from customtkinter import CTkFrame, CTkLabel, CTkEntry, CTkFont, CTkButton, DISABLED

class Signin(CTkFrame):
    def __init__(self, parent, fg_color='transparent', **kwargs ):
        super().__init__(parent, fg_color=fg_color, ** kwargs)
        self.parent = parent
        self.widgets()
        self.align()

    def widgets(self) -> None:
        
        # font
        h1 = CTkFont(family="sans", size=18)
        pcode = CTkFont(family="Helvatica", size=17)
        
        # Labels
        CTkLabel(self, text="\tLogin", font=h1).grid(row=0, column=0, pady=(0, 20))
        CTkLabel(self, text="Username :").grid(row=1, column=0, padx=10, pady=(0,10))
        CTkLabel(self, text="Password :").grid( row=2, column=0, padx=10, pady=(0,10))

        # Textboxes
        self.capt_uname = CTkEntry(self, validatecommand=self.realtime_validate, validate="focusout")
        self.capt_password = CTkEntry(self, show=BULLET, validatecommand=self.realtime_validate, validate="focusout")

        # Button
        self.submit_btn = CTkButton(self, text="Login",font=pcode, command=self.button_event, state=DISABLED)
        self.exit_btn = CTkButton(self, text='EXIT', command=lambda: self.parent.destroy())

    
    def align(self) -> None:

        # TextBoxes
        self.capt_uname.grid(row=1, column=1, padx=10, pady=(0, 10))
        self.capt_password.grid(row=2, column=1, padx=10, pady=(0, 10))

        # Button
        self.submit_btn.grid(row=3, column=1, pady=(0, 20))
        self.exit_btn.grid(row=3,column=0, padx=10, pady=(0,20))

    def button_event(self) -> None:
        self.submit_btn.configure(text='Logging in...')
        uname, password = self.capt_uname.get(), self.capt_password.get()
        if self.final_validate(uname, password): self.parent.welcome(login='signin')
        else: self.submit_btn.configure(text='Invalid Details')

    def realtime_validate(self) -> None:
        check = 0 
        # get the password
        uname, password = self.capt_uname.get(), self.capt_password.get()
        
        # check if empty
        self.capt_uname.configure(text_color='white' if uname else 'red')
        self.capt_password.configure(text_color='white' if password else 'red')

        # results
        check += 1 if self.capt_uname.cget('text_color') == 'white' else 0
        check += 1 if self.capt_uname.cget('text_color') == 'white' else 0

        if check == 2: self.submit_btn.configure(state='normal')
        else: self.submit_btn.configure(state=DISABLED)

    def final_validate(self, uname, password) -> bool:
        self.parent.retrieve_logins()
        if  (uname == self.parent.uname) and (password == self.parent.password): return True
        else: return False
        
    def get_credintials(self):...

    def save_to_Server(self):...