try:
    from src.app import Main
except:
    from .src.app import Main
    
if __name__ == '__main__':
    system = Main()
    system.mainloop()