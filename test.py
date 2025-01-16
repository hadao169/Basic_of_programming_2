import ctypes
a = 5

def change(a):
  print(hex(id(a)))

  a = 10
  print(hex(id(a)))

  return a
  
print(change(a))


print(hex(id(a)))
print(a)

b=15
print(id(b))
b="hello"
print(hex(id(b)))
print(b)

value = ctypes.cast(140726239552744, ctypes.POINTER(ctypes.py_object)).contents.value
print(value)