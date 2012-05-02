import ctypes
from pprint import pprint

if hasattr(ctypes.pythonapi, 'Py_InitModule4'):
    Py_ssize_t = ctypes.c_int
elif hasattr(ctypes.pythonapi, 'Py_InitModule4_64'):
    Py_ssize_t = ctypes.c_int64
else:
    raise TypeError("Cannot determine type of Py_ssize_t")

print 'sizeof(Py_ssize_t) = %s bytes' % ctypes.sizeof(Py_ssize_t) 

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


print 'sizeof(PyObject) = %s bytes' % ctypes.sizeof(PyObject) 


'''
/* from cpython/Include/intobject.h */

typedef struct {
    PyObject_HEAD
    long ob_ival;
} PyIntObject;
'''
class PyIntObject(PyObject):
    _fields_ = [('ob_ival', ctypes.c_long)]

print 'sizeof(PyIntObject) = %s bytes' % ctypes.sizeof(PyIntObject) 

'''
/* from cpython/Include/object.h */
#define PyObject_VAR_HEAD               \
    PyObject_HEAD                       \
    Py_ssize_t ob_size; /* Number of items in variable part */
'''

'''
/* from cpython/Include/stringobject.h */
typedef struct {
    PyObject_VAR_HEAD
    long ob_shash;
    int ob_sstate;
    char ob_sval[1];

    /* Invariants:
     *     ob_sval contains space for 'ob_size+1' elements.
     *     ob_sval[ob_size] == 0.
     *     ob_shash is the hash of the string or -1 if not computed yet.
     *     ob_sstate != 0 iff the string object is in stringobject.c's
     *       'interned' dictionary; in this case the two references
     *       from 'interned' to this object are *not counted* in ob_refcnt.
     */
} PyStringObject;
'''

class PyStringObject(PyObject):
    _fields_ = [('ob_size', Py_ssize_t),
                ('ob_shash', ctypes.c_long),
                ('ob_sstate', ctypes.c_int),
                ('ob_sval', ctypes.POINTER(ctypes.c_char)),
               ]

print 'sizeof(PyStringObject) = %s bytes' % ctypes.sizeof(PyStringObject) 

def show_attrs(obj):
    for name in dir(obj):
        if name.startswith('ob_'):
            val = getattr(obj, name)
            print '{0:10} = {1!r}'.format(name,val)

print '*' * 20, 'n = 42'
n = 42
obj_n = PyIntObject.from_address(id(n))
show_attrs(obj_n)

print '*' * 20, "s0 = ''"
s0 = ''
obj_s0 = PyStringObject.from_address(id(s0))
show_attrs(obj_s0)

print '*' * 20, "s1 = 'ABC'"
s1 = 'ABC'
obj_s1 = PyStringObject.from_address(id(s1))
show_attrs(obj_s1)

print obj_s1.ob_sval.contents

