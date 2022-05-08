"""
This is example of printing using win32printing and works only
on WINDOWS and only using standard printer driver
Tested with this printer: https://www.aibecy.com/p-os0287us.html
Source: https://pypi.org/project/win32printing/
Install: pip install win32printing
In order to use this example please install generic printer driver or driver provided from
printer manufacturer. -> https://www.aibecy.com/p-os0287us.html
"""

from win32printing import Printer

font = {
    "height": 20,
}
with Printer(linegap=1) as printer:
    printer.text("Hello World", font_config=font, align="center")
    printer.new_page()