import tkinter as Tk
import tkinter.messagebox

#create "MPG" class
class MPG:
    def __init__(self):
        #initialize window
        self.main_window=tkinter.Tk()
        self.main_window.title("MPG Calculator")
      
        self.gas_gallons=tkinter.IntVar()
        self.miles=tkinter.IntVar()
        self.calculate=tkinter.StringVar()

        #create gas gallons entry
        self.gas_gallons_label=tkinter.Label(self.main_window, text="Please enter the number of gallons of gas the vehicle holds:")
        self.gas_gallons_label.pack()
        self.gas_gallons_entry=tkinter.Entry(self.main_window, textvariable=self.gas_gallons)
        self.gas_gallons_entry.pack()

        #create miles per full tank entry
        self.miles_label=tkinter.Label(self.main_window,text="Enter the number of miles that can be driven on a full tank:")
        self.miles_label.pack()
        self.miles_entry=tkinter.Entry(self.main_window,textvariable=self.miles)
        self.miles_entry.pack()

        #create calculate button
        self.calculate_button=tkinter.Button(self.main_window,text="Calculate MPG",command=self.mpg_calc)
        self.calculate_button.pack()

        tkinter.mainloop()
        
    #function that calculates mpg
    def mpg_calc(self):
      gas_gallons_val=self.gas_gallons.get()
      miles_val=self.miles.get()
      final_calc=(miles_val/gas_gallons_val)
      tkinter.messagebox.showinfo("MPG",f"The vehicle gets {final_calc} miles per gallon of gas.")

mpg=MPG()
