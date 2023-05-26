from customtkinter import CTkFrame, CTkLabel, CTk, CTkEntry, CTkFont

class Signup(CTkFrame):
    '''
    Defines the signup page 
    '''
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.widgets()
        self.align()
      

    def widgets(self):
        # font
        h1 = CTkFont(family="sans", size=18)
        # Labels
        self.header = CTkLabel(self, text=" Signup", font=h1)
        self.fname = CTkLabel(self, text="Name :")
        self.lname = CTkLabel(self,text="Last Name :")
        self.password = CTkLabel(self,text="Password :")

        # Textboxes
        self.capt_fname = CTkEntry(self, placeholder_text="e.g Micheal")
        self.capt_lname = CTkEntry(self, placeholder_text="e.g Evans")
        self.capt_password = CTkEntry(self,)

    def align(self):

        # Labels
        self.header.grid(row=0, column=2, pady=14)
        self.fname.grid(row=1, column=1, padx=6, pady=14)
        self.lname.grid(row=2, column=1, padx=10, pady=12)
        self.password.grid(row=3, column=1, padx=10, pady=12)

        # TextBoxes
        self.capt_fname.grid(row=1, column=3)
        self.capt_lname.grid(row=2, column=3)
        self.capt_password.grid(row=3, column=3)


if __name__ == '__main__':
    app = CTk()
    page = Signup(parent=app)
    page.pack()
    app.mainloop()