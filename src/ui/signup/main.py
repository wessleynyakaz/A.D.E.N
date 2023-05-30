try:
    from customtkinter import CTkFrame, CTkLabel, CTk, CTkEntry, CTkFont, CTkButton, StringVar
    from ..tools import BULLET
except:
    from src.ui.tools import BULLET

class Signup(CTkFrame):
    '''
    Defines the signup page 
    '''

    def __init__(self, parent, **kwargs):
        super().__init__(parent,  **kwargs)
        self.parent = parent
        self.widgets()
        self.align()
        

    def widgets(self):
        
        # font
        h1 = CTkFont(family="sans", size=18)
        pcode = CTkFont(family="Helvatica", size=17)
        
        # Labels
        CTkLabel(self, text="\tSignup", font=h1, anchor='center').grid(row=0, column=1, pady=3)
        CTkLabel(self, text="Name :").grid(row=1, column=1, padx=6, pady=12)
        CTkLabel(self, text="Last Name :").grid(row=2, column=1, padx=10, pady=12)
        CTkLabel(self, text="Password :").grid( row=3, column=1, padx=10, pady=12)

        # Textboxes
        self.capt_fname = CTkEntry(self, placeholder_text="e.g Micheal", )
        self.capt_lname = CTkEntry(self, placeholder_text="e.g Evans")
        self.capt_password = CTkEntry(self,show=BULLET)

        # Button
        self.submit = CTkButton(self, text="Submit",font=pcode, command=self.button_event)

    def align(self):

        # TextBoxes
        self.capt_fname.grid(row=1, column=2)
        self.capt_lname.grid(row=2, column=2)
        self.capt_password.grid(row=3, column=2)

        # Button
        self.submit.grid(row=5, column=2)

    def button_event(self):
        '''
        Add code to go to the server and check for duplicates and save, return a value (OK) and enter app
        '''
        self.parent.overrideredirect(False)
        name,  lname, password= self.capt_fname.get(),  self.capt_lname.get(), self.capt_password.get()
        logins = name, lname, password
        self.saveCredentials(logins)

        #debugging
        print('Contents :' , logins)
        print('\nType (whole) :', type(logins))
        x = str(logins[0])
        print('\nType (part) :',x)

        self.parent.welcome(logins=logins, login='signup')

    def saveCredentials(self, logins: tuple):
        '''
        Code to save login data to xml
        '''


if __name__ == '__main__':
    app = CTk()
    page = Signup(parent=app)
    page.pack()
    app.mainloop()