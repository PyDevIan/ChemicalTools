#APPLICATION
# Import module
import tkinter as tk
from tkinter import font
import sys
from tkinter import messagebox
import psutil
from PIL import Image ,ImageTk
import os

# Create object
root =tk.Tk()
  
# Adjust size
root.geometry( "320x280" )
root.title("Forklift Scenarios")
custom_font = font.Font(size=16) 
#background image
current_directory = os.path.dirname(os.path.abspath(__file__))
image_filename = "clark.png"
image_path = os.path.join(current_directory, image_filename)
image = Image.open(image_path)

tk_image = ImageTk.PhotoImage(image)


background_label =tk.Label(root, image=tk_image)
background_label.pack()
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Επιλογή εικόνας από directory αναλόγως το σενάριο 
def show():
    # Συνάρτηση για σύνθεση του URL βάση της επιλογής του χρήστη
    def Senaria(x):
      current_directory = os.path.dirname(os.path.abspath(__file__))
      image_filename = x+".png"
      image_path = os.path.join(current_directory, image_filename)
      image=Image.open(image_path )
      return image.show()

    plan=clicked.get()
    if plan==planAa:
      Senaria("planAa")
    elif plan==planAb:
      Senaria("planAb")
    elif plan==planAc:
      Senaria("planAc")
    elif plan==planBa:
      Senaria("planBa")
    elif plan==planBb:
      Senaria("planBb")
    elif plan==planBc:
      Senaria("planBc")
    elif plan==planBd:
      Senaria("planBd")
    elif plan==planCa:
      Senaria("planCa")
    elif plan==planCb:
      Senaria("planCb")
    elif plan==plan3Aa:
      Senaria("plan3Aa")
    elif plan==plan3Abfort:
      Senaria("plan3Abfort")
    elif plan==plan3Abvlav:
      Senaria("plan3Abvlav")
    elif plan==plan3Ac:
      Senaria("plan3Ac")
    elif plan==plan3Ba:
      Senaria("plan3Ba")
    elif plan==plan3Bb:
      Senaria("plan3Bb")      
    elif plan==plan3Bcfort:
      Senaria("plan3Bcfort")      
    elif plan==plan3Bcvlav:
      Senaria("plan3Bcvlav")        
    elif plan==plan3Bdfort:
      Senaria("plan3Bdfort")      
    elif plan==plan3Bdvlav:
      Senaria("plan3Bdvlav")      
    elif plan==plan3Cvlav_fort:
      Senaria("plan3Cvlav_fort")      
    else :
      print("Not a valid plan")
      

#Διαφορετικά Σενάρια κλαρκ παραλαβής
planAa="4 Κλάρκ: Πριν της 20:00, χωρίς φορτηγό ή βλάβη"
planAb="4 Κλάρκ: Πριν της 20:00, με φορτηγό"
planAc="4 Κλάρκ: Πριν της 20:00, με φορτηγό και βλάβη"
planBa="4 Κλάρκ: Δεξαμενισμός κάτω πατάρι, χωρίς φορτηγό ή βλάβη"
planBb="4 Κλάρκ: Δεξαμενισμός πάνω πατάρι, χωρίς φορτηγό ή βλάβη"
planBc="4 Κλάρκ: Δεξαμενισμός κάτω πατάρι, με φορτηγό"
planBd="4 Κλάρκ: Δεξαμενισμός πάνω πατάρι, με φορτηγό"
planCa="4 Κλάρκ: Δεξαμενισμός κάτω πατάρι, με φορτηγό και βλάβη"
planCb="4 Κλάρκ: Δεξαμενισμός πάνω πατάρι, με φορτηγό και βλάβη"
plan3Aa="3 Κλάρκ:Πριν της 20:00, χωρίς φορτηγό η βλάβη"
plan3Abfort="3 Κλάρκ: Πριν της 20:00, με φορτηγό"
plan3Abvlav="3 Κλάρκ:Πριν της 20:00, με Βλάβη"
plan3Ac="3 Κλάρκ:Πριν της 20:00, με φορτηγό και βλάβη"
plan3Ba="3 Κλάρκ: Δεξαμενισμός κάτω πατάρι, χωρίς φορτηγό ή βλάβη"
plan3Bb="3  Κλάρκ: Δεξαμενισμός πάνω πατάρι, χωρίς φορτηγό ή βλάβη"
plan3Bcfort="3 Κλάρκ: Δεξαμενισμός κάτω πατάρι, με φορτηγό"
plan3Bcvlav="3 Κλάρκ: Δεξαμενισμός κάτω πατάρι, με βλάβη"
plan3Bdfort="3 Κλάρκ: Δεξαμενισμός πάνω πατάρι, με φορτηγό"
plan3Bdvlav="3 Κλάρκ: Δεξαμενισμός πάνω πατάρι, με βλάβη"
plan3Cvlav_fort="3 Κλάρκ: Δεξαμενισμός με φορτηγό και βλάβη"
  
# Dropdown menu options
options = [planAa,planAb,planAc,planBa,planBb,planBc,planBd,planCa,planCb,
           plan3Aa,plan3Abfort,plan3Abvlav,plan3Ac,plan3Ba,plan3Bb,plan3Bcfort,plan3Bcvlav,
           plan3Bdfort,plan3Bdvlav,plan3Cvlav_fort]
  
# datatype of menu text
clicked = tk.StringVar()
  
# initial menu text
clicked.set( "Choose your Scenario" )
  
# Create Dropdown menu
drop = tk.OptionMenu( root , clicked , *options ,)
drop.pack()
  
# Create button, it will change label text
button =tk.Button( root , text = "click Me" , command = show ).pack()
  
footer_label = tk.Label(root, text="Developed by PyDevIan")
footer_label.pack(side=tk.BOTTOM, pady=10)
# Execute tkinter


def main():
 
  root.mainloop()

def check_already_running(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            messagebox.showerror('Error', 'Your Application is already running!')
            sys.exit(0)

if __name__ == "__main__":
    process_name = "SenariaClark"

    check_already_running(process_name)

    main()
