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
        self.frames = dict()

        container = ttk.Frame(self)
        container.grid(padx=60, pady=30, sticky="EW")

        for FrameClass in (MetersToFeet, FeetToMeters):
            frame = FrameClass(container, self)
            self.frames[FrameClass] = frame
            frame.grid(row=0, column=0, sticky="NSEW")
        
        self.show_frame(MetersToFeet)

    def show_frame(self, container):
        frame = self.frames[container]
        self.bind("<Return>", frame.calculate)
        self.bind("<KP_Enter>", frame.calculate)
        frame.tkraise()

class MetersToFeet(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        self.feet_value = tk.StringVar()
        self.meters_value = tk.StringVar()

        meters_label = ttk.Label(self, text="Meters: ")
        meters_input = ttk.Entry(self, width=10, textvariable=self.meters_value)
        feet_label = ttk.Label(self, text="Feet: ")
        feet_display = ttk.Label(self, textvariable=self.feet_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate)
        switch_page_button = ttk.Button(
            self,
            text="Switch to feet conversion",
            command=lambda: controller.show_frame(FeetToMeters)
            )

        meters_label.grid(column=0, row=0, sticky="W", padx=5, pady=5)
        meters_input.grid(column=1, row=0, sticky="EW",padx=5, pady=5)
        meters_input.focus()

        feet_label.grid(column=0, row=1, sticky ="W",padx=5, pady=5)
        feet_display.grid(column=1, row=1, sticky ="EW",padx=5, pady=5)

        calc_button.grid(column=0, row=2, columnspan=2, sticky ="EW",padx=5, pady=5)
        switch_page_button.grid(column=0, row=3, columnspan=2, sticky="EW")

    def calculate(self, *args):
            try:
                meters = float(self.meters_value.get())
                feet = meters * 3.28084
                self.feet_value.set(f"{feet:.3f}")
            except ValueError:
                pass

class FeetToMeters(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        self.feet_value = tk.StringVar()
        self.meters_value = tk.StringVar()

        feet_label = ttk.Label(self, text="Feet: ")
        feet_input = ttk.Entry(self, width=10, textvariable=self.feet_value)
        meters_label = ttk.Label(self, text="Meters: ")
        meters_display = ttk.Label(self, textvariable=self.meters_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate)
        switch_page_button = ttk.Button(
            self,
            text="Switch to meters conversion",
            command=lambda: controller.show_frame(MetersToFeet)
            )

        feet_label.grid(column=0, row=0, sticky="W", padx=5, pady=5)
        feet_input.grid(column=1, row=0, sticky="EW",padx=5, pady=5)
        feet_input.focus()

        meters_label.grid(column=0, row=1, sticky ="W",padx=5, pady=5)
        meters_display.grid(column=1, row=1, sticky ="EW",padx=5, pady=5)

        calc_button.grid(column=0, row=2, columnspan=2, sticky ="EW",padx=5, pady=5)
        switch_page_button.grid(column=0, row=3, columnspan=2, sticky="EW")

    def calculate(self, *args):
            try:
                feet = float(self.feet_value.get())
                meters = feet / 3.28084
                self.meters_value.set(f"{meters:.3f}")
            except ValueError:
                pass

root = DistanceConverter()




root.columnconfigure(0,weight=1)


# -- Widgets --


# -- Layout --



root.mainloop()
