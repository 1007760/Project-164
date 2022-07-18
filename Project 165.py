from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
root = Tk()
root.geometry("500x500")
root.title("Project 164-165")
root.configure(bg = "teal")
image = Label(root, bg = "teal")
image.place(relx = 0.5, rely = 0.5, anchor = CENTER)
img_path = StringVar()

def openimage() :
    global img_path
    img_path = fildialog.askopenfilename(title = "Open image file", filetypes = [("Image Files","*.jpg;*.gif;*.jpg;;*.png;*.txt")])
    print(img_path)
    img = img_path
    image["image"] = img
    img.close()

btn = Button(root, text = "Open Image", bg = "grey")
btn.place(relx = 0.5, rely = 0.3, anchor = CENTER)
root.mainloop()