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

    def events(self):
        '''
        Define event listeners
        '''


if __name__ == '__main__':
    system = Main()
    system.mainloop()