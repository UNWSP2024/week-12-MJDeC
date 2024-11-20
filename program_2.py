import tkinter as Tk
import tkinter.messagebox

#Create "Auto" Class
class Auto:
  def __init__(self):
    self.main_window=tkinter.Tk()
    self.main_window.title("Joe's Automotive Options")
    
    check1=Tk.IntVar
    check2=Tk.IntVar
    check3=Tk.IntVar
    check4=Tk.IntVar
    check5=Tk.IntVar
    check6=Tk.IntVar
    check7=Tk.IntVar
    
    #Create checkbuttons
    self.check1=tkinter.Checkbutton(self.main_window,text="Oil Change-$30.00",onvalue=1,offvalue=0)
    self.check1.pack()
    self.check2=tkinter.Checkbutton(self.main_window,text="Lube Job-$20.00",onvalue=1,offvalue=0)
    self.check2.pack()
    self.check3=tkinter.Checkbutton(self.main_window,text="Radiator Flush-$40.00",onvalue=1,offvalue=0)
    self.check3.pack()
    self.check4=tkinter.Checkbutton(self.main_window,text="Transmission Fluid-$100.00",onvalue=1,offvalue=0)
    self.check4.pack()
    self.check5=tkinter.Checkbutton(self.main_window,text="Inspection-$35.00",onvalue=1,offvalue=0) 
    self.check5.pack()
    self.check6=tkinter.Checkbutton(self.main_window,text="Muffler Replacement-$200.00",onvalue=1,offvalue=0)
    self.check6.pack()
    self.check7=tkinter.Checkbutton(self.main_window,text="Tire Rotation-$20.00",onvalue=1,offvalue=0)
    self.check7.pack()

    def total():
      if check1.get==1:
        cost=cost+30.00
      if check2.get==1:
        cost=cost+20.00
      if check3.get==1:
        cost=cost+40.00
      if check4.get==1:
        cost=cost+100.00
      if check5.get==1:
        cost=cost+35.00
      if check6.get==1:
        cost=cost+200.00
      if check7.get==1:
        cost=cost+20.00
      tkinter.messagebox.showinfo("Total",f"Your total cost is ${cost}")

    
    #create total button
    self.total_button=tkinter.Button(self.main_window,text="Total Cost",command=total)
    self.total_button.pack()
      
    tkinter.mainloop()
                                                                         
auto=Auto()
