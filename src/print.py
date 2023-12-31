from __future__ import print_function
from escpos import printer
import reader

# Sends a specified shopping list to the printer
def main():    
    p = printer.Usb(0x0416,0x5011,in_ep=0x81,out_ep=0x03)
    p.text("\n\n")
    p.set(align="center")    
    p.text('\n*******************************\n')
    p.text("CURRENT SHOPPING LIST:\n")
    p.text('----------------------\n')
    p.set(align='left') 
    for item in reader.read_file('shopping_list.txt'):
        p.text('[ ] ' + item + '\n\n')
    p.set(align='center')
    p.text('\n*******************************\n\n\n\n\n\n')
if __name__ == '__main__':
    main()
