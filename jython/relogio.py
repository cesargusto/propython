from javax.swing import *
from java.awt import Font
from time import strftime

class Relogio(JFrame):
    def __init__(self):
        JFrame.__init__(self, u'TicTac',
            defaultCloseOperation = JFrame.DISPOSE_ON_CLOSE)
        self.mostrador = JLabel('00:00:00',
            font=Font('Sanserif',Font.BOLD, 70))
        self.contentPane.add(self.mostrador)
        self.pack()
        self.visible = True

    def start(self):
        def tic(evento):
            agora = strftime('%H:%M:%S')
            if self.mostrador.text != agora:
                self.mostrador.text = agora
        Timer(100, tic).start()

if __name__=='__main__':
    rel = Relogio()
    rel.start()

DEMO = '''
from relogio import Relogio
rel = Relogio()
rel.start()

from java.awt import *
rel.mostrador.foreground = Color.RED

print rel.mostrador.text

from time import sleep
while True:
    if rel.mostrador.text.endswith('0'):
        print 'PING', rel.mostrador.text
    sleep(1)
     
'''
