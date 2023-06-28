import tkinter as tk
from tkinter import font
import sys
from tkinter import messagebox
import psutil
import openpyxl
from datetime import datetime, timezone

# Create object
root =tk.Tk()
  
# Adjust size
root.geometry( "320x350" )
root.title("Lye Calculator")
custom_font = font.Font(size=12 ) 
TANKVOLUME=52
TANKHEIGHT=273.68

def write(x ,y ,z,w):
        file_path = 'Ε4_75_Lye.xlsx'  # Replace with the actual file path
        book = openpyxl.load_workbook(file_path)
        sheet_name = w # Replace with the actual sheet name
        row_index = int(x)  # Replace with the desired row index
        column_name = str(y)  # Replace with the desired column name
        new_value = z # Replace with the new value
        
        
        sheet = book[sheet_name]
        column_index = openpyxl.utils.column_index_from_string(column_name)
        column_letter = openpyxl.utils.get_column_letter(column_index)
        cell_address = f"{column_letter}{row_index}"
        cell = sheet[cell_address]
        cell.value = new_value   
        book.save('Ε4_75_Lye.xlsx')
        
        
        # Save the changes



def calculate():
    lye_level_start = float(entry1.get())
    Dense_lye=float(entry2.get())/100
    Lye_C_start= float(entry3.get())/100
    Lye_C_final = float(entry4.get())/100
    Tank= int(entry6.get())
    
    lye_level_start_m=lye_level_start*0.19
    starting_lye_kg=lye_level_start_m*Lye_C_start*2130
    final_lye_kg=Lye_C_final*TANKVOLUME*2130
    manuf_lye=TANKVOLUME-lye_level_start_m
    demanding_lye_kg=round((final_lye_kg-starting_lye_kg),2)
    Lye_requested_m3=round((demanding_lye_kg/Dense_lye/2130),2)
    Lye_height_final=round(((Lye_requested_m3/0.19)+(lye_level_start)),2)
    Water_height_final=round((TANKHEIGHT-Lye_height_final),2)
    
    now = datetime.now(timezone.utc)
    formatted_time = now.strftime("%d-%m-%y")
    Lot = now.strftime("%y%m%d")
    salt_kg=round(((manuf_lye*600)/TANKVOLUME),2)
    
    write('4','H',formatted_time,'ΣΟΔΑ 1')
    write('5','H',Tank,'ΣΟΔΑ 1')
    write('4','E',Lot,'ΣΟΔΑ 1')
    write('15','E',lye_level_start_m,'ΣΟΔΑ 1')
    write('16','D',manuf_lye,'ΣΟΔΑ 1')
    write('10','I',salt_kg,'ΣΟΔΑ 1')
    write('9','C',entry2.get(),'ΣΟΔΑ 1')
    write('10','C',Lye_requested_m3,'ΣΟΔΑ 1')
    
    

    
    
    return label5.config(text=f'Για την παρασκευή χρειάζεται: \n Σόδα (υπόγεια): {Lye_requested_m3} m3 ή'+
                         f' \n Τελικό ύψος Σόδας {Lye_height_final} cm και \n Νερό: {Water_height_final} cm '+
                         f'\n Καταναλώθηκαν: {demanding_lye_kg} Kg Σόδας'
                         f'\n {salt_kg} kg Αλάτι ', font=custom_font, fg="red")


label1 = tk.Label(root, text="Ύψος στάθμης αρχικό (cm):")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Συγκέντρωση πυκνής Σόδας %:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

label3 = tk.Label(root, text="Συγκέντρωση σόδας αρχικό %:")
label3.pack()
entry3 = tk.Entry(root)
entry3.pack()

label4 = tk.Label(root, text="Συγκέντρωση σόδας τελικό %:")
label4.pack()
entry4 = tk.Entry(root)
entry4.pack()

label6 = tk.Label(root, text="Δεξαμενή :")
label6.pack()
entry6 = tk.Entry(root)
entry6.pack()


  
# Create button, it will change label text
button =tk.Button( root , text = "Calculate" , command = calculate ).pack()

  
label5=tk.Label(root,text="")
label5.pack()

def main():
 
  root.mainloop()

def check_already_running(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            messagebox.showerror('Error', 'Your Application is already running!')
            sys.exit(0)

if __name__ == "__main__":
    process_name = "BrineCalc"

    check_already_running(process_name)

    main()