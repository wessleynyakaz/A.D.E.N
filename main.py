try:
    from src.app import Main
except:
    from .src.app import Main
finally:
    import sys

# The welcome phase
if getattr(sys, 'frozen', False):
  import pyi_splash




if __name__ == '__main__':
    system = Main()
    # Close the wecome after loading the app
    if getattr(sys, 'frozen', False):
        pyi_splash.close()
    system.mainloop()
