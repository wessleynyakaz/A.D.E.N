try:
    from ..signup.main import Signup
except:
    from src.ui.signup.main import Signup


class Signin(Signup):
    '''
    Defines logging in
    '''