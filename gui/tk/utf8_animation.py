from Tkinter import *
import tkFont

TOP_MARGIN = 32
RIGHT_MARGIN = 10
LINE_HEIGHT = 90
FONT_SIZE = 55

root = Tk()

bit_font = tkFont.Font(family='Courier', size=FONT_SIZE)

canvas_width, canvas_height = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (canvas_width, canvas_height))

canvas = Canvas(root, width=canvas_width, height=canvas_height, background='black')
canvas.pack()

bits = '0' * 8
#bits = (' '+bits)*4

code_bits = canvas.create_text(canvas_width-RIGHT_MARGIN, TOP_MARGIN, 
    anchor='ne', text=bits, fill='white', font=bit_font)

bits = (' '+bits)*4

utf8_bits = []
bits = '0' * 8
bits_width = bit_font.measure(bits+' ')
for i in range(4):
    utf8_bits.append(canvas.create_text(canvas_width-RIGHT_MARGIN-bits_width*i, 
        TOP_MARGIN+LINE_HEIGHT, 
        anchor='ne', text=bits, fill='dark gray', font=bit_font))   

START = 20
counter = START

def animate():
    global counter
    bits = '{0:08b}'.format(counter)
    counter = int(counter + 1.0/START*counter)
    canvas.itemconfig(code_bits, text=bits)
    try:
        utf_codes = utf8(counter)
    except ValueError:
        counter = START
    else:    
        utf_codes.reverse()
        for i in range(4):
            try:
                bits = '{0:08b}'.format(utf_codes[i])
            except IndexError:
                bits = ' ' * 8
            canvas.itemconfig(utf8_bits[i], text=bits)    
    root.after(100, animate)

clicked = False
def quit(event):
    global clicked
    if clicked:
        root.quit()
    else:
        clicked = True

ranges = [0x007F, 0x07FF, 0xFFFF, 0x10FFFF]

def bytes_needed(code):
    for i, range in enumerate(ranges):
        if code <= range:
            return i+1
    raise ValueError('Code out of range')

def utf8(code):
    needed = bytes_needed(code)
    work_code = code
    if needed == 1:
        res = [code]
    else:
        bytes = []
        prefix = prefix_mask = 128
        for b in range(needed-1):
            bytes.insert(0, (work_code&63)|128)
            prefix_mask >>= 1
            prefix += prefix_mask
            work_code /= 64
        res = [prefix|work_code] + bytes
    #assert unichr(code).encode('utf-8') == ''.join([chr(b) for b in res])
    return res



canvas.bind('<Button-1>', quit)
animate()

mainloop()