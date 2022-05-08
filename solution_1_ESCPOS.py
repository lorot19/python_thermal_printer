"""
This is example of printing using python-escpos module
Tested with this printer: https://www.aibecy.com/p-os0287us.html
Source: https://github.com/python-escpos/python-escpos
Install: pip install python-escpos
if you got this error:
    error in mongoengine setup command: use_2to3 is invalid.
    //For windows
    pip install setuptools==58 --upgrade --ignore-installed
    //For linux, macOS
    sudo -H pip install -U pip setuptools==58

IMPORTANT FOR WIN USERS:
This module is dependant on pyUSB module which is quite tricky
on WIN machines. Most probably you will get noBackend error or
no device found. To fix that problems few things needs to be done:

1. if not, install pyUSB -> pip install pyusb
2. download libUSB driver -> https://github.com/libusb/libusb/releases/tag/v1.0.20
    and copy DLL files to system32 folder
3. comment following lines in printer.py for more info:
    -> https://nyorikakar.medium.com/printing-with-python-and-epson-pos-printer-fbd17e127b6c
    try:
        check_driver = self.device.is_kernel_driver_active(0)
    except NotImplementedError:
        pass
    if check_driver is None or check_driver:
        try:
           self.device.detach_kernel_driver(0)
        except usb.core.USBError as e:
            if check_driver is not None:
                print("Could not detatch kernel driver: {0}".format(str(e)))
4. sometimes also zadig tool could be very useful: https://zadig.akeo.ie
"""
#

from escpos.printer import Usb

p = Usb(0x6868, 0x0200)
p.text("This is example of printing\n")
p.image("image.png")
p.barcode('1324354657687', 'EAN13', 64, 2, '', '')
p.qr("hello", size=5)
p.cut()