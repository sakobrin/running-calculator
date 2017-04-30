from tkinter import *
from tkinter import ttk

main = Tk()

content = ttk.Frame(main)
main.title('Running Calculator')
frame = ttk.Frame(content, borderwidth=5, relief="sunken", width = 500, height = 300)

timelbl = ttk.Label(content, text = "Time")
time = ttk.Entry(content)

distancelbl = ttk.Label(content, text = "Distance")
distance = ttk.Entry(content)

pacelbl = ttk.Label(content, text = "Pace")
pace = ttk.Entry(content)

viewSplits = BooleanVar()
viewSplits.set(False)
splits = ttk.Checkbutton(content, text="View Splits?", variable = viewSplits, onvalue= True)

content.grid(column = 0, row = 0)
frame.grid(column = 0, row = 0, columnspan = 1, rowspan = 9)

timelbl.grid(column = 0, row = 0, columnspan = 1)
time.grid(column = 0, row = 1, columnspan = 1)

distancelbl.grid(column = 0, row = 3, columnspan = 1)
distance.grid(column = 0, row = 4, columnspan = 1)

pacelbl.grid(column = 0, row = 6, columnspan = 1)
pace.grid(column = 0, row = 7, columnspan = 1)

splits.grid(column = 0, row = 9)

main.mainloop()