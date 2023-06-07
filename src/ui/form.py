'''
A  form to capture user's  conditions and preferences
'''
from customtkinter import CTkFrame, CTkLabel, CTkEntry, CTkFont, CTkButton, DISABLED

class Form(CTkFrame):
    def __init__(self, parent, caller='optional'):
        super().__init__(parent)
        caller.destroy()
        