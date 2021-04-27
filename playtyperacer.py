import pytesseract
import pyautogui as pyg
import os
import time

def get_text():
    ''' getting the text from the image
        now the thing is that there are \n 
        in the text which we do not need also 
        a weird character in the text, so we
        will do some string manipulation
    '''
    os.system('SnippingTool.exe')
    text = pytesseract.image_to_string('Resources/Capture.png')
    text = text[:-2]
    text = " ".join(text.split("\n"))
    ''' more refining of text '''

    test_text = text.split()
    for k in test_text:
        if k == "{" or k=="}" or k=="|":
            test_text.remove(k)
    text = " ".join(test_text)

    ''' finally return the text '''
    return text

def start_typing(text):
    ''' now we will use the pyautogui
        module to type the text obtained
        from the image
    '''

    pyg.write(text,interval=0.0215)

def waiting_period():
    ''' now from after capturing the
        screenshot the program will 
        start typing it automatically which
        we don't want as the browser window
        may be out of focus, so we will
        add some waiting period for the 
        program and in the mean time we will
        re focus on the browser
    '''
    os.system('cls')
    for k in [3,2,1]:
        print(k)
        time.sleep(1.5)
        os.system('cls')

def clean_up(key=0):
    k = key
    if k == 1:
        os.remove('Resources/Capture.png') 
    else:
        pass

def main(): 

    #k = input('Captured the text? y/n: ').strip()
    k = 'y'
    if k.lower() == 'y':

        text = get_text()
        waiting_period()
        start_typing(text)
        clean_up(1)
main()
