try:
    import Tkinter as tk
    # For python 2
except ImportError:
    import tkinter as tk
    # For python 3

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import gui
    gui.vp_start_gui()




