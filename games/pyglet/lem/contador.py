class Contador(object):
    def __init__(self):
        self.dic = {}
            
    def incluir(self, item):
        qtd = self.dic.get(item, 0) + 1
        self.dic[item] = qtd
        return qtd
        
    def contar(self, item):
        return self.dic[item]
        
class ContadorTolerante(Contador):
    
    def contar(self, item):
        return self.dic.get(item, 0)
        
class ContadorTotalizador(Contador):

    def __init__(self):
        #Contador.__init__(self)
        super(ContadorTotalizador, self).__init__()
        self.total = 0
            
    def incluir(self, item):
        self.total += 1
        #Contador.incluir(self, item)
        super(ContadorTotalizador, self).incluir(item)
                
    def pct(self, item):
        return float(self.contar(item)) / self.total * 100
        
class ContadorTotalizadorTolerante(ContadorTolerante, ContadorTotalizador):
    pass
    

         

