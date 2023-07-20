# -*- coding: utf-8 -*-
"""
@author: Shrihan Tayal
"""
print("Hello world")

""" Image To Sketch """
import cv2
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import qrcode
import random
import smtplib
from email.message import EmailMessage
import imghdr
from tkinter.filedialog import askopenfilename
import webbrowser

def open_img(frame3):
    """
    Opens a file dialog to select an image file.

    Parameters:
        frame3 (tkinter.Frame): The tkinter frame where the file dialog will be displayed.

    Returns:
        str: The selected file's path.
    """
    global my_img
    frame3.filename = askopenfilename(initialdir="/images")
    return frame3.filename    

def see_image(frame3):
    """
    Reads an image file using OpenCV.

    Parameters:
        frame3 (tkinter.Frame): The tkinter frame to display the file dialog.

    Returns:
        numpy.ndarray: The image as a NumPy array.
    """
    # Reading the image
    image = cv2.imread(open_img(frame3))
    return image

def create_sketch(frame3, frame6):
    """
    Converts the selected image to a pencil sketch using OpenCV.

    Parameters:
        frame3 (tkinter.Frame): The tkinter frame to display the file dialog.
        frame6 (tkinter.Frame): The tkinter frame to display the converted pencil sketch.

    Returns:
        tkinter.Frame: The frame containing the converted pencil sketch.
    """
    image = see_image(frame3)
    # Converting BGR image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Image inversion
    inverted_image = 255 - gray_image
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred = 255 - blurred
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
    cv2.imshow("Original Image", image)
    cv2.imshow("Pencil Sketch", pencil_sketch)
    cv2.imwrite('', pencil_sketch)  # Enter file path
    cv2.waitKey(0)
    return frame6

def Sketch_IT_server(inp_1, frame1):
    """
    Sends the converted pencil sketch via email using Gmail.

    Parameters:
        inp_1 (str): The email address of the recipient.
        frame1 (tkinter.Frame): The tkinter frame for the landing page.

    Returns:
        tkinter.Frame: The frame for the landing page.
    """
    # Sketch_IT server for Gmail
    inp_1 = email.get()
    print("Email Id of the sendee:", inp_1)
    msg = EmailMessage()
    msg['Subject'] = 'Sketch from Sketch_IT'
    msg['From'] = ''          # Enter email id
    msg['To'] = inp_1
    msg.set_content("Sketch from Sketch_IT")

    with open("", "rb") as f:  # Enter file path
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)
    
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('', '')        # Enter Email, password
    # Sender, receiver, message
    server.send_message(msg)
    server.quit()
    
    webbrowser.open_new("www.gmail.com")
    
    return frame1

def OTP_gen():
    """
    Generates a random 6-digit OTP (One-Time Password).

    Returns:
        str: The generated OTP.
    """
    s = "".join([str(random.randint(0, 9)) for i in range(6)])
    return s

def QR_code(s):
    """
    Creates a QR code from the given text.

    Parameters:
        s (str): The text to encode in the QR code.

    Returns:
        PIL.Image.Image: The generated QR code image.
    """
    img = qrcode.make(s)  
    img.save("qrcode.jpeg")
    return img

def Gmail_OTP_server(inp_1):
    """
    Sends the OTP and QR code via email for Gmail verification.

    Parameters:
        inp_1 (str): The email address of the recipient.
    """
    msg = EmailMessage()
    msg['Subject'] = 'User Authentication'
    msg['From'] = ''      # Enter Email ID
    msg['To'] = inp_1
    msg.set_content("Scan the QR code and enter the OTP")
    
    with open("qrcode.jpeg", "rb") as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
    
    msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)
    
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('', '')     # Enter Email, password
    # Sender, receiver, message
    server.send_message(msg)
    server.quit()
    
def Gmail_id(frame4, frame5):
    """
    Verifies the Gmail id and sends the OTP for verification.

    Parameters:
        frame4 (tkinter.Frame): The tkinter frame for the OTP page.
        frame5 (tkinter.Frame): The tkinter frame for the error page.

    Returns:
        tkinter.Frame: The frame for the OTP page or error page based on the validity of the Gmail id.
    """
    inp_1 = email.get()
    print(inp_1)
    if inp_1[-10:] == "@gmail.com":
        Gmail_OTP_server(inp_1)
        return frame4
    else:
        return frame5

def verify(OTP, frame3, frame5):
    """
    Verifies the OTP for Gmail login credentials.

    Parameters:
        OTP (str): The 6-digit OTP entered by the user.
        frame3 (tkinter.Frame): The tkinter frame for the image page.
        frame5 (tkinter.Frame): The tkinter frame for the error page.

    Returns:
        tkinter.Frame: The frame for the image page or error page based on the validity of the OTP.
    """
    inp_1 = email.get()
    inp_2 = pwd.get()
    #print(inp_1[-10:], inp_2, OTP)
    
    if inp_1[-10:] == "@gmail.com" and inp_2 == OTP:
        return frame3
    else:
        return frame5

def controller():
    """
    Main function to create and manage the GUI frames.
    """
    # GUI for steps
    def show_frame(frame):
        """
        Switches the displayed frame to the given frame.

        Parameters:
            frame (tkinter.Frame): The frame to switch to.
        """
        frame.tkraise()
        
    window = tk.Tk()
    #window.iconbitmap()
    window.state("zoomed")
    window['bg'] = 'white'
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)
    
    # Frames
    frame1 = tk.Frame(window, bg="white")
    frame2 = tk.Frame(window, bg="white")
    frame3 = tk.Frame(window, bg="white")
    frame4 = tk.Frame(window, bg="white")
    frame5 = tk.Frame(window, bg="white")
    frame6 = tk.Frame(window, bg="white")
    
    for frame in (frame1, frame2, frame3, frame4, frame5, frame6):
        frame.grid(row=0, column=0, sticky='nsew')
                
    show_frame(frame1)

    # ... (Remaining code for the GUI) ...

    window.mainloop()

# Call the main controller function to start the GUI
controller()
