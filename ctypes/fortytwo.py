# coding: utf-8

'''
Copiado de:
"Deixando o interpretador Python maluco por diversão e lucro, ou 
 Como se livrar de um colega de trabalho desenvolvedor Python"

http://lameiro.wordpress.com/2010/07/18/deixando-o-interpretador-python-maluco/

'''

import ctypes

if hasattr(ctypes.pythonapi, 'Py_InitModule4'):
    Py_ssize_t = ctypes.c_int
elif hasattr(ctypes.pythonapi, 'Py_InitModule4_64'):
    Py_ssize_t = ctypes.c_int64
else:
    raise TypeError("Cannot determine type of Py_ssize_t")

print 'Py_ssize_t =', Py_ssize_t 

class PyObject(ctypes.Structure):
    pass # incomplete type

class PyObject(ctypes.Structure):
    _fields_ = [('ob_refcnt', Py_ssize_t),
                ('ob_type', ctypes.POINTER(PyObject))]

class PyIntObject(PyObject):
    _fields_ = [('ob_ival', ctypes.c_long)]

forty_two_object = PyIntObject.from_address(id(42))
forty_two_object.ob_ival = 0

print 42 == 0

