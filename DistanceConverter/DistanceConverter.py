import tkinter as tk
from tkinter import ttk
#from windows import set_dpi_awareness

try:
    from ctypes  import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

#set_dpi_awareness()

class DistanceConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Distance Converter")
        self.frame = MetersToFeet(self, padding=(60,30))
        self.frame.grid()

        self.bind("<Return>", self.frame.calculate_feet)
        self.bind("<KP_Enter>", self.frame.calculate_feet)

class MetersToFeet(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        self.feet_value = tk.StringVar()
        self.meters_value = tk.StringVar()

        meters_label = ttk.Label(self, text="Meters: ")
        meters_input = ttk.Entry(self, width=10, textvariable=self.meters_value)
        feet_label = ttk.Label(self, text="Feet: ")
        feet_display = ttk.Label(self, textvariable=self.feet_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate_feet)

        meters_label.grid(column=0, row=0, sticky="W", padx=5, pady=5)
        meters_input.grid(column=1, row=0, sticky="EW",padx=5, pady=5)
        meters_input.focus()

        feet_label.grid(column=0, row=1, sticky ="W",padx=5, pady=5)
        feet_display.grid(column=1, row=1, sticky ="EW",padx=5, pady=5)

        calc_button.grid(column=0, row=2, columnspan=2, sticky ="EW",padx=5, pady=5)

    def calculate_feet(self, *args):
            try:
                meters = float(self.meters_value.get())
                feet = meters * 3.28084
                self.feet_value.set(f"{feet:.3f}")
            except ValueError:
                pass


root = DistanceConverter()




root.columnconfigure(0,weight=1)


# -- Widgets --


# -- Layout --



root.mainloop()
