import tkinter as tk
import tkinter.messagebox

#create "Rates" class
class Rates:
  def __init__(self):
    self.main_window=tkinter.Tk()
    self.main_window.title("Long-Distance Call Rates")

    self.radio_var=tkinter.IntVar()
    #self.radio_var.set(1)
    
    #create radiobuttons
    self.radio1=tkinter.Radiobutton(self.main_window,text="Daytime (6:00 A.M. through 5:59 P.M.) = $0.02 per minute",variable=self.radio_var)
    self.radio2=tkinter.Radiobutton(self.main_window,text="Evening (6:00 P.M.  through 11:59 P.M.) = $0.12 per minute",variable=self.radio_var)
    self.radio3=tkinter.Radiobutton(self.main_window,text="Off-Peak (midnight through 5:59 P.M.) = $0.05 per minute",variable=self.radio_var)
    self.radio1.pack()
    self.radio2.pack()
    self.radio3.pack()

    #create entrybox with label and calculate button
    self.min_num=tkinter.Label(self.main_window,text="Enter the number of minutes you would like to speak for:")
    self.min_num.pack()
    self.entry_box=tkinter.Entry(self.main_window)
    self.entry_box.pack()
    self.calc=tkinter.Button(self.main_window,text="Calculate")
    self.calc.pack()
    
    #def charge(self):
      
        #tkinter.messagebox.showinfo("Charge","Your charge is"
    
    tkinter.mainloop()


rates=Rates()
