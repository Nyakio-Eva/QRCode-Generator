# QRCode-Generator
This project is a simple QR code generator built using the qrcode Python package. It allows you to input any data, such as text or a URL, and generate a QR code image from it.

### Features
- Generate QR codes from any text or URL.
- Save the QR code as an image file (PNG, JPG).
- Customize the size and border of the generated QR code.

### Requirements
To run this project, you will need Python 3.x and the following package:

        qrcode: To install, run:
        pipenv install qrcode
        
        install pillow for color customization
        pipenv install pillow



### Usage
1. Clone the repository:  

       git@github.com:Nyakio-Eva/QRCode-Generator.git   

2. Navigate to the project directory:

       cd qrcode-generator

3. Run the Python script:
    ```bash
       python3 qr.py
       python3 advancedqr.py

4. Input the text or URL and name of file when prompted, and the QR code will be generated and saved as an image file.    

### Customization
You can modify the QR code's size, border, color or file name by updating the script:

    Size: Change the box_size parameter in the code to       adjust the QR code's size.
    Border: Update the border parameter to control the thickness around the QR code.
    color: Add a hex code or color name of your choice in the fill_color and back_color sections

### Contributing
Contributions are welcome! If you have ideas for additional features or improvements, feel free to open a pull request or issue.

### License
This project is licensed under the MIT License. See the LICENSE file for details.



