'''
Defines the UI and link user, os data to instructions.
Starts, monitor the program.
Decide to bring on the ui or go background
'''
from customtkinter import CTk


class Main(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("300x300")
        self.title('A.D.E.N')
        self.resizable(False, False)
        self.overrideredirect(True)
        self.startup()

    def checkUse(self):
        '''
        Checks for first time use via an algorithm
        '''
        return True

    def startup(self):
        '''
        Starts the system
        '''
        match self.checkUse():
            case True:
                self.eventListner()
            case False:
                try:
                    from ui.signup import main
                except:
                    from .ui.signup import main
                finally:
                    pass
                del main

    def eventListner(self):
        '''
        Define event listeners
        '''

    def display(self):
        '''
        Displays output
        '''
