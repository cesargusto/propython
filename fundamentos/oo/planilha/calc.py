from cmd import Cmd

class Planilha(Cmd):
    _cels = {}
    _funcs = {}
    def __init__(self, **funcs):
        Cmd.__init__(self)
        self._funcs.update(funcs)
        self.prompt = '> '
        self.cmdloop()
    def __setitem__(self, chave, formula):
        self._cels[chave] = formula
    def formula(self, chave):
        return self._cels[chave]
    def __getitem__(self, chave ):
        return eval(self._cels[chave], self._funcs, self)
    def precmd(self, linha):
        if '=' in linha:
            linha = 'def ' + linha.strip()
        else:
            linha = 'calc ' + linha.strip()
        return linha
    def do_def(self, linha):
        local, formula = linha.split('=')
        self[local.strip()] = formula
        
    def do_calc(self, linha):
        print self[linha]  

if __name__ == "__main__":
    p = Planilha()
    
    
