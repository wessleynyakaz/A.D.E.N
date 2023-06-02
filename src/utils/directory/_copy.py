'''
Copies files 
'''
from _setPath import FROM, TO
from shutil import copy, copytree
from os.path import exists

def Available(file):
    '''
    Checks whether a file or folder exist
    '''

def check(file):
    '''
    Checks whether a file or folder has been passed in
    '''
    return 'file'

def change(file: str):
    '''
    Changes the file name
    '''
    pos = file.find('.txt')
    name = file[:pos]
    output = name + str(1)
    output += file[4::]
    return output

def copyFile(file: str, times: int):
    for i in range(times): # defin incrementation for files fil1 
        if exists(TO + '/' + file):
            copy(file, (TO + '/' + change(file)))
        else:
            copy(file, (TO + '/'))     
def copyFolder(folder: str, times: int):...

def main(file: str, times: int):
    TYPE = check(file)
    if TYPE == 'file':
        status = copyFile(file, times)
    else:
        status = copyFolder(file, times)
    match status:
        case 0:
            return 'success'
        case 1:
            return 'failed'
        case 2:
            return 'destination can\'t be accessed'

if __name__ == '__main__':
    # fil = input('Enter file: ')
    print('<<Copying>> : '+ 'test.txt ' + f'{10} times')
    print(main(file='test.txt', times=10))