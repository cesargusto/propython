import ctypes
import sys

if hasattr(ctypes.pythonapi, 'Py_InitModule4'):
    Py_ssize_t = ctypes.c_int
elif hasattr(ctypes.pythonapi, 'Py_InitModule4_64'):
    Py_ssize_t = ctypes.c_int64
else:
    raise TypeError("Cannot determine type of Py_ssize_t")

if sys.maxunicode >= 2**16:
    tam_char = 4
else:
    tam_char = 2



'''
/* from cpython/Include/object.h */

#define PyObject_HEAD                   \
    _PyObject_HEAD_EXTRA                \
    Py_ssize_t ob_refcnt;               \
    struct _typeobject *ob_type;
'''

class PyObject(ctypes.Structure):
    pass # incomplete type: see "15.17.1.16. Incomplete Types"

PyObject._fields_ = [('ob_refcnt', Py_ssize_t),
                     ('ob_type', ctypes.POINTER(PyObject))] # recursive definition



class PyUnicodeObject(PyObject):
    _fields_ = [('ob_length', Py_ssize_t),
                #('ob_str', ctypes.c_wchar_p),
                ('ob_str', ctypes.POINTER(ctypes.c_char)),
                ('ob_shash', ctypes.c_long),
               ]


def dumpbytes(uniobj):
    print ' '.join(''.join(['%02x' % ord(uniobj.ob_str[i+j]) for j in range(tam_char)]) 
            for i in range(0, uniobj.ob_length*tam_char, tam_char))

def shou(unistr):
    print unistr, u'\u2192', repr(unistr)
    obj_uni = PyUnicodeObject.from_address(id(unistr))
    print ' ', 
    dumpbytes(obj_uni)

for unistr in (u'A', u'AB', u'AB\xc7', u'\u6c23'):
    shou(unistr)

if tam_char > 2:
    shou(unichr(0x1F004))

