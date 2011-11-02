#################### 01
2**1000
'Garoa Hacker Clube'[::-1]
p = 3j+4
_
type(p)
p.real, p.imag
abs(p)
dir()
help(p) #
#################### 03
1.1
print 1.1
s = 'maçã'
s
print s
2**100
print repr(2**100)
print repr(s)
repr(2**100)
repr(s)
eval(repr(s))
#################### 04a
def dobro(n):
  '''devolve n*2'''
  return n*2
#################### 04b
dobro(21)
dobro('Clube')
l = [30, 20, 60]
dobro(l)
[dobro(n) for n in l]
x2 = dobro
x2(3j+4)
x2
x2.__doc__
help(x2) #
#################### 06
dir(dobro)
dobro.__code__
dir(dobro.__code__)
dobro.__code__.co_argcount
dobro.__code__.co_varnames
dobro.__code__.co_code
import dis
dis.dis(_)
##################### 07
import Tkinter
import time

relogio = Tkinter.Label() # (1)
relogio.pack()
relogio['text'] = time.strftime('%H:%M:%S')
relogio['font'] = 'Helvetica 96 bold'

def tictac():
    agora = time.strftime('%H:%M:%S')
    if agora != relogio['text']:
        relogio['text'] = agora
    relogio.after(200, tictac)

tictac()
relogio['fg'] = 'red'
relogio.mainloop()

##################### 08


