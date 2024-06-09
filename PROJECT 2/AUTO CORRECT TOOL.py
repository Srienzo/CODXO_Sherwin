from textblob import TextBlob
from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

def auto_correct(event=None):
    text = Input_text.get(1.0, END)
    corrected_text = TextBlob(text).correct().string
    Output_text.delete(1.0, END)
    Output_text.insert(END, corrected_text)

def clear():
    Input_text.delete(1.0, END)
    Output_text.delete(1.0, END)

# Initialize Tkinter main window
mainwin = Tk()
mainwin.geometry('850x600')
mainwin.title("Auto Correct @Sherwin")

# Load background image from URL
url = "https://wallpapercave.com/wp/wp5642517.jpg"
response = requests.get(url)
bg_image = Image.open(BytesIO(response.content))
bg_image = bg_image.resize((850, 600), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a canvas to place the background image
canvas = Canvas(mainwin, width=850, height=600)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Add heading
canvas.create_text(425, 40, text="AUTO CORRECT TOOL", font=('Helvetica', 24, 'bold'), fill='#61DAFB')

# Create input and output text boxes
input_frame = Frame(mainwin, bg='#282C34')
input_frame.place(x=10, y=80, width=400, height=400)
Label(input_frame, text="Input Text", font=('Helvetica', 18, 'bold'), bg='#282C34', fg='white').pack(pady=10)
Input_text = Text(input_frame, font=('Helvetica', 14), bg='#1E1E1E', fg='white', height=10, wrap=WORD, padx=10, pady=10, width=40, insertbackground='white', borderwidth=2, relief="solid")
Input_text.pack()

output_frame = Frame(mainwin, bg='#282C34')
output_frame.place(x=440, y=80, width=400, height=400)
Label(output_frame, text="Corrected Output", font=('Helvetica', 18, 'bold'), bg='#282C34', fg='white').pack(pady=10)
Output_text = Text(output_frame, font=('Helvetica', 14), bg='#1E1E1E', fg='white', height=10, wrap=WORD, padx=10, pady=10, width=40, insertbackground='white', borderwidth=2, relief="solid")
Output_text.pack()

# Bind the auto_correct function to KeyRelease event
Input_text.bind("<KeyRelease>", auto_correct)

# Clear button
Button(mainwin, text="Clear", font=('Helvetica', 16, 'bold'), command=clear, bg='#61DAFB', fg='#282C34', borderwidth=2, relief="solid").place(x=380, y=500)

mainwin.mainloop()
