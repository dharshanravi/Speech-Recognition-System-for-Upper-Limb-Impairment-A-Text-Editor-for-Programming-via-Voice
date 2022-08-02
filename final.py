import speech_recognition as sr
from pywinauto import application
from pynput.keyboard import Key, Controller
import pyautogui as pag
import time
import os
import alphabet

r = sr.Recognizer()
keyboard = Controller() 
app = application.Application()
app.start("Notepad.exe") 

while True:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('Speak now')
        audio_text = r.listen(source,phrase_time_limit = 5)    
        try:    
            text = "# Type your code here!!!"
            text = r.recognize_google(audio_text,language = "en-IN")
            if(text.lower() == 'back' or text.lower() == 'delete'):
                for i in range(0,textlen):
                    keyboard.press(Key.backspace)
                    keyboard.release(Key.backspace)
            elif(text == 'next line'):
                keyboard.press(Key.enter)
                keyboard.release(Key.enter) 
            elif(text == 'select top'):
                keyboard.press(Key.shift)
                keyboard.press(Key.up)
                keyboard.release(Key.up)
                keyboard.release(Key.shift)
            elif(text == 'select bottom'):
                keyboard.press(Key.shift)
                keyboard.press(Key.down)
                keyboard.release(Key.down)
                keyboard.release(Key.shift)
            elif(text == 'select left 5') or (text == 'select left five'):
                keyboard.press(Key.shift)
                for x in range(0,6):
                    keyboard.press(Key.left)
                    keyboard.release(Key.left)
                keyboard.release(Key.shift)
            elif(text == 'select right 5') or (text == 'select right five'):
                keyboard.press(Key.shift)
                for x in range(0,6):
                    keyboard.press(Key.right)
                    keyboard.release(Key.right)
                keyboard.release(Key.shift)
            elif(text == 'select left'):
                keyboard.press(Key.shift)
                keyboard.press(Key.left)
                keyboard.release(Key.left)
                keyboard.release(Key.shift)
            elif(text == 'select right'):
                keyboard.press(Key.shift)
                keyboard.press(Key.right)
                keyboard.release(Key.right)
                keyboard.release(Key.shift)
            elif(text == 'left'):
                keyboard.press(Key.left)
                keyboard.release(Key.left)
            elif(text == 'right'):
                keyboard.press(Key.right)
                keyboard.release(Key.right)
            elif(text == 'top'):
                keyboard.press(Key.up)
                keyboard.release(Key.up)
            elif(text == 'bottom'):
                keyboard.press(Key.down)
                keyboard.release(Key.down)
            elif(text == 'go left'):
                for x in range(0,11):
                    keyboard.press(Key.left)
                    keyboard.release(Key.left)
            elif(text == 'go right'):
                for x in range(0,11):
                    keyboard.press(Key.right)
                    keyboard.release(Key.right)
            elif(text == 'go top'):
                for x in range(0,5):
                    keyboard.press(Key.up)
                    keyboard.release(Key.up)
            elif(text == 'go bottom'):
                for x in range(0,5):
                    keyboard.press(Key.down)
                    keyboard.release(Key.down)
            elif(text == 'control c'):
                keyboard.press(Key.ctrl)
                keyboard.press('c')
                keyboard.release('c')
                keyboard.release(Key.ctrl)
            elif(text.lower() == 'all'):
                keyboard.press(Key.ctrl)
                keyboard.press('a')
                keyboard.release('a')
                keyboard.release(Key.ctrl)
            elif(text == 'control v'):
                keyboard.press(Key.ctrl)
                keyboard.press('v')
                keyboard.release('v')
                keyboard.release(Key.ctrl)
            elif(text == 'tab'):
                pag.write('\t')
            elif(text.lower() == 'addition'):
                keyboard.press('+')
                keyboard.release('+')
            elif(text.lower() == 'subtraction'):
                keyboard.press('-')
                keyboard.release('-')
            elif(text.lower() == 'multiplication'):
                keyboard.press('*')
                keyboard.release('*')
            elif(text.lower() == 'division'):
                keyboard.press('/')
                keyboard.release('/')
            elif(text.lower() == 'mod'):
                keyboard.press('%')
                keyboard.release('%')
            elif(text.lower() == 'equal'):
                pag.write("= ")
            elif(text.lower() == 'equal to'):
                pag.write("== ")
            elif(text.lower() == 'not equal to'):
                pag.write("!= ")
            elif(text.lower() == 'and'):
                pag.write("and")
            elif(text.lower() == 'or'):
                pag.write("or")
            elif(text.lower() == 'circumflex'):
                pag.write("^")
            elif(text.lower() == 'close tag'):
                pag.write(">")
            elif(text.lower() == 'open tag'):
                pag.write("<")
            elif(text.lower() == 'punctuation colon'):
                pag.write(':')
            elif(text.lower() == 'semicolon'):
                pag.write(";")
            elif(text.lower() == 'interval'):
                pag.write(",")
            elif(text.lower() == 'quotation'):
                pag.write("''")
                for i in range(3):
                    keyboard.press(Key.left)
                    keyboard.release(Key.left)
            elif(text.lower() == 'quotation 1'):
                pag.write('""')
                for i in range(3):
                    keyboard.press(Key.left)
                    keyboard.release(Key.left)
            elif(text.lower() == 'underscore'):
                pag.write('_')
            elif(text.lower() == 'open bracket'):
                pag.write("(")
                pag.write(")")
                keyboard.press(Key.left)
                keyboard.release(Key.left)
            elif(text.lower() == 'curly bracket'):
                pag.write("{")
                pag.write("}")
                keyboard.press(Key.left)
                keyboard.release(Key.left)
            elif(text.lower() == 'box bracket'):
                pag.write("[")
                pag.write("]")
                keyboard.press(Key.left)
                keyboard.release(Key.left)
            elif(text.lower() == 'space'):
                pag.write(" ")
            elif(text.lower() == 'conditional statement'):
                pag.write("if :\n\nelse :")
                keyboard.press(Key.up)
                keyboard.release(Key.up)
                keyboard.press(Key.up)
                keyboard.release(Key.up)
                for i in range(3):
                    keyboard.press(Key.right)
                    keyboard.release(Key.right)
            elif(text.lower() == 'conditional statement 1'):
                pag.write("elif :")
            elif(text.lower() == 'looping statement'):
                pag.write("for :")
                keyboard.press(Key.left)
                keyboard.release(Key.left)
            elif( text.lower() == 'looping statement 1' or text.lower() =='looping statement one'):
                pag.write("for i in range():")
                keyboard.press(Key.left)
                keyboard.release(Key.left)
                keyboard.press(Key.left)
                keyboard.release(Key.left)
            elif(text.lower() == 'looping statement 2' or text.lower() =='looping statement tu' or text.lower() =='looping statement to'):
                pag.write("while :")
                keyboard.press(Key.left)
                keyboard.release(Key.left)
            elif(text == 'function'):
                pag.write("def :")
                keyboard.press(Key.left)
                keyboard.release(Key.left)
            elif(text == 'function 1'):
                pag.write("def (self):")
                for i in range(7):
                    keyboard.press(Key.left)
                    keyboard.release(Key.left)
            elif(text.lower() == 'constructor'):
                pag.write("def __init__(self):")
                keyboard.press(Key.left)
                keyboard.release(Key.left)
                keyboard.press(Key.left)
                keyboard.release(Key.left)
            elif(text == 'cut'):
                keyboard.press(Key.ctrl)
                keyboard.press('x')
                keyboard.release('x')
                keyboard.release(Key.ctrl)
            elif(text == 'backspace'):
                keyboard.press(Key.backspace)
                keyboard.release(Key.backspace)
            elif(text == 'backspace 5') or (text == 'backspace five'):
                for x in range(0,6):
                    keyboard.press(Key.backspace)
                    keyboard.release(Key.backspace)
            elif(text == 'backspace 10') or (text == 'backspace ten'):
                for x in range(0,11):
                    keyboard.press(Key.backspace)
                    keyboard.release(Key.backspace)
            elif(text.split()[0] == 'backspace'):
                for x in range(0,int(text.split()[1])):
                    keyboard.press(Key.backspace)
                    keyboard.release(Key.backspace)
            elif(text == 'undo'):
                keyboard.press(Key.ctrl)
                keyboard.press('z')
                keyboard.release('z')
                keyboard.release(Key.ctrl)
            elif(text.lower() == 'save the program'):
                app.Notepad.menu_select("File ->SaveAs")
                print("say name")
                audio_1=r.listen(source,phrase_time_limit = 5)
                text_1=r.recognize_google(audio_1,language = "en-IN")
                app.SaveAs.edit.set_edit_text(text_1+".txt")
                app.SaveAs.Save.click()
            elif(text == 'open'):
                app.Notepad.menu_select("File ->Open")
                print("say name")
                audio_1=r.listen(source,phrase_time_limit = 5)
                text_1=r.recognize_google(audio_1,language = "en-IN")
                app.Open.edit.set_edit_text(text_1+".txt")
                app.Open.Open.click()
            elif(text == 'intensify '):
                app.Notepad.menu_select("Format ->Font")
                app.Font.edit.set_edit_text("Cooper")
                app.Font.OK.click()
            elif(text == 'exit'):
                app.Notepad.menu_select("File ->Exit")
                keyboard.press(Key.alt)
                keyboard.press('n')
                keyboard.release('n')
                keyboard.release(Key.alt)
                break
            elif(text.lower() == 'execute'):
                os.system("start cmd")
                time.sleep(0.5)
                pag.write('rename ' + text_1 + '.txt ' + text_1 + '.py')
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                time.sleep(1)
                pag.write('python ' + text_1 + ".py")
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
            elif(text == 'close'):
                pag.write('exit')
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
            elif(text.split()[0].lower() == 'number'):
                text = text.split()[1]
                pag.write(text + " ")
            elif(text.lower() == 'print'):
                text = text + '()'
                pag.write(text)
                keyboard.press(Key.left)
                keyboard.release(Key.left)
            elif(text.split()[0].lower() == 'change'):
                temp = text.split()[1]
                if(temp == '1' or temp == 'one'):
                    text = 'int()'
                elif(temp == '3' or temp == 'three'):
                    text = 'str()'
                else:
                    text = 'float()'
                pag.write(text)
                keyboard.press(Key.left)
                keyboard.release(Key.left)
            elif(text.lower() == 'user input'):
                text = 'input()'
                pag.write(text)
            elif(text != "stop"):
                if(text.split()[0] == 'print'):
                    res = list(text)
                    res.insert(5, '(\"')
                    res = ''.join(res)
                    res += '\")'
                    text = res
                    text = text.replace(' ', '', 1)
                elif(text.split()[0].lower() == 'on'):
                    text = text.split()[1]
                elif(text.split()[0].lower() == 'character'):
                    alpha=text.split()[1]
                    if alpha.lower() == 'tu' or alpha.lower() == 'to':
                        alpha = '2'
                    text=alphabet.return_alphabet(int(alpha))
                pag.write(text + " ")
            else:
                print("<*Stopped*>")
                break
        except:
            print('Not recognized')
        if(text != "# Type your code here!!!"):
            textlen = len(text)+1    