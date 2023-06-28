import tkinter as tk
from tkinter import font
import sys
from tkinter import messagebox
import psutil


root=tk.Tk()
root.title("Basicity Calculator")
custom_font = font.Font(size=14) 
root.geometry( "300x200" )

def handle_button_click():
    ml_HCl = float(entry1.get())
    ml_sample = float(entry2.get()) 
    mol_HCl = (0.1*ml_HCl)/1000
    MWNAOH=40
    sp_gr=1.52
    result = round((mol_HCl*(MWNAOH/ml_sample)/1*100),3)
    result2= round((mol_HCl*(MWNAOH/ml_sample)/sp_gr*100),3)
    return result1.config(text=(f"Basicity ={result} % w/v NaOH \n Basicity ={result2} % w/w NaOH 50%"),
                          font=custom_font,fg="blue")
    
    
label1 = tk.Label(root, text="Κατανάλωση ml οξέος (HCl 0,1N):")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="ml Δείγματος")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

button = tk.Button(root, text = "Calculate", command=handle_button_click)
button.pack()

result1=tk.Label(root,text="")
result1.pack()

def main():
 
    root.mainloop()

def check_already_running(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            messagebox.showerror('Error', 'Your Application is already running!')
            sys.exit(0)

if __name__ == "__main__":
    process_name = "BacisityApp"

    check_already_running(process_name)

    main()