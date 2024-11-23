import tkinter as tk
import tkinter.messagebox
#Create "Auto" Class
class Auto:
  def __init__(self):
    self.main_window=tkinter.Tk()
    self.main_window.title("Joe's Automotive Options")
    
    check1=tk.IntVar()
    check2=tk.IntVar()
    check3=tk.IntVar()
    check4=tk.IntVar()
    check5=tk.IntVar()
    check6=tk.IntVar()
    check7=tk.IntVar()
    
    #Create checkbuttons
    self.oil=tkinter.Checkbutton(self.main_window,text="Oil Change-$30.00",variable=check1,onvalue=1,offvalue=0)
    self.oil.pack()
    self.lube=tkinter.Checkbutton(self.main_window,text="Lube Job-$20.00",variable=check2,onvalue=1,offvalue=0)
    self.lube.pack()
    self.rad=tkinter.Checkbutton(self.main_window,text="Radiator Flush-$40.00",variable=check3,onvalue=1,offvalue=0)
    self.rad.pack()
    self.tf=tkinter.Checkbutton(self.main_window,text="Transmission Fluid-$100.00",variable=check4,onvalue=1,offvalue=0)
    self.tf.pack()
    self.insp=tkinter.Checkbutton(self.main_window,text="Inspection-$35.00",variable=check5,onvalue=1,offvalue=0) 
    self.insp.pack()
    self.muff=tkinter.Checkbutton(self.main_window,text="Muffler Replacement-$200.00",variable=check6,onvalue=1,offvalue=0)
    self.muff.pack()
    self.tire=tkinter.Checkbutton(self.main_window,text="Tire Rotation-$20.00",variable=check7,onvalue=1,offvalue=0)
    self.tire.pack()
    
    def total():
      cost=0
      if check1.get()==1:
        cost=cost+30.00
      if check2.get()==1:
        cost=cost+20.00
      if check3.get()==1:
        cost=cost+40.00
      if check4.get()==1:
        cost=cost+100.00
      if check5.get()==1:
        cost=cost+35.00
      if check6.get()==1:
        cost=cost+200.00
      if check7.get()==1:
        cost=cost+20.00
      tkinter.messagebox.showinfo("Total",f"Your total cost is ${cost:.2f}")

    #create total button
    self.total_button=tkinter.Button(self.main_window,text="Total Cost",command=total)
    self.total_button.pack()
    self.quit_button=tkinter.Button(self.main_window,text="Quit",command=self.main_window.destroy)
    self.quit_button.pack()
      
    tkinter.mainloop()
                                                                         
auto=Auto()
