from pynput.mouse import Controller
#cannot control the keyboard and the mouse at the same time using the pynput library

#Top-left is considered (0,0)
def controlMouse():
    mouse = Controller()
    mouse.position(500,500)

controlMouse()