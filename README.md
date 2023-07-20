## Image To Sketch GUI

This code provides a graphical user interface (GUI) for converting images to pencil sketches. The GUI is built using the `tkinter` library in Python and utilizes various modules for image processing, email communication, and QR code generation.

### Requirements

- Python 3.x
- OpenCV
- tkinter
- PIL (Python Imaging Library)
- qrcode
- smtplib

### Functionality

1. `open_img(frame3)`: Opens a file dialog to select an image file.

2. `see_image(frame3)`: Reads an image file using OpenCV.

3. `create_sketch(frame3, frame6)`: Converts the selected image to a pencil sketch using OpenCV and displays it.

4. `Sketch_IT_server(inp_1, frame1)`: Sends the converted pencil sketch via email using Gmail.

5. `OTP_gen()`: Generates a random 6-digit OTP (One-Time Password).

6. `QR_code(s)`: Creates a QR code from the given text.

7. `Gmail_OTP_server(inp_1)`: Sends the OTP and QR code via email for Gmail verification.

8. `Gmail_id(frame4, frame5)`: Verifies the Gmail id and sends the OTP for verification.

9. `verify(OTP, frame3, frame5)`: Verifies the OTP for Gmail login credentials.

10. `controller()`: Main function to create and manage the GUI frames.

### Usage

To use the GUI, run the script, and a window will appear with options to select an image, convert it to a pencil sketch, and send it via email using Gmail. The process involves verifying the Gmail id with OTP authentication.

Ensure that the required Python libraries are installed before running the script.

Please note that the email credentials and paths for saving images should be set appropriately for the code to work as intended.

For any questions or issues, please contact Shrihan Tayal (author of the code).
