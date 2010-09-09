#!/usr/bin/env python

import hashlib

TAM_BLOCO = 2**20 # (1 MiB, um mebibyte)

def hex_hash(obj_hash, nome_arq):
    ''' devolve o hash do arquivo calculado com o objeto hash,
        na forma de uma string hexadecimal '''

    arq = open(nome_arq,'rb') # necessario especificar modo binario no Windows
    while True:
        bloco = arq.read(TAM_BLOCO)
        if not bloco:
            break
        obj_hash.update(bloco)
    arq.close()
    return obj_hash.hexdigest()

if __name__=='__main__':
    import sys
    arq_entrada = ''
    if len(sys.argv) != 2:
        print 'informe o nome do arquivo cujo hash deseja calcular'
    else:
        arq_entrada = sys.argv[1]
        print hex_hash(hashlib.md5(), arq_entrada)    
        
        
        
    
