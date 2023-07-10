import tkinter as tk
from tkinter import font
import sys
from tkinter import messagebox
import psutil

root = tk.Tk()
root.title("Salt Calculator")
custom_font = font.Font(size=16) 
# Adjust size
root.geometry( "300x250" )

def handle_button_click():
    input_text1 = float(entry1.get())
    input_text2 = float(entry2.get())
    input_text3 = float(entry3.get())
    input_text4 = float(entry4.get())
#Calculation of 10% of error correction in the extract
    E_mlcor=input_text2+(input_text2*10)/100
#Calculation of Salt percentage in solid matter through titration
    result=(input_text4/1000)*(5.844)*(E_mlcor/input_text3)*(100/input_text1)
    result=round(result,3) 
    return label5.config(text=("Salt=",result,"%"),font=custom_font,fg="blue")
    
label1 = tk.Label(root, text="gr Δείγματος:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="ml Εκχυλίσματος:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

label3 = tk.Label(root, text="ml δείγματος")
label3.pack()
entry3 = tk.Entry(root)
entry3.pack()

label4= tk.Label(root, text="Κατανάλωση AgNO3:")
label4.pack()
entry4 = tk.Entry(root)
entry4.pack()

button = tk.Button(root, text="Submit", command=handle_button_click)
button.pack()

label5=tk.Label(root,text="")
label5.pack()

footer_label = tk.Label(root, text="Developed by Ioannis Tsioukis")
footer_label.pack(side=tk.BOTTOM, pady=10)


def main():
 
    root.mainloop()

def check_already_running(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            messagebox.showerror('Error', 'Your Application is already running!')
            sys.exit(0)

if __name__ == "__main__":
    process_name = "SaltApp"

    check_already_running(process_name)

    main()







