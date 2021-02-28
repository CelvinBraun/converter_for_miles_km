from tkinter import *

class Convert:

    def __init__(self):

        self.direction = True
        self.value = 0

        # label settings
        self.top_value_label = Label(text="Miles")
        self.top_value_label.grid(row=0, column=3)
        self.bottom_value_label = Label(text="Km")
        self.bottom_value_label.grid(row=1, column=3)
        self.equal_label = Label(text="is equal to:")
        self.equal_label.grid(row=1, column=0)
        self.result_label = Label(text="0")
        self.result_label.grid(row=1, column=2)

        # entry
        self.user_input = Entry()
        self.user_input.config(width=5)
        self.user_input.grid(row=0, column=2)

        # button settings
        self.calc_button = Button(text="Calculate", command=self.check_direction)
        self.calc_button.grid(row=4, column=2)
        self.switch_button = Button(text="Switch Units", command=self.set_direction)
        self.switch_button.grid(row=4, column=3)

    def set_direction(self):
        if self.direction == True:
            self.direction = False
            self.check_direction()
        else:
            self.direction = True
            self.check_direction()

    def check_direction(self):
        if self.direction == True:
            self.top_value_label.config(text="Miles")
            self.bottom_value_label.config(text="Km")
            self.miles_to_km()
        else:
            self.top_value_label.config(text="Km")
            self.bottom_value_label.config(text="Miles")
            self.km_to_miles()

    def miles_to_km(self):
        miles = self.user_input.get()
        result = float(miles) * 1.609344
        self.result_label.config(text=result)

    def km_to_miles(self):
        km = self.user_input.get()
        result = float(km) * 0.62137119223733
        self.result_label.config(text=result)