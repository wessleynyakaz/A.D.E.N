'''
A template to display or  specific data(information passed in)
'''
from customtkinter import CTkFrame, CTkButton

class Stats(CTkFrame):
    '''
    Displays(not edit but will) statistical data from a source
    '''
    def __init__(self, parent,data= None, fg_color='transparent'):
        super().__init__(parent, fg_color=fg_color)
        self.parent = parent
        self.parent.overrideredirect(False)
        self.parent.iconbitmap('res\img\icons\icon_normal.ico')
        self.parent.title('Results')
        self.widgets()
        self.align()

    def widgets(self) -> None:
        CTkButton(self, text='SAVE').grid(row=0, column=0, pady=5)
        self.stat_display = CTkFrame(self, fg_color='green', height=3000, width=320)

    def align(self) -> None:
        self.stat_display.grid(row=1, column=0, padx=5)

class Normal(CTkFrame):
    def __init__(self, data):
        super().__init__(self)
        self.widgets()

    def wigets() -> None:
        '''
        Defines statistical models i.e graphs
        '''

    def align() -> None: ...

if __name__ == '__main__':
    from customtkinter import CTk
    root = CTk()
    root.overrideredirect(1)
    root.geometry('800x800')
    Stats(root).grid()
    root.mainloop()