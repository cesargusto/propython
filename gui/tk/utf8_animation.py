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
    utf8_bits = canvas.create_text(canvas_width-RIGHT_MARGIN-bits_width*i, 
        TOP_MARGIN+LINE_HEIGHT, 
        anchor='ne', text=bits, fill='dark gray', font=bit_font)    


counter = 0

def animate():
    global counter
    bits = '{0:08b}'.format(counter)
    counter += 1
    canvas.itemconfig(code_bits, text=bits)
    root.after(1, animate)

clicked = False
def quit(event):
    global clicked
    if clicked:
        root.quit()
    else:
        clicked = True

canvas.bind('<Button-1>', quit)
animate()

mainloop()