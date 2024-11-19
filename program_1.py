import tkinter
import tkinter.messagebox

class MPG:
    def __init__(self):
        self.main_window=tkinter.Tk()
        self.main_window.title("MPG Calculator")
      
        self.gas_gallons=tkinter.IntVar()
        self.miles=tkinter.IntVar()
        self.calculate=tkinter.StringVar()

        self.gas_gallons_label=tkinter.Label(self.main_window, text="Please enter the number of gallons of gas the vehicle holds:")
        self.gas_gallons_label.pack()
        self.gas_gallons_entry=tkinter.Entry(self.main_window, textvariable=self.gas_gallons)
        self.gas_gallons_entry.pack()

        self.miles_label=tkinter.Label(self.main_window,text="Enter the number of miles that can be driven on a full tank:")
        self.miles_label.pack()
        self.miles_entry=tkinter.Entry(self.main_window,textvariable=self.miles)
        self.miles_entry.pack()

        self.calculate_button=tkinter.Button(self.main_window,text="Calculate MPG",command=self.mpg_calc)
        self.calculate_button.pack()

        tkinter.mainloop()

    def mpg_calc(self):
      gas_gallons_val=self.gas_gallons.get()
      miles_val=self.miles.get()
      final_calc=(gas_gallons_val/miles_val)
      tkinter.messagebox.show("MPG",f"The vehicle gets {final_calc} miles per gallon of gas.")

mpg=MPG()
