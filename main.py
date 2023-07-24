from tkinter.messagebox import showinfo

import cv2
import pytesseract
import tkinter as tk
from tkinter import filedialog as fd

button = None  # Declare button as global variable
data = None  # Declare data as global variable


def imageToText():
    global button, data  # Access the global button and data variables
    image = cv2.imread(selectFile())
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresholded_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(thresholded_image)
    list = text.split("\n")
    print(list)
    sortedlist = sortList(list)
    print(sortedlist)
    data["text"] = '\n'.join(sortedlist)
    button["state"] = "disabled"

def selectFile():
    filetypes = (('image files', '.png'),
                ('image files', '.jpg'))
    filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
    return filename


def sortList(unsortedList):
    sortedList = []

    # Read stores.txt to get store names
    with open('stores.txt') as f:
        stores = set(f.read().splitlines())

    # Loop through the unsortedList and check for stores and dollar amounts
    for line in unsortedList:
        words = line.lower().split()  # Split the line into words
        if any(word in stores for word in words) or any(any(c.isdigit() and '.' in word[i:] for i, c in enumerate(word)) for word in words):
            sortedList.append(line)

    return sortedList


def main():
    global button, data  # Declare button and data as global variables
    app = tk.Tk()
    label = tk.Label(app, text="Welcome to your image reader")
    button = tk.Button(app, text="Open image", command=imageToText)
    data = tk.Label(app, text="")
    label.pack()
    button.pack()
    data.pack()
    app.mainloop()

main()
