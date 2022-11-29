import tkinter as tk
from gui import create_button_frame

def create_main_window():

    # root window
    root = tk.Tk()
    root.title('NomadSport')
    root.geometry('1000x620')
    root.resizable(0, 0)

    # layout on the root window
    root.columnconfigure(0, weight=1)

    button_frame = create_button_frame(root)
    button_frame.grid(column=0, row=0, sticky='w')

    root.mainloop()


if __name__ == "__main__":
    create_main_window()
