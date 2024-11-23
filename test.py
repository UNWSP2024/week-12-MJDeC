import tkinter as tk
import tkinter.messagebox

def calculate():
  value = float(entry.get())
  if radio_var.get() == 1:
    result = value * 2
  elif radio_var.get() == 2:
    result = value * 3
  else:
    result = value

result_label.config(text=f"Result: {result}")

window = tk.Tk()
window.title("Multiplier")

entry = tk.Entry(window)
entry.pack()

radio_var = tk.IntVar()
radio_var.set(1)
    
#create radiobuttons
self.radio1=tkinter.Radiobutton(window,text="Daytime (6:00 A.M. through 5:59 P.M.) = $0.02 per minute",variable=radio_var,value=.02)
self.radio2=tkinter.Radiobutton(window,text="Evening (6:00 P.M.  through 11:59 P.M.) = $0.12 per minute",variable=radio_var,value=.12)
self.radio3=tkinter.Radiobutton(window,text="Off-Peak (Midnight through 5:59 A.M.) = $0.05 per minute",variable=radio_var,value=.05)
self.radio1.pack()
self.radio2.pack()
self.radio3.pack()
  
#create calculate button
self.calc=tkinter.Button(window,text="Calculate",command=calculate)
self.calc.pack()
self.quit_button=tkinter.Button(window,text="Quit",command=self.window.destroy)
self.quit_button.pack()
    
window.mainloop()
calculate()
