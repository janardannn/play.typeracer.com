import pytesseract
import pyautogui as pyg
import os
import time

def get_text():
    ''' Getting text from the image.
        Now the thing is that there are \n 
        in the text which we don't want and 
        a weird character in the end of the 
        text, so we will do some string 
        manipulation as well.
    '''
    os.system('SnippingTool.exe')
    text = pytesseract.image_to_string('Resources/Capture.png')
    text = text[:-2]
    text = " ".join(text.split("\n"))
    
    ''' more refining of text '''

    if '|' in text:
        text = text.replace('|','I')

    elif '1' in text:
        text = text.replace('1','I')

    test_text = text.split()
    i = 0
    while i<len(text):
        
        for k in test_text:
            if k == "{" or k=="}" or k=="|" or k=="(" or k==")":
                test_text.remove(k)
        i+=1

    text = " ".join(test_text)

    ''' finally return the text '''
    return text

def start_typing(text):
    ''' now we will use pyautogui
        module to type the text obtained
        from the image
    '''
    ''' interval is necessary even if 
        it is as low as 0.01, otherwise 
        it will be too fast for the website
        to consider as valid input
    '''
    pyg.write(text,interval=0.0945)

def waiting_period():
    ''' now after capturing the
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

def clean_up():
    os.remove('Resources/Capture.png')

def main(): 

    #k = input('Captured the text? y/n: ').strip()
    k = 'y'
    if k.lower() == 'y':

        text = get_text()
        waiting_period()
        start_typing(text)
        clean_up()
main()
