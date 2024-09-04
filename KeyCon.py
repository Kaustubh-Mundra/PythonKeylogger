from pynput.keyboard import Controller

def controlKeyboard():
    keyboard = Controller()
    keyboard.type("Hi")
#the sentence will be types wherever the curson is at present

controlKeyboard()