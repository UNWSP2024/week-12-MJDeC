import tkinter

#Create "Auto" Class
class Auto:
  def __init__(self):
    self.main_window=tkinter.Tk()
    self.main_window.title("Joe's Automotive Options")
    
    #Create checkbuttons
    self.check1=tkinter.Checkbutton(self.main_window,text="Oil Change-$30.00")
    self.check1.pack()
    self.check2=tkinter.Checkbutton(self.main_window,text="Lube Job-$20.00")
    self.check2.pack()
    self.check3=tkinter.Checkbutton(self.main_window,text="Radiator Flush-$40.00")
    self.check3.pack()
    self.check4=tkinter.Checkbutton(self.main_window,text="Transmission Fluid-$100.00")
    self.check4.pack()
    self.check5=tkinter.Checkbutton(self.main_window,text="Inspection-$35.00") 
    self.check5.pack()
    self.check6=tkinter.Checkbutton(self.main_window,text="Muffler Replacement-$200.00")
    self.check6.pack()
    self.check7=tkinter.Checkbutton(self.main_window,text="Tire Rotation-$20.00")
    self.check7.pack()
    
    #create total button
    self.total_button=tkinter.Button(self.main_window,text="Total Cost")
    self.total_button.pack()
    

    tkinter.mainloop()
                                                                         
auto=Auto()
