import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import qrcode
import psutil
import sys
from PIL import Image, ImageDraw, ImageFont

def generate_qr_code():
    text = input_entry.get()
    sample=input_entry2.get()
    if text:
        try:
            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(text)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            filename = input_entry2.get() + '.png'
            
            # Save the QR code image
            img.save(filename)

            # Add text to the image
            image_with_text = add_text_to_image(img, sample)

            # Save the image with text
            image_with_text.save(filename)
            
            messagebox.showinfo('QR Code Generated', f'The QR code image has been saved as {filename}.')
        except:
            messagebox.showerror('Error', 'An error occurred while generating the QR code.')
    else:
        messagebox.showwarning('Empty Input', 'Please enter some text.')

def add_text_to_image(image, sample):
    draw = ImageDraw.Draw(image)
    width, height = image.size

    # Define the font size and type
    font_size = 32
    font = ImageFont.truetype("arial.ttf", font_size)

    # Calculate the size of the text
    text_width, text_height = draw.textsize(sample, font)

    # Calculate the position to place the text
    text_x = (width - text_width) // 2
    text_y = height - text_height - 10

    # Draw the text on the image
    draw.text((text_x, text_y), sample, fill='black', font=font)

    return image

# Create the main window
window = tk.Tk()
window.title('QRCode-Gen')
window.geometry("300x160")

# Create a label and an entry field
label = ttk.Label(window, text='Enter text:')
label.pack()
input_entry = ttk.Entry(window, width=40)
input_entry.pack()

label2 = ttk.Label(window, text='Enter Sample Name:')
label2.pack()
input_entry2 = ttk.Entry(window)
input_entry2.pack()

# Create a button to generate the QR code
button = ttk.Button(window, text='Generate QR Code', command=generate_qr_code)
button.pack()

footer_label = tk.Label(window, text="Developed by Ioannis Tsioukis")
footer_label.pack(side=tk.BOTTOM, pady=10)

# Run the main event loop
def main():
    window.mainloop()

def check_already_running(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            messagebox.showerror('Error', 'Your Application is already running!')
            sys.exit(0)

if __name__ == "__main__":
    process_name = "Barcoder"
    check_already_running(process_name)
    main()
