import tkinter as tk
from tkinter import font
from tkinter import messagebox
import sys  
import psutil



root=tk.Tk()
root.geometry('280x200')
root.title("Acidity Calculator")
custom_font = font.Font(size=10) 

def handle_button_click():
    imput_mlsample=float(mlsample.get())
    input_mlNaOH=float(mlNaOH.get())
    mlNaoH=(input_mlNaOH/1000)*0.1
    Lactic_result=round((((mlNaoH*90)*100)/imput_mlsample),3)
    Acetic_result=round((((mlNaoH*60)*100)/imput_mlsample),3)
    Citric_result=round((((mlNaoH*192.12/3)*100)/imput_mlsample),3)
    HCl_result=round(((mlNaoH*36.4)*100/imput_mlsample),3)
    oleic_result=round(((mlNaoH*282)*100/(imput_mlsample*0.91)),3)
    

    return  label3.config(text=f'Acidity={Lactic_result} % w/w Lactic acid''\n'
                            f'Acidity={Acetic_result} % w/w Acetic acid''\n'
                            f'Acidity={Citric_result} % w/w Citric acid''\n'
                            f'Acidity={HCl_result} % w/w HCl acid''\n'
                            f'Acidity={oleic_result} % w/w Oleic acid''\n'
                            ,font=custom_font,fg="blue"
    )


label1 = tk.Label(root, text="ml Δείγματος:")
label1.pack()
mlsample = tk.Entry(root)
mlsample.pack()

label2 = tk.Label(root, text="ml NaOH O,1N:")
label2.pack()
mlNaOH = tk.Entry(root)
mlNaOH.pack()

button = tk.Button(root, text="Submit", command=handle_button_click)
button.pack()

label3=tk.Label(root,text="")
label3.pack()


def main():
 
    root.mainloop()

def check_already_running(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            messagebox.showerror('Error', 'Your Application is already running!')
            sys.exit(0)

if __name__ == "__main__":
    process_name = "AcidityApp"

    check_already_running(process_name)
    
    main()

