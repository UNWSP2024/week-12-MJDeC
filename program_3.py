import tkinter

class Rates:
  def __init__(self):
    self.main_window=tkinter.Tk()
    self.main_window.title("Long-Distance Call Rates")

    self.radio1=tkinter.Radiobutton(self.main_window,text="Daytime (6:00 A.M. through 5:59 P.M.) = $0.02 per minute")
    self.radio1.pack()
    self.radio2=tkinter.Radiobutton(self.main_window,text="Evening (6:00 P.M.  through 11:59 P.M.) = $0.12 per minute")
    self.radio2.pack()
    self.radio3=tkinter.Radiobutton(self.main_window,text="Off-Peak (midnight through 5:59 P.M.) = $0.05")
    self.radio3.pack()

    tkinter.mainloop()






rates=Rates()
