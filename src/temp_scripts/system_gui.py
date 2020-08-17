# TODO - update to minimize imports
from tkinter import *
from tkinter.ttk import *

# TODO - move to external strings file
TITLE = "System: Blink"
DESCR = "The system that blinks with a frequency proportional to regulatory bits and shocks received by system. Press the 'Start' button. "
HOST = "Host: localhost"
PORT = "Port: 3843"

class BlinkGUI:
    def __init__(self, master):
        self.master = master
        master.title(TITLE)

        self.blink_canvas = Canvas(self.master)
        self.graph_canvas = Canvas(self.master)

        # Text / Labels
        descTxt = StringVar(value=DESCR)
        self.desc_entry = Entry(self.master, textvariable=descTxt, state="readonly")
        self.scroll = Scrollbar(self.master, orient="vertical", command=self.desc_entry.xview)
        self.desc_entry.config(xscrollcommand=self.scroll.set)
        # self.title_label = Label(self.master, text=TITLE)
        # self.descr_label = Label(self.master, text=DESCR)
        self.host_label = Label(self.master, text=HOST)
        self.port_label = Label(self.master, text=PORT)
        
        # Control buttons
        self.start_button = Button(self.master, text="Start", command=self.start)
        self.stop_button = Button(self.master, text="Stop", command=self.stop)
        self.increase_button = Button(self.master, text="Increase")
        self.decrease_button = Button(self.master, text="Decrease")
        self.shock_button = Button(self.master, text="Shock")
        
        # Layout - top bar
        # self.title_label.grid(row=0, sticky="w")
        self.desc_entry.grid(row=1, sticky="w")

        self.host_label.grid(row=0, column=2, sticky="w")
        self.port_label.grid(row=1, column=2, sticky="w")

        self.blink_canvas.grid(row=1, column=3, sticky="e")

        # # Layout - left bar
        # self.receiving_label.grid(row=2)
        # self.frequency_label.grid(row=2)

        # # Layout - middle canvas
        # self.canvas.grid(row=1, sticky="nsew")

        # # Layout - bottom bar
        # self.start_button.grid(row=3, column=0)
        # self.stop_button.grid(row=3, column=1)
        # self.increase_button.grid(row=3, column=1)
        # self.decrease_button.grid(row=3, column=1)
        # self.shock_button.grid(row=3, column=1)
        

    def start(self):
        print("STARTING")
    
    def stop(self):
        print("STOPPING")

root = Tk()
my_gui = BlinkGUI(root)
root.columnconfigure([0,1,2,3], weight=1)
root.rowconfigure([0,1,2,3], weight=1)
root.mainloop()
