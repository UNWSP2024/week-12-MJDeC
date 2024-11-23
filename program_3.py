import tkinter as tk
import tkinter.messagebox

#create "Rates" class
class Rates:
  def __init__(self):
    self.main_window=tkinter.Tk()
    self.main_window.title("Long-Distance Call Rates")

    #select one radiobutton
    self.radio_var=tkinter.IntVar()
    self.radio_var.set(1)

    #enter amount of minutes you want to talk for
    self.min_num=tkinter.Label(self.main_window,text="Enter the number of minutes you would like to speak for:")
    self.min_num.pack()
    self.entry_box=tkinter.Entry(self.main_window)
    self.entry_box.pack()
    
    #create radiobuttons
    self.radio1=tkinter.Radiobutton(self.main_window,text="Daytime (6:00 A.M. through 5:59 P.M.) = $0.02 per minute",variable=self.radio_var,value=".02")
    self.radio2=tkinter.Radiobutton(self.main_window,text="Evening (6:00 P.M.  through 11:59 P.M.) = $0.12 per minute",variable=self.radio_var,value=".12")
    self.radio3=tkinter.Radiobutton(self.main_window,text="Off-Peak (Midnight through 5:59 A.M.) = $0.05 per minute",variable=self.radio_var,value=".05")
    self.radio1.pack()
    self.radio2.pack()
    self.radio3.pack()

    def charge(self):
      number=float(self.entry_box.get())
      multiplier=float(self.radio_var.get())
      result=number*multiplier
      tkinter.messagebox.showinfo("Charge",f"Your charge is ${result:.2f}")
  
    #create calculate button
    self.calc=tkinter.Button(self.main_window,text="Calculate",command=charge)
    self.calc.pack()
    
    tkinter.mainloop()
rates=Rates()
