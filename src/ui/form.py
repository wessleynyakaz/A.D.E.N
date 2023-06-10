'''
A  form to capture user's  conditions and preferences
'''
from customtkinter import CTkFrame, CTkLabel, CTkEntry, CTkFont, CTkButton, DISABLED, CTk, CTkRadioButton, CTkTextbox, CTkCheckBox
from customtkinter import StringVar


class Form(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color='transparent')
        self.parent = parent
        self.parent.iconbitmap('res\img\icons\icon_inverted.ico')
        self.parent.title('Preferences')
        self.variables()
        self.widgets()
        self.align()

    def widgets(self):
        # Fonts
        HEADER = CTkFont(self, size=20, weight='bold')
        
        # Labels
        self.nm = CTkLabel(self,text='Full Name :', font=HEADER)
        self.shrt = CTkLabel(self,text='Short Comings :', font=HEADER)
        
        # Textboxes
        self.capt_name = CTkEntry(self, width=200)

        # CheckBoxes
        self.hearing = CTkCheckBox(self, text='hearing', variable=self.hearing_variable)
        self.visual = CTkCheckBox(self, text='Visual', variable=self.visual_variable)
        self.other = CTkCheckBox(self, text='Other', variable=self.other_variable)

        # Buttons
        self.submit = CTkButton(self, text='Finish Up', command=self.finish())
    
    def align(self):
        # Labels
        self.nm.grid(row=0, column=0, sticky='nswe')
        self.shrt.grid(row = 1, column = 0, pady=9, sticky='nswe')
        
        # Textboxes
        self.capt_name.grid(row=0, column=1, sticky='nswe')
        
        # CheckBoxes 
        self.hearing.grid(row=1, column=1, padx=8, sticky='nswe')
        self.visual.grid(row=2, column=1, padx=8, sticky='nswe')
        self.other.grid(row=3, column=1, pady=9, padx=8, sticky='nswe')

        # Buttons
        self.submit.grid()

    def variables(self):
        self.hearing_variable = self.visual_variable = self.other_variable = StringVar()

    def finish(self):...

    def extract_name(self):...

    def save(self):...


if __name__ == '__main__':
    _ = CTk()
    _.geometry('500x500')
    Form(_).grid()
    _.mainloop()