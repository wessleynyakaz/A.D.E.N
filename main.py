try: from src.engine import Main
except: from .src.engine import Main
finally:
    import sys
    if __name__ == '__main__':
        if getattr(sys, 'frozen', False): import pyi_splash
        system = Main()
        # Close the wecome after loading the app
        if getattr(sys, 'frozen', False): pyi_splash.close()
        system.mainloop()