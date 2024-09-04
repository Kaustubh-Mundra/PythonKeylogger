from pynput.mouse import Listener

def logging(x,y):
    print(f'({x},{y})')
    # with open("mouselog.txt","a") as f:
    #     f.write("\n"+f'({x},{y})')

with Listener(on_move=logging) as l:
    l.join()